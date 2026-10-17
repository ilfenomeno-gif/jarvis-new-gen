"""Safe image input for image-to-3D: a local file or a web URL becomes a sanitised PNG.

Only the re-encoded PNG reaches the 3D worker. Downloads accept http/https only, refuse
private/loopback addresses (also after redirects), and are capped in size and time.
"""
from __future__ import annotations

import ipaddress
import re
import socket
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

MAX_IMAGE_BYTES = 15 * 1024 * 1024
MAX_PIXELS = 40_000_000
MAX_SIDE = 1024
MAX_REDIRECTS = 4
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff"}


def _check_public_host(host: str) -> None:
    if not host:
        raise ValueError("image_url has no host")
    try:
        infos = socket.getaddrinfo(host, None)
    except OSError:
        raise ValueError(f"cannot resolve host '{host}'") from None
    for info in infos:
        address = ipaddress.ip_address(info[4][0].split("%")[0])
        if not address.is_global:
            raise ValueError("image_url must point to a public web address")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _open(url: str, opener, timeout: float):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 jarvis-image-to-3d",
                                                   "Accept": "image/*"})
    return opener.open(request, timeout=timeout)


def download_image(url, timeout: float = 20.0, opener=None, resolver=_check_public_host) -> bytes:
    url = str(url or "").strip()
    if len(url) > 2000:
        raise ValueError("image_url is too long")
    opener = opener or urllib.request.build_opener(_NoRedirect)
    for _ in range(MAX_REDIRECTS + 1):
        parts = urllib.parse.urlsplit(url)
        if parts.scheme not in ("http", "https") or parts.username or parts.password:
            raise ValueError("image_url must be a plain http(s) link")
        resolver(parts.hostname or "")
        try:
            response = _open(url, opener, timeout)
        except urllib.error.HTTPError as exc:
            if exc.code in (301, 302, 303, 307, 308) and exc.headers.get("Location"):
                url = urllib.parse.urljoin(url, exc.headers["Location"])
                continue
            raise ValueError(f"download failed: HTTP {exc.code}") from None
        except (urllib.error.URLError, OSError) as exc:
            raise ValueError(f"download failed: {getattr(exc, 'reason', exc)}") from None
        with response:
            data = response.read(MAX_IMAGE_BYTES + 1)
        if len(data) > MAX_IMAGE_BYTES:
            raise ValueError("the image is too large (max 15 MB)")
        return data
    raise ValueError("too many redirects")


def sanitise_image(data: bytes, dest_dir: Path) -> Path:
    """Decode with Pillow (rejects non-images), shrink and re-encode as PNG in dest_dir."""
    from PIL import Image
    import io
    Image.MAX_IMAGE_PIXELS = MAX_PIXELS
    try:
        image = Image.open(io.BytesIO(data))
        image.load()
    except Exception:
        raise ValueError("the file is not a readable image (png, jpg, webp, bmp, gif)") from None
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGBA" if "transparency" in image.info or image.mode in ("LA", "PA") else "RGB")
    image.thumbnail((MAX_SIDE, MAX_SIDE))
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / f"input-{uuid.uuid4().hex[:8]}.png"
    image.save(target, "PNG")
    return target


def read_local_image(path) -> bytes:
    text = str(path or "").strip().strip('"')
    if not text:
        raise ValueError("image_path is empty")
    file = Path(text).expanduser().resolve()
    if file.suffix.lower() not in IMAGE_EXTENSIONS:
        raise ValueError("image_path must be an image file (png, jpg, webp, bmp, gif)")
    if not file.is_file():
        raise ValueError(f"image not found: {file}")
    if file.stat().st_size > MAX_IMAGE_BYTES:
        raise ValueError("the image is too large (max 15 MB)")
    return file.read_bytes()


def label_for(image_path=None, image_url=None) -> str:
    """Short readable name used for the saved model file."""
    raw = Path(str(image_path)).stem if image_path else Path(urllib.parse.urlsplit(str(image_url)).path).stem
    slug = re.sub(r"[^a-z0-9]+", " ", raw.lower()).strip()[:60]
    return "image " + (slug or "model")


def prepare_image(image_path, image_url, dest_dir: Path, **kwargs) -> Path:
    """Validated PNG copy of the user's image; exactly one of image_path / image_url."""
    if image_path and image_url:
        raise ValueError("give either image_path or image_url, not both")
    if not image_path and not image_url:
        raise ValueError("image_path is empty")
    data = read_local_image(image_path) if image_path else download_image(image_url, **kwargs)
    return sanitise_image(data, dest_dir)
