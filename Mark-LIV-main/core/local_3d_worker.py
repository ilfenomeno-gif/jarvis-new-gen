"""Heavy worker for local text-to-3D. Runs in its own process (see core/local_3d_gen.py).

Stage 1: SD-Turbo makes a picture of the prompt. Stage 2: TripoSR reconstructs it as a
mesh, saved as .glb. The models are loaded one after the other to fit in 8 GB of VRAM.
The last stdout line is ``JARVIS_RESULT {json}``.
"""
from __future__ import annotations

import argparse
import gc
import json
import os
import sys
from pathlib import Path

RESULT_PREFIX = "JARVIS_RESULT "
TEXT2IMG_MODEL = os.environ.get("JARVIS_3D_TEXT2IMG", "stabilityai/sd-turbo")
TRIPOSR_MODEL = os.environ.get("JARVIS_3D_TRIPOSR", "stabilityai/TripoSR")
# (marching-cubes resolution, chunk size): retried smaller after an out-of-memory
QUALITY_STEPS = [(256, 8192), (192, 4096), (128, 2048)]
PROMPT_SUFFIX = ", single object, centered, plain white background, studio lighting, high detail"


def emit(payload: dict) -> None:
    print(RESULT_PREFIX + json.dumps(payload), flush=True)


def triposr_dir() -> Path:
    return Path(os.environ.get("TRIPOSR_DIR") or Path(__file__).resolve().parent.parent / "third_party" / "TripoSR")


def _missing_modules() -> list[str]:
    import importlib.util
    needed = ["diffusers", "transformers", "rembg", "trimesh", "omegaconf", "einops", "PIL", "huggingface_hub"]
    missing = [name for name in needed if importlib.util.find_spec(name) is None]
    if not (triposr_dir() / "tsr").is_dir():
        missing.append("TripoSR sources (run: python -m core.local_3d_gen setup)")
    return missing


def probe() -> dict:
    try:
        import torch
    except ImportError:
        return {"torch": False, "cuda": False, "missing": ["torch"]}
    info = {"torch": True, "torch_version": torch.__version__, "cuda": bool(torch.cuda.is_available()),
            "missing": _missing_modules()}
    if info["cuda"]:
        props = torch.cuda.get_device_properties(0)
        info.update(gpu=props.name, vram_gb=round(props.total_memory / 1024 ** 3, 2))
    return info


def _free(torch) -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _text_to_image(prompt: str, torch):
    from diffusers import AutoPipelineForText2Image
    pipe = AutoPipelineForText2Image.from_pretrained(TEXT2IMG_MODEL, torch_dtype=torch.float16, variant="fp16")
    pipe.to("cuda")
    try:
        # SD-Turbo is distilled for one step without guidance
        return pipe(prompt=prompt + PROMPT_SUFFIX, num_inference_steps=2, guidance_scale=0.0,
                    width=512, height=512).images[0]
    finally:
        del pipe
        _free(torch)


def _install_marching_cubes_fallback() -> None:
    """torchmcubes has no Windows wheel and must be compiled; use scikit-image instead.

    torchmcubes returns vertices as (axis2, axis1, axis0) with inside = value < level;
    skimage returns (axis0, axis1, axis2), so reverse the axes and the face winding.
    """
    try:
        import torchmcubes  # noqa: F401
        return
    except ImportError:
        pass
    import types

    import numpy as np
    import torch
    from skimage.measure import marching_cubes as sk_marching_cubes

    def marching_cubes(vol, thresh):
        volume = vol.detach().cpu().numpy().astype(np.float32)
        verts, faces, _, _ = sk_marching_cubes(volume, level=float(thresh))
        verts = np.ascontiguousarray(verts[:, ::-1])
        faces = np.ascontiguousarray(faces[:, ::-1])
        return torch.from_numpy(verts.copy()).float(), torch.from_numpy(faces.astype(np.int64))

    module = types.ModuleType("torchmcubes")
    module.marching_cubes = marching_cubes
    sys.modules["torchmcubes"] = module


def _image_to_mesh(image, torch):
    _install_marching_cubes_fallback()
    sys.path.insert(0, str(triposr_dir()))
    import numpy as np
    import rembg
    from PIL import Image
    from tsr.system import TSR
    from tsr.utils import remove_background, resize_foreground

    session = rembg.new_session()
    cut = resize_foreground(remove_background(image, session), 0.85)
    arr = np.array(cut).astype(np.float32) / 255.0
    arr = arr[:, :, :3] * arr[:, :, 3:4] + (1 - arr[:, :, 3:4]) * 0.5
    prepared = Image.fromarray((arr * 255.0).astype(np.uint8))

    model = TSR.from_pretrained(TRIPOSR_MODEL, config_name="config.yaml", weight_name="model.ckpt")
    model.to("cuda")
    try:
        last_oom = None
        for resolution, chunk in QUALITY_STEPS:
            try:
                model.renderer.set_chunk_size(chunk)
                with torch.no_grad():
                    codes = model([prepared], device="cuda")
                return model.extract_mesh(codes, True, resolution=resolution)[0]
            except torch.cuda.OutOfMemoryError as exc:
                last_oom = exc
                _free(torch)
        raise last_oom
    finally:
        del model
        _free(torch)


def _to_gltf_y_up(mesh):
    """TripoSR meshes are Z-up; glTF/Three.js are Y-up (y' = z, z' = -y)."""
    import numpy as np
    from trimesh.transformations import rotation_matrix
    mesh.apply_transform(rotation_matrix(-np.pi / 2, [1, 0, 0]))
    return mesh


def generate(prompt: str, out: Path) -> dict:
    import torch
    if not torch.cuda.is_available():
        return {"ok": False, "code": "no_cuda", "message": "no CUDA GPU available"}
    try:
        image = _text_to_image(prompt, torch)
        image.save(out.with_suffix(".png"))
        mesh = _to_gltf_y_up(_image_to_mesh(image, torch))
        mesh.export(str(out))
    except torch.cuda.OutOfMemoryError:
        _free(torch)
        return {"ok": False, "code": "oom", "message": "CUDA out of memory"}
    except Exception as exc:
        return {"ok": False, "code": "error", "message": f"{type(exc).__name__}: {exc}"[:400]}
    return {"ok": True, "path": str(out), "vertices": int(len(mesh.vertices)), "faces": int(len(mesh.faces))}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--prompt")
    parser.add_argument("--out")
    args = parser.parse_args(argv)
    if args.probe:
        emit(probe())
        return 0
    if not args.prompt or not args.out:
        emit({"ok": False, "code": "error", "message": "--prompt and --out are required"})
        return 2
    result = generate(args.prompt, Path(args.out))
    emit(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
