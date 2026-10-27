"""Voice I/O boundary for Gemini Live and headless tests."""
from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator, Mapping
from typing import Any


class VoiceTransport(ABC):
    @property
    @abstractmethod
    def connected(self) -> bool: ...

    @abstractmethod
    async def send_audio(self, media: Mapping[str, Any]) -> None: ...

    @abstractmethod
    async def send_content(
        self,
        *,
        turns: Any,
        turn_complete: bool = True,
    ) -> None: ...

    @abstractmethod
    async def send_tool_response(self, function_responses: Any) -> None: ...

    @abstractmethod
    def receive(self) -> AsyncIterator[Any]: ...

    @abstractmethod
    def close(self) -> None: ...


class GeminiLiveTransport(VoiceTransport):
    """Adapt a connected Gemini Live session to the voice transport contract.

    The surrounding ``async with`` owns the provider session; ``close`` only
    marks this adapter unavailable so it cannot outlive that context.
    """

    def __init__(self, session: Any) -> None:
        self._session = session
        self._connected = True

    @property
    def connected(self) -> bool:
        return self._connected

    def _require_connection(self) -> None:
        if not self._connected:
            raise RuntimeError("Gemini Live transport is closed.")

    async def send_audio(self, media: Mapping[str, Any]) -> None:
        self._require_connection()
        await self._session.send_realtime_input(media=dict(media))

    async def send_content(
        self,
        *,
        turns: Any,
        turn_complete: bool = True,
    ) -> None:
        self._require_connection()
        await self._session.send_client_content(
            turns=turns,
            turn_complete=turn_complete,
        )

    async def send_tool_response(self, function_responses: Any) -> None:
        self._require_connection()
        await self._session.send_tool_response(
            function_responses=function_responses,
        )

    async def receive(self) -> AsyncIterator[Any]:
        self._require_connection()
        async for event in self._session.receive():
            yield event

    def close(self) -> None:
        self._connected = False


class NullTransport(VoiceTransport):
    """In-memory transport for tests and headless runs."""

    def __init__(self) -> None:
        self._connected = True
        self.audio: list[dict[str, Any]] = []
        self.contents: list[tuple[Any, bool]] = []
        self.tool_responses: list[Any] = []
        self._events: list[Any] = []

    @property
    def connected(self) -> bool:
        return self._connected

    async def send_audio(self, media: Mapping[str, Any]) -> None:
        if not self._connected:
            raise RuntimeError("Null transport is closed.")
        self.audio.append(dict(media))

    async def send_content(
        self,
        *,
        turns: Any,
        turn_complete: bool = True,
    ) -> None:
        if not self._connected:
            raise RuntimeError("Null transport is closed.")
        self.contents.append((turns, turn_complete))

    async def send_tool_response(self, function_responses: Any) -> None:
        if not self._connected:
            raise RuntimeError("Null transport is closed.")
        self.tool_responses.append(function_responses)

    async def receive(self) -> AsyncIterator[Any]:
        if not self._connected:
            raise RuntimeError("Null transport is closed.")
        events, self._events = self._events, []
        for event in events:
            yield event

    def feed_event(self, event: Any) -> None:
        if not self._connected:
            raise RuntimeError("Null transport is closed.")
        self._events.append(event)

    def close(self) -> None:
        self._connected = False
