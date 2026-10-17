"""Drives the 3D globe in the central display. UI only: no data is read or written."""
from core.viewer3d import build_call

_MODES = ("show", "hide", "fly_to", "add_marker", "clear_markers", "spin")


def viewer_3d(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    mode = str(params.get("mode", "")).strip().lower()
    if mode not in _MODES:
        return f"Unknown mode '{mode}'. Use one of: {', '.join(_MODES)}."
    if player is None or not hasattr(player, "viewer3d_call"):
        return "The interface is not available."
    try:
        if mode in ("show", "hide"):
            player.viewer3d_show(mode == "show")
            return "3D viewer shown." if mode == "show" else "3D viewer hidden."
        if mode == "fly_to":
            player.viewer3d_call("flyTo", [params.get("lat"), params.get("lon")])
            return f"Globe turning to {params.get('lat')}, {params.get('lon')}."
        if mode == "add_marker":
            player.viewer3d_call(
                "addMarker",
                [params.get("lat"), params.get("lon"), params.get("label", "")],
            )
            return "Marker added."
        if mode == "clear_markers":
            player.viewer3d_call("clearMarkers", [])
            return "Markers cleared."
        spin = params.get("spin", True)
        player.viewer3d_call("spin", [spin])
        return "Globe spinning." if spin else "Globe still."
    except ValueError as exc:
        return f"Invalid request: {exc}"


TOOL = {
    "name": "viewer_3d",
    "description": (
        "Controls the holographic 3D globe in the central display. mode=show or "
        "hide switches to or from it; fly_to turns the globe to lat/lon; "
        "add_marker puts a labelled marker at lat/lon; clear_markers removes "
        "them; spin starts or stops the rotation."
    ),
    "risk_class": "read",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "mode": {"type": "STRING", "description": ", ".join(_MODES)},
            "lat": {"type": "NUMBER", "description": "Latitude, -90 to 90."},
            "lon": {"type": "NUMBER", "description": "Longitude, -180 to 180."},
            "label": {"type": "STRING", "description": "Marker label."},
            "spin": {"type": "BOOLEAN", "description": "For mode=spin."},
        },
        "required": ["mode"],
    },
    "handler": viewer_3d,
}
