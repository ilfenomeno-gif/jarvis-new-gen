"""Drives the 3D globe in the central display. UI only: no data is read or written."""
from core.viewer3d import build_call, fetch_flights
import json

_MODES = (
    "show", "hide", "fly_to", "add_marker", "clear_markers", "spin",
    "load_live_flights", "clear_flights", "load_model", "clear_model",
    "explode_model", "highlight_part", "set_hologram",
    "set_material_style", "set_part_info", "list_parts", "list_models", "hovered_part",
    "set_controls",
)


def _part_info(raw) -> dict:
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except ValueError:
            raise ValueError("part_info must be a JSON object such as {\"fan\": \"cools the card\"}") from None
    if not isinstance(raw, dict) or not raw:
        raise ValueError("part_info must be a non-empty object of part name -> description")
    return raw


def viewer_3d(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    mode = str(params.get("mode", "")).strip().lower()
    if mode not in _MODES:
        return f"Unknown mode '{mode}'. Use one of: {', '.join(_MODES)}."
    if player is None or not hasattr(player, "viewer3d_call"):
        return "The interface is not available."
    try:
        if mode == "set_material_style":
            style = str(params.get("style") or "").strip().lower()
            player.viewer3d_call("setMaterialStyle", [style])
            return f"Material style set to {style}. It applies to the loaded 3D model, or to the next one loaded (the globe has no material styles)."
        if mode == "set_controls":
            on = bool(params.get("on", True))
            player.viewer3d_call("setControls", [on])
            return "Mouse controls on (drag rotates, wheel zooms, right button pans)." if on else "Mouse controls off."
        if mode == "list_models":
            from core.viewer3d import list_models
            found = list_models()
            if not (found["generated"] or found["cad"]):
                return "No models available. CAD models: run 'python -m core.registry_cli download-cad-models'."
            return (
                "CAD (multi-part, use these to explain/disassemble): " + (", ".join(found["cad"]) or "none downloaded yet")
                + ". Generated (single-part): " + (", ".join(found["generated"]) or "none") + "."
            )
        if mode == "hovered_part":
            if not hasattr(player, "viewer3d_hover"):
                return "Hover information is not available."
            hover = player.viewer3d_hover()
            if not hover.get("name"):
                return "The mouse is not over any part of the 3D model right now."
            text = f" - {hover['text']}" if hover.get("text") else " (no description set for this part)"
            return f"The user is looking at: {hover['name']}{text}"
        if mode == "set_part_info":
            info = _part_info(params.get("part_info"))
            player.viewer3d_call("setPartInfo", [info])
            return f"{len(info)} part description(s) set: hover a part to read it."
        if mode == "list_parts":
            from core.viewer3d import model_file, part_names
            names = part_names(model_file(params.get("model")))
            return "Parts: " + ", ".join(names) if names else "Parts have no names: the viewer labels them 'Parte 1', 'Parte 2', ... by position."
        if mode == "set_hologram":
            on = params.get("on", True)
            player.viewer3d_call("setHologram", [bool(on)])
            return "Hologram effect on." if on else "Hologram effect off (plain materials)."
        if mode == "explode_model":
            on = params.get("on", True)
            player.viewer3d_call("explodeModel", [bool(on)])
            return "Model exploded." if on else "Model reassembled."
        if mode == "highlight_part":
            part = str(params.get("part") or "")
            player.viewer3d_call("highlightPart", [part])
            return f"Part '{part}' highlighted." if part else "Highlight removed."
        if mode == "load_model":
            from core.viewer3d import model_file
            name = model_file(params.get("model")) and str(params.get("model")).strip()
            player.viewer3d_call("loadModel", [name])
            return f"Model {name} loaded in the hologram."
        if mode == "clear_model":
            player.viewer3d_call("clearModel", [])
            return "Model removed, globe restored."
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
        "on the hologram'. load_model shows a .glb/.gltf already saved in the models "
        "folder (model=file name) in place of the globe; clear_model restores the globe. "
        "explode_model (on=true/false) spreads the loaded model's parts apart and "
        "back; highlight_part makes the named part glow (empty part clears it); "
        "set_hologram (on=true/false) toggles the projection look (on by default). "
        "set_material_style (style=hologram, blueprint or realistic) changes how the "
        "loaded model is drawn: blueprint = solid blue with glowing CAD edges, "
        "realistic = PBR look (the model's own materials with studio HDRI reflections "
        "and soft shadows); use it for 'show it in blueprint mode'. "
        "Teaching flow ('smonta il PC e spiegami i componenti'): load_model "
        "model=cad/pc.glb, then explode_model, then speak about each part while calling "
        "highlight_part (cpu, ram_1, gpu, ...) so it glows. "
        "list_parts (model=file name) returns the part names; set_part_info "
        "(part_info = JSON text like {\"fan\": \"cools the card\"}) attaches descriptions "
        "to parts: the user then sees a tooltip with the name and description when "
        "the mouse is over that part. hovered_part returns the part under the mouse "
        "right now: use it for 'what is this?' / 'what am I looking at?'. list_models "
        "lists loadable models: for 'explain an engine' / 'take a PC apart' prefer a "
        "multi-part cad/<name>.glb over generating one (generated models are single-part "
        "and cannot be exploded); model may be 'cad/<name>.glb'. set_controls (on=true/false) "
        "enables or disables the mouse controls on a loaded model (drag to rotate, wheel to "
        "zoom, right button to pan); they are on by default. The model 'cad/pc.glb' (a "
        "multi-part PC: case, motherboard, cpu, cpu_cooler, ram_1, ram_2, gpu, psu, fan) "
        "always exists: for 'explain/take apart a PC' call load_model with model=cad/pc.glb, "
        "then explode_model; never say it is missing."
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
            "model": {"type": "STRING", "description": "For load_model: file name such as sword.glb."},
            "on": {"type": "BOOLEAN", "description": "For explode_model: true explodes, false reassembles."},
            "part": {"type": "STRING", "description": "For highlight_part: node name."},
            "style": {"type": "STRING", "description": "For set_material_style: hologram, blueprint, realistic."},
            "part_info": {"type": "STRING", "description": "For set_part_info: JSON object text, part name -> description."},
        },
        "required": ["mode"],
    },
    "handler": viewer_3d,
}
