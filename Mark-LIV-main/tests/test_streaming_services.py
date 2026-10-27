"""Tests for streaming navigation through the user's browser profile."""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plugins import streaming_services


@pytest.mark.parametrize(
    ("service", "expected_host", "expected_path", "query_key"),
    [
        ("netflix", "www.netflix.com", "/search", "q"),
        (
            "prime_video",
            "www.primevideo.com",
            "/search/ref=atv_nb_sr",
            "phrase",
        ),
    ],
)
def test_search_url_encodes_title(service, expected_host, expected_path, query_key):
    url = streaming_services._target_url(service, "search", "Dune & Friends")
    parsed = urlsplit(url)
    assert parsed.scheme == "https"
    assert parsed.netloc == expected_host
    assert parsed.path == expected_path
    assert parse_qs(parsed.query) == {query_key: ["Dune & Friends"]}


def test_open_uses_fixed_service_homepage():
    assert streaming_services._target_url("netflix", "open") == "https://www.netflix.com/"
    assert streaming_services._target_url("prime_video", "open") == "https://www.primevideo.com/"


def test_availability_search_uses_italian_justwatch_results():
    url = streaming_services._target_url("netflix", "availability", "Dune & Friends")
    parsed = urlsplit(url)
    assert parsed.netloc == "www.justwatch.com"
    assert parsed.path == "/it/cerca"
    assert parse_qs(parsed.query) == {"q": ["Dune & Friends"]}


@pytest.mark.parametrize(
    ("service", "action", "query"),
    [
        ("unknown", "open", ""),
        ("netflix", "watch", ""),
        ("netflix", "search", ""),
        ("prime_video", "availability", ""),
    ],
)
def test_invalid_service_or_missing_query_is_rejected(service, action, query):
    with pytest.raises(ValueError):
        streaming_services._target_url(service, action, query)


@pytest.mark.parametrize(
    ("service", "action", "query", "expected_url"),
    [
        ("netflix", "open", "", "https://www.netflix.com/"),
        (
            "prime_video",
            "play",
            "Dune",
            "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=Dune",
        ),
    ],
)
def test_streaming_uses_native_browser_without_webview_or_credential_prompt(
    monkeypatch, service, action, query, expected_url
):
    calls = []

    def fake_browser_control(parameters, player=None):
        calls.append(parameters)
        return f"Opened in your default browser: {parameters['url']}"

    monkeypatch.setattr(streaming_services, "browser_control", fake_browser_control)
    player = type(
        "Player",
        (),
        {
            "open_url_in_webview": lambda *_args: pytest.fail(
                "the embedded view does not reuse the authenticated browser profile"
            ),
            "confirm_streaming_play_in_chrome": lambda *_args: pytest.fail(
                "opening a search page must not ask for credentials or playback confirmation"
            ),
        },
    )()

    result = streaming_services.run(
        {"service": service, "action": action, "query": query},
        player=player,
    )
    assert calls == [{"action": "go_to", "url": expected_url}]
    assert result.startswith("Opened in your default browser")


def test_availability_opens_justwatch_and_explains_subscription_vs_paid(monkeypatch):
    calls = []
    monkeypatch.setattr(
        streaming_services,
        "browser_control",
        lambda parameters, player=None: (
            calls.append(parameters) or "Opened in your default browser"
        ),
    )

    result = streaming_services.run(
        {"service": "netflix", "action": "availability", "query": "Dune"},
    )
    assert calls == [
        {
            "action": "go_to",
            "url": "https://www.justwatch.com/it/cerca?q=Dune",
        }
    ]
    assert "incluse nell'abbonamento" in result
    assert "noleggio/acquisto" in result


def test_browser_failure_is_returned_without_claiming_opened(monkeypatch):
    monkeypatch.setattr(
        streaming_services,
        "browser_control",
        lambda **_kwargs: "Could not open a browser",
    )
    result = streaming_services.run(
        {"service": "netflix", "action": "open"},
    )
    assert result == "Could not open a browser"
