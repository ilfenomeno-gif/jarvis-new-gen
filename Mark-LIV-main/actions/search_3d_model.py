"""Finds a ready-made .glb model on the web and shows it in the viewer (realistic).

Preferred over generate_3d_model for complex or mechanical objects (cars, engines,
weapons, buildings, famous characters), where the AI generators deform the mesh.
"""
from core import model_search


def search_3d_model(parameters: dict, player=None, **_ignored) -> str:
    query = str((parameters or {}).get("query") or "").strip()
    if not query:
        return "Invalid request: query is empty."
    if len(query) > 120:
        return "Invalid request: query is too long (max 120 characters)."
    result = model_search.search_and_download(query)
    if not result["ok"]:
        return (f"No exact ready-made 3D model found for '{query}' ({result['reason']}). "
                "Do NOT ask the user: switch to the generative fallback now. Call web_search with "
                "mode='images' for a clear photo of the object, then generate_3d_model with "
                "image_url=<first direct link> (local Stable Fast 3D). Tell the user, e.g. "
                "\"Non ho trovato un modello esatto, quindi lo genero da un'immagine\".")
    path = result["path"]
    credit = f"'{result['name']}' by {result['author']} ({result['license']}), saved as downloads/{path.name}."
    if player is not None and hasattr(player, "viewer3d_call") and (parameters or {}).get("show", True) is not False:
        player.viewer3d_call("setMaterialStyle", ["realistic"])
        player.viewer3d_call("loadModel", [f"downloads/{path.name}"])
        shown = "Loaded in realistic style. Drag with the mouse to rotate. "
    else:
        shown = ""
    return f"Found 3D model {credit} {shown}{result['note']}".strip()


TOOL = {
    "name": "search_3d_model",
    "description": (
        "Searches the web for a ready-made .glb 3D model (Sketchfab with a token, else a curated library), "
        "downloads it and shows it in realistic style. Use it FIRST for any specific object (car model, engine, "
        "weapon, building, famous character): real models have perfect curves and textures. "
        "If it finds nothing (or only a generic sample, or no token), do not ask the user: use web_search "
        "mode='images' to find a photo, then generate_3d_model with image_url. For simple or organic objects "
        "(apple, chair, dragon) use generate_3d_model directly. Always mention the author and license from the result."
    ),
    "risk_class": "write",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "query": {"type": "STRING", "description": "What to search, e.g. 'ferrari car'. Max 120 characters."},
            "show": {"type": "BOOLEAN", "description": "Show it right away (default true)."},
        },
        "required": ["query"],
    },
    "handler": search_3d_model,
}
