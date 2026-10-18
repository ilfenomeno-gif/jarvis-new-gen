"""Local text-to-3D (SD-Turbo -> TripoSR), no external API. No torch import here.

The heavy work runs in a subprocess (core/local_3d_worker.py): VRAM is released when it
exits, a crash cannot take JARVIS down, and out-of-memory becomes a clear message.
TripoSR is image-to-3D only, so the prompt is first turned into a picture.
Setup: see requirements-3d.txt and ``python -m core.local_3d_gen setup``.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

from core.model_gen import clean_prompt, model_name
from core.viewer3d import MAX_MODEL_BYTES, MODELS_DIR

BASE = Path(__file__).resolve().parent.parent
TRIPOSR_DIR = Path(os.environ.get("TRIPOSR_DIR") or BASE / "third_party" / "TripoSR")
TRIPOSR_REPO = "https://github.com/VAST-AI-Research/TripoSR.git"
SF3D_DIR = Path(os.environ.get("SF3D_DIR") or BASE / "third_party" / "stable-fast-3d")
SF3D_REPO = "https://github.com/Stability-AI/stable-fast-3d.git"
MIN_VRAM_GB = 6.0
DEFAULT_TIMEOUT = 1800.0
RESULT_PREFIX = "JARVIS_RESULT "

SETUP_MESSAGE = (
    "Local 3D generation is not installed. Run 'python -m core.local_3d_gen setup', then "
    "'pip install -r requirements-3d.txt' (see the file for the CUDA build of torch)."
)
OOM_MESSAGE = (
    "The GPU ran out of memory. Close other GPU programs (games, video editors, browsers "
    "with hardware acceleration) and retry, or use the Tripo backend."
)


def python_exe() -> str:
    exe = os.environ.get("JARVIS_3D_PYTHON") or sys.executable
    path = Path(exe)
    if path.name.lower() == "pythonw.exe":  # pythonw has no stdout to read the result from
        sibling = path.with_name("python.exe")
        if sibling.exists():
            return str(sibling)
    return exe


def is_installed() -> bool:
    """Cheap check (no torch import): torch present and the TripoSR sources cloned."""
    return importlib.util.find_spec("torch") is not None and (TRIPOSR_DIR / "tsr").is_dir()


def _run(cmd: list[str], timeout: float):
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "TRIPOSR_DIR": str(TRIPOSR_DIR), "SF3D_DIR": str(SF3D_DIR)}
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=timeout, creationflags=flags, cwd=str(BASE), env=env)
    return proc.returncode, proc.stdout, proc.stderr


def _parse_result(stdout: str) -> dict | None:
    for line in reversed((stdout or "").splitlines()):
        if line.startswith(RESULT_PREFIX):
            try:
                return json.loads(line[len(RESULT_PREFIX):])
            except ValueError:
                return None
    return None


def probe(runner=None, timeout: float = 180.0) -> dict:
    """Hardware/dependency report from the worker: {torch, cuda, gpu, vram_gb, missing}."""
    runner = runner or _run
    try:
        code, out, err = runner([python_exe(), "-m", "core.local_3d_worker", "--probe"], timeout)
    except Exception as exc:
        return {"torch": False, "cuda": False, "missing": [f"probe failed: {type(exc).__name__}"]}
    result = _parse_result(out)
    if result is None:
        return {"torch": False, "cuda": False, "missing": ["torch"]}
    return result


def readiness_problem(info: dict) -> str | None:
    """A user-facing reason why local generation cannot run, or None when it can."""
    if not info.get("torch"):
        return SETUP_MESSAGE
    if info.get("missing"):
        return "Local 3D generation is missing: " + ", ".join(info["missing"]) + ". " + SETUP_MESSAGE
    if not info.get("cuda"):
        return ("No CUDA GPU found: local 3D generation on CPU would take far too long. "
                "Install the CUDA build of torch (requirements-3d.txt) or use the Tripo backend.")
    vram = float(info.get("vram_gb") or 0)
    if vram < MIN_VRAM_GB:
        return (f"The GPU ({info.get('gpu', '?')}) has {vram:.1f} GB of VRAM; TripoSR needs about "
                f"{MIN_VRAM_GB:.0f} GB. Use the Tripo backend instead.")
    return None


def generate_local(prompt, models_dir: Path | None = None, runner=None,
                   timeout: float = DEFAULT_TIMEOUT, image: Path | None = None) -> Path:
    """Blocking: run in a worker thread. Returns the saved .glb path.

    With ``image`` (a sanitised PNG from core.image_input) the SD-Turbo stage is skipped and
    TripoSR reconstructs the picture directly; ``prompt`` then only names the model file.
    """
    prompt = clean_prompt(prompt)
    models_dir = Path(models_dir or MODELS_DIR)
    models_dir.mkdir(parents=True, exist_ok=True)
    runner = runner or _run
    problem = readiness_problem(probe(runner))
    if problem:
        raise RuntimeError(problem)

    tmp = models_dir / f".tmp-{uuid.uuid4().hex[:8]}"
    tmp.mkdir(parents=True)
    out_file = tmp / "model.glb"
    try:
        cmd = [python_exe(), "-m", "core.local_3d_worker", "--out", str(out_file)]
        cmd += ["--image", str(image)] if image else ["--prompt", prompt]
        try:
            code, stdout, stderr = runner(cmd, timeout)
        except subprocess.TimeoutExpired:
            raise RuntimeError("Local 3D generation timed out (the first run downloads several GB "
                               "of models; retry once they are cached).") from None
        result = _parse_result(stdout)
        if result is None:
            tail = " ".join((stderr or "").strip().splitlines()[-2:])[:300]
            if "out of memory" in (stderr or "").lower():
                raise RuntimeError(OOM_MESSAGE)
            raise RuntimeError(f"Local generator crashed (exit {code}): {tail or 'no output'}")
        if not result.get("ok"):
            if result.get("code") == "oom":
                raise RuntimeError(OOM_MESSAGE)
            raise RuntimeError(f"Local generation failed: {result.get('message', 'unknown error')}")
        if not out_file.is_file():
            raise RuntimeError("Local generator reported success but wrote no file")
        if out_file.stat().st_size > MAX_MODEL_BYTES:
            raise RuntimeError("generated model is too large")
        with out_file.open("rb") as handle:
            if handle.read(4) != b"glTF":
                raise RuntimeError("generated file is not a valid .glb")
        digest = hashlib.sha1(Path(image).read_bytes()).hexdigest() if image else ""
        target = models_dir / model_name(prompt + digest)
        shutil.move(str(out_file), target)
        return target
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _clone(repo: str, target: Path, marker: str, label: str) -> str:
    if (target / marker).is_dir():
        return f"{label} already present in {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(["git", "clone", "--depth", "1", repo, str(target)], capture_output=True, text=True)
    if proc.returncode != 0:
        return f"{label}: git clone failed: " + (proc.stderr or "").strip()[-300:]
    return f"{label} cloned into {target}"


def setup() -> str:
    """Clone TripoSR (MIT) and Stable Fast 3D next to the code; torch etc. are pip-installed.

    SF3D is optional: its CUDA/C++ extensions (texture_baker, uv_unwrapper) must be built with MSVC
    (see requirements-3d.txt) and its weights are gated on Hugging Face. Without them the worker uses TripoSR.
    """
    return "\n".join([
        _clone(TRIPOSR_REPO, TRIPOSR_DIR, "tsr", "TripoSR"),
        _clone(SF3D_REPO, SF3D_DIR, "sf3d", "Stable Fast 3D"),
    ])

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "status"
    if command == "setup":
        print(setup())
    else:
        info = probe()
        print(json.dumps(info, indent=2))
        print(readiness_problem(info) or "Local 3D generation is ready.")
