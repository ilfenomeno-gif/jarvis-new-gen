"""Generates a 3D model from text and shows it as a hologram in the viewer.

Backend: local GPU (core/local_3d_gen.py) or Tripo3D (consumes credits), chosen by
model_gen.backend(). Writes one .glb into assets/viewer3d/models/.
"""
from core import model_gen


def generate_3d_model(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    try:
        prompt = model_gen.clean_prompt(params.get("prompt"))
    except ValueError as exc:
        return f"Invalid request: {exc}"
    from core import local_3d_gen
    choice = model_gen.backend()
    key = model_gen.tripo_key() if model_gen.tripo_available() else ""
    use_local = choice == "local" or (choice == "auto" and not key and local_3d_gen.is_installed())
    try:
        if use_local:
            path = local_3d_gen.generate_local(prompt)
        elif choice == "tripo" or key:
            if not model_gen.tripo_available():
                return model_gen.SDK_MISSING_MESSAGE
            if not key:
                return model_gen.KEY_MISSING_MESSAGE
            path = model_gen.generate_model(prompt, key)
        else:
            return (model_gen.KEY_MISSING_MESSAGE + " Or install the free local generator: "
                    + local_3d_gen.SETUP_MESSAGE)
    except RuntimeError as exc:
        return f"3D generation failed: {exc}"
    if player is not None and hasattr(player, "viewer3d_call") and params.get("show", True) is not False:
        player.viewer3d_call("loadModel", [path.name])
        return f"Model '{path.name}' generated and shown as a hologram."
    return f"Model '{path.name}' generated and saved."


TOOL = {
    "name": "generate_3d_model",
    "description": (
        "Creates a 3D model from a text description (free local GPU generator, or Tripo3D "
        "with API credits; takes up to a few minutes) and shows it as a hologram in the central display. Use when "
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
