"""Validation for commands sent to the 3D viewer. No Qt imports.

The page executes only functions in ALLOWED, with arguments passed as JSON
(never interpolated into script text).
"""
from __future__ import annotations

import json

ALLOWED = {
    "flyTo": 2,
    "addMarker": 3,
    "clearMarkers": 0,
    "spin": 1,
}


def _coord(value, low: float, high: float, name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a number")
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a number") from None
    if not low <= number <= high:
        raise ValueError(f"{name} must be between {low:g} and {high:g}")
    return number


def build_call(function: str, args: list) -> tuple[str, str]:
    """Return (function, args_json) or raise ValueError."""
    if function not in ALLOWED:
        raise ValueError(f"Unknown viewer function '{function}'.")
    if len(args) != ALLOWED[function]:
        raise ValueError(f"{function} takes {ALLOWED[function]} argument(s).")
    if function in ("flyTo", "addMarker"):
        clean = [_coord(args[0], -90, 90, "lat"), _coord(args[1], -180, 180, "lon")]
        if function == "addMarker":
            clean.append(str(args[2])[:60])
    elif function == "spin":
        if not isinstance(args[0], bool):
            raise ValueError("spin takes true or false")
        clean = [args[0]]
    else:
        clean = []
    return function, json.dumps(clean)
