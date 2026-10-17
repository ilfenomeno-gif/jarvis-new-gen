"""Generates a 3D model from text (Tripo3D) and shows it as a hologram in the viewer.

Consumes Tripo credits and writes one .glb into assets/viewer3d/models/.
"""
from core import model_gen


def generate_3d_model(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    try:
        prompt = model_gen.clean_prompt(params.get("prompt"))
    except ValueError as exc:
        return f"Invalid request: {exc}"
    if not model_gen.tripo_available():
        return model_gen.SDK_MISSING_MESSAGE
    key = model_gen.tripo_key()
    if not key:
        return model_gen.KEY_MISSING_MESSAGE
    try:
        path = model_gen.generate_model(prompt, key)
    except RuntimeError as exc:
        return f"3D generation failed: {exc}"
    if player is not None and hasattr(player, "viewer3d_call") and params.get("show", True) is not False:
        player.viewer3d_call("loadModel", [path.name])
        return f"Model '{path.name}' generated and shown as a hologram."
    return f"Model '{path.name}' generated and saved."


TOOL = {
    "name": "generate_3d_model",
    "description": (
        "Creates a 3D model from a text description (Tripo3D, takes up to a minute and "
        "uses API credits) and shows it as a hologram in the central display. Use when "
        "the user asks to create, build or show something in 3D, e.g. 'make a hologram "
        "of a jet engine'. Afterwards viewer_3d can explode_model, highlight_part or "
        "clear_model."
    ),
    "risk_class": "write",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "prompt": {"type": "STRING", "description": "What to create, max 300 characters."},
            "show": {"type": "BOOLEAN", "description": "Show it right away (default true)."},
        },
        "required": ["prompt"],
    },
    "handler": generate_3d_model,
}
