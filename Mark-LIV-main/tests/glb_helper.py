"""Builds a tiny valid .glb (two named nodes) so viewer tests need no network or assets."""
import json
import struct


def make_glb(path) -> None:
    positions = struct.pack("<9f", 0, 0, 0, 1, 0, 0, 0, 1, 0)
    gltf = {
        "asset": {"version": "2.0"},
        "scene": 0,
        "scenes": [{"nodes": [0, 1]}],
        "nodes": [
            {"name": "part_a", "mesh": 0, "translation": [-1, 0, 0]},
            {"name": "part_b", "mesh": 0, "translation": [1, 0, 0]},
        ],
        "meshes": [{"primitives": [{"attributes": {"POSITION": 0}}]}],
        "accessors": [{
            "bufferView": 0, "componentType": 5126, "count": 3, "type": "VEC3",
            "min": [0, 0, 0], "max": [1, 1, 0],
        }],
        "bufferViews": [{"buffer": 0, "byteLength": len(positions)}],
        "buffers": [{"byteLength": len(positions)}],
    }
    js = json.dumps(gltf).encode()
    js += b" " * (-len(js) % 4)
    total = 12 + 8 + len(js) + 8 + len(positions)
    blob = struct.pack("<III", 0x46546C67, 2, total)
    blob += struct.pack("<II", len(js), 0x4E4F534A) + js
    blob += struct.pack("<II", len(positions), 0x004E4942) + positions
    with open(path, "wb") as f:
        f.write(blob)

def make_animated_glb(path) -> None:
    """One triangle node 'cpu' with a 1 s translation clip named 'spin'."""
    data = struct.pack("<9f", 0, 0, 0, 1, 0, 0, 0, 1, 0) + struct.pack("<2f", 0, 1) + struct.pack("<6f", 0, 0, 0, 0, 1, 0)
    gltf = {
        "asset": {"version": "2.0"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": [{"name": "cpu", "mesh": 0}],
        "meshes": [{"primitives": [{"attributes": {"POSITION": 0}}]}],
        "animations": [{
            "name": "spin",
            "samplers": [{"input": 1, "output": 2, "interpolation": "LINEAR"}],
            "channels": [{"sampler": 0, "target": {"node": 0, "path": "translation"}}],
        }],
        "accessors": [
            {"bufferView": 0, "componentType": 5126, "count": 3, "type": "VEC3", "min": [0, 0, 0], "max": [1, 1, 0]},
            {"bufferView": 1, "componentType": 5126, "count": 2, "type": "SCALAR", "min": [0], "max": [1]},
            {"bufferView": 2, "componentType": 5126, "count": 2, "type": "VEC3"},
        ],
        "bufferViews": [
            {"buffer": 0, "byteOffset": 0, "byteLength": 36},
            {"buffer": 0, "byteOffset": 36, "byteLength": 8},
            {"buffer": 0, "byteOffset": 44, "byteLength": 24},
        ],
        "buffers": [{"byteLength": len(data)}],
    }
    js = json.dumps(gltf).encode()
    js += b" " * (-len(js) % 4)
    total = 12 + 8 + len(js) + 8 + len(data)
    blob = struct.pack("<III", 0x46546C67, 2, total)
    blob += struct.pack("<II", len(js), 0x4E4F534A) + js
    blob += struct.pack("<II", len(data), 0x004E4942) + data
    with open(path, "wb") as f:
        f.write(blob)