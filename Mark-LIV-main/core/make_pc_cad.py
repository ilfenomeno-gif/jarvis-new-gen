"""Builds a small multi-part PC as assets/viewer3d/models/cad/pc.glb (needs trimesh).

No PC model exists among the free Khronos samples, so it is generated here. Every part is its
own named node, so viewer_3d explode_model separates them and the hover tooltip shows the name.
Run: python -m core.make_pc_cad
"""
from __future__ import annotations

from pathlib import Path

from core.viewer3d import MODELS_DIR

# name -> (size x, y, z, centre x, y, z, RGBA). Units are arbitrary; the viewer rescales.
# The left side of the case (x = -1) is open so the internals stay visible.
PARTS = {
    "motherboard": ((0.06, 1.7, 1.5), (0.7, 0.0, 0.0), (20, 110, 60, 255)),
    "cpu": ((0.08, 0.3, 0.3), (0.62, 0.35, 0.0), (190, 190, 200, 255)),
    "cpu_cooler": ((0.3, 0.45, 0.45), (0.4, 0.35, 0.0), (90, 100, 120, 255)),
    "ram_1": ((0.08, 0.6, 0.12), (0.62, 0.35, 0.5), (30, 30, 40, 255)),
    "ram_2": ((0.08, 0.6, 0.12), (0.62, 0.35, 0.68), (30, 30, 40, 255)),
    "gpu": ((0.35, 0.18, 1.1), (0.45, -0.25, 0.0), (160, 30, 30, 255)),
    "psu": ((1.0, 0.5, 0.7), (-0.0, -0.95, -0.6), (50, 50, 55, 255)),
    "fan": ((0.12, 0.5, 0.5), (0.1, 0.0, -0.95), (0, 170, 220, 255)),
}
CASE_COLOR = (70, 80, 95, 255)
WALL = 0.05


def _case_mesh(trimesh):
    """Open-sided case shell as one mesh: floor, ceiling, back and right panels."""
    h = 1.0
    panels = [
        ((2.0, WALL, 2.0), (0.0, -h, 0.0)),
        ((2.0, WALL, 2.0), (0.0, h, 0.0)),
        ((2.0, 2.0, WALL), (0.0, 0.0, -1.0)),
        ((WALL, 2.0, 2.0), (1.0, 0.0, 0.0)),
    ]
    boxes = []
    for extents, centre in panels:
        box = trimesh.creation.box(extents=extents)
        box.apply_translation(centre)
        boxes.append(box)
    case = trimesh.util.concatenate(boxes)
    case.visual.face_colors = CASE_COLOR
    return case


def build_scene():
    try:
        import trimesh
    except ImportError as exc:
        raise RuntimeError("trimesh is not installed: pip install -r requirements-3d.txt") from exc
    scene = trimesh.Scene()
    scene.add_geometry(_case_mesh(trimesh), node_name="case", geom_name="case")
    for name, (extents, centre, color) in PARTS.items():
        mesh = trimesh.creation.box(extents=extents)
        mesh.apply_translation(centre)
        mesh.visual.face_colors = color
        scene.add_geometry(mesh, node_name=name, geom_name=name)
    return scene


def make_pc_cad(dest: Path | None = None) -> Path:
    target = Path(dest or MODELS_DIR / "cad") / "pc.glb"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(build_scene().export(file_type="glb"))
    return target


if __name__ == "__main__":
    print(f"Saved {make_pc_cad()}")
