"""@file
@brief The writing session: holds the text and decides when it is deleted.
"""

from disappearing_text.constants import IDLE_TIMEOUT_SECONDS


class WritingSession:
    """@brief The text being written and the idle timeout that deletes it.

    Time is passed in as seconds, so the session needs no clock.
    """

    def __init__(self) -> None:
        """@brief Start a session with empty text that has not expired."""
        self._text: str = ""
        self._last_typed_at: float = 0.0
        self._expired: bool = False

    @property
    def text(self) -> str:
        """@brief The text the writer has now."""
        return self._text

    @property
    def has_expired(self) -> bool:
        """@brief True when the text was deleted and the writer has not typed since."""
        return self._expired

    def type_text(self, text: str, now: float) -> None:
        """@brief Replace the whole text and restart the countdown.

        @param text The whole text as the writer has it now; may be empty.
        @param now The current moment in seconds.
        @raises TypeError When text is not a str; the session is left unchanged.
        """
        if not isinstance(text, str):
            raise TypeError(f"text must be str, not {type(text).__name__}")
        self._text = text
        self._last_typed_at = now
        self._expired = False

    def check_timeout(self, now: float) -> bool:
        """@brief Delete the text when more than the idle timeout has passed.

        @param now The current moment in seconds.
        @return True when the text was deleted by this call, otherwise False.
        """
        if not self._text or self._seconds_idle(now) <= IDLE_TIMEOUT_SECONDS:
            return False
        self._text = ""
        self._expired = True
        return True

    def seconds_left(self, now: float) -> float | None:
        """@brief Seconds until the text is deleted.

        @param now The current moment in seconds.
        @return The seconds left, never below zero, or None when the text is empty.
        """
        if not self._text:
            return None
        return max(0.0, IDLE_TIMEOUT_SECONDS - self._seconds_idle(now))

    def _seconds_idle(self, now: float) -> float:
        """@brief Seconds since the writer last typed."""
        return now - self._last_typed_at
