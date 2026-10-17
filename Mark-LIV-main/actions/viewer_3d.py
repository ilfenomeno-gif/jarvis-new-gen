"""Drives the 3D globe in the central display. UI only: no data is read or written."""
from core.viewer3d import build_call, fetch_flights

_MODES = (
    "show", "hide", "fly_to", "add_marker", "clear_markers", "spin",
    "load_live_flights", "clear_flights",
)


def viewer_3d(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    mode = str(params.get("mode", "")).strip().lower()
    if mode not in _MODES:
        return f"Unknown mode '{mode}'. Use one of: {', '.join(_MODES)}."
    if player is None or not hasattr(player, "viewer3d_call"):
        return "The interface is not available."
    try:
        if mode == "load_live_flights":
            region = str(params.get("region") or "europe").strip().lower()
            # Tool threads may block; the UI thread is only reached via the signal.
            flights = fetch_flights(region)
            player.viewer3d_call("setFlights", [flights])
            return f"{len(flights)} live flights shown on the globe ({region})."
        if mode == "clear_flights":
            player.viewer3d_call("clearFlights", [])
            return "Flights cleared."
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
    except (ValueError, RuntimeError) as exc:
        return f"Invalid request: {exc}"


TOOL = {
    "name": "viewer_3d",
    "description": (
        "Controls the holographic 3D globe in the central display. mode=show or "
        "hide switches to or from it; fly_to turns the globe to lat/lon; "
        "add_marker puts a labelled marker at lat/lon; clear_markers removes "
        "them; spin starts or stops the rotation; load_live_flights fetches real-time "
        "flights (OpenSky) and plots them on the globe, region=europe, usa or world "
        "(default europe), and shows the globe; clear_flights removes them. Use "
        "load_live_flights for requests like 'show live flights' or 'track flights "
        "on the hologram'."
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
            "region": {"type": "STRING", "description": "For load_live_flights: europe, usa, world."},
        },
        "required": ["mode"],
    },
    "handler": viewer_3d,
}
