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
    "setFlights": 1,
    "clearFlights": 0,
}

MAX_FLIGHTS = 400
REGIONS = {
    "europe": (35.0, 72.0, -12.0, 40.0),
    "usa": (24.0, 50.0, -125.0, -66.0),
    "world": (-90.0, 90.0, -180.0, 180.0),
}
OPENSKY_URL = "https://opensky-network.org/api/states/all"


def parse_states(payload: dict, limit: int = MAX_FLIGHTS) -> list[list]:
    """OpenSky state vectors -> [[lat, lon, callsign, altitude_m], ...], airborne only."""
    flights = []
    for row in (payload or {}).get("states") or []:
        try:
            lon, lat, on_ground = row[5], row[6], row[8]
        except (IndexError, TypeError):
            continue
        if lat is None or lon is None or on_ground:
            continue
        altitude = row[7] if len(row) > 7 and row[7] is not None else 0
        flights.append([lat, lon, str(row[1] or "").strip()[:12], altitude])
    # Evenly thinned so a capped list still covers the whole region.
    if len(flights) > limit:
        step = len(flights) / limit
        flights = [flights[int(i * step)] for i in range(limit)]
    return flights


def fetch_flights(region: str = "europe", opener=None, timeout: float = 15.0) -> list[list]:
    """Blocking HTTP call: run it in a worker thread, never on the UI thread."""
    import urllib.request

    if region not in REGIONS:
        raise ValueError(f"Unknown region '{region}'. Use: {', '.join(REGIONS)}.")
    lamin, lamax, lomin, lomax = REGIONS[region]
    url = f"{OPENSKY_URL}?lamin={lamin}&lamax={lamax}&lomin={lomin}&lomax={lomax}"
    request = urllib.request.Request(url, headers={"User-Agent": "jarvis-viewer3d"})
    try:
        with (opener or urllib.request.urlopen)(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"OpenSky not reachable: {exc}") from None
    return parse_states(payload)


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
    elif function == "setFlights":
        if not isinstance(args[0], list) or any(
            not isinstance(f, (list, tuple)) or len(f) < 3 for f in args[0]
        ):
            raise ValueError("setFlights takes a list of [lat, lon, callsign]")
        clean = [[
            [_coord(f[0], -90, 90, "lat"), _coord(f[1], -180, 180, "lon"), str(f[2])[:12]]
            for f in args[0][:MAX_FLIGHTS]
        ]]
    elif function == "spin":
        if not isinstance(args[0], bool):
            raise ValueError("spin takes true or false")
        clean = [args[0]]
    else:
        clean = []
    return function, json.dumps(clean)
