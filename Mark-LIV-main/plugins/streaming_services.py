"""Open streaming services in the user's authenticated browser profile."""

from __future__ import annotations

from urllib.parse import urlencode

from actions.browser_control import browser_control

_SERVICES = {
    "netflix": {
        "home": "https://www.netflix.com/",
        "search": "https://www.netflix.com/search",
    },
    "prime_video": {
        "home": "https://www.primevideo.com/",
        "search": "https://www.primevideo.com/search/ref=atv_nb_sr",
    },
}
_JUSTWATCH_SEARCH = "https://www.justwatch.com/it/cerca"

PLUGIN = {
    "name": "streaming_services",
    "description": (
        "Opens Netflix or Prime Video in the user's normal browser, preserving "
        "its existing signed-in account/session; never asks for or stores "
        "credentials. Can search for or open a title. The availability action "
        "opens JustWatch Italy results so the user can distinguish titles "
        "included with a subscription from rent/buy offers. It never purchases "
        "or rents content."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "service": {
                "type": "STRING",
                "description": "Streaming service to open.",
                "enum": ["netflix", "prime_video"],
            },
            "action": {
                "type": "STRING",
                "description": (
                    "open the service, search/play a title, or availability "
                    "(open JustWatch Italy to check subscription versus paid offers)."
                ),
                "enum": ["open", "search", "play", "availability"],
            },
            "query": {
                "type": "STRING",
                "description": "Film or series title for search, play, or availability.",
            },
            "browser": {
                "type": "STRING",
                "description": "Optional browser; otherwise use the default browser and its existing account session.",
                "enum": ["chrome", "edge", "firefox", "opera", "operagx", "brave", "vivaldi"],
            },
        },
        "required": ["service", "action"],
    },
}


def _target_url(service: str, action: str, query: str = "") -> str:
    service_key = service.strip().casefold().replace("-", "_").replace(" ", "_")
    action_key = action.strip().casefold()
    if service_key not in _SERVICES:
        raise ValueError("Service must be netflix or prime_video.")
    if action_key not in {"open", "search", "play", "availability"}:
        raise ValueError("Action must be open, search, play, or availability.")
    if action_key == "open":
        return _SERVICES[service_key]["home"]
    if not query.strip():
        raise ValueError("A title is required for search, play, and availability.")
    if action_key == "availability":
        return f"{_JUSTWATCH_SEARCH}?{urlencode({'q': query.strip()})}"
    params = {"q": query.strip()} if service_key == "netflix" else {
        "phrase": query.strip()
    }
    return f"{_SERVICES[service_key]['search']}?{urlencode(params)}"


def run(parameters: dict, player=None) -> str:
    service = str(parameters.get("service", ""))
    action = str(parameters.get("action", ""))
    query = str(parameters.get("query", ""))
    url = _target_url(service, action, query)
    browser = parameters.get("browser")
    result = browser_control(
        parameters={
            "action": "go_to",
            "url": url,
            **({"browser": browser} if browser else {}),
        },
        player=player,
    )
    if not result.startswith("Opened"):
        return result
    if action.casefold() == "availability":
        return (
            f"{result} Controlla su JustWatch le offerte indicate come incluse "
            "nell'abbonamento Netflix o Prime Video; le opzioni noleggio/acquisto "
            "sono a pagamento extra. La disponibilità dipende dal paese e dal catalogo aggiornato."
        )
    return result
