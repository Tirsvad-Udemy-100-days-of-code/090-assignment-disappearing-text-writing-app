"""@file
@brief View model of the writing page.
"""

from dataclasses import dataclass

from disappearing_text.constants import (
    IDLE_TIMEOUT_SECONDS,
    POLL_INTERVAL_MILLISECONDS,
    WARNING_THRESHOLD_SECONDS,
)

## Title of the single screen, as in the wireframe.
PAGE_TITLE: str = "Write without stopping"


@dataclass(frozen=True, slots=True)
class WritingViewModel:
    """@brief What the page needs besides the writing state."""

    title: str
    idle_timeout_seconds: int
    warning_threshold_seconds: int
    poll_interval_milliseconds: int

    @classmethod
    def from_constants(cls) -> "WritingViewModel":
        """@brief Build the view model from the title and the constants.

        @return The view model for the writing page.
        """
        return cls(
            title=PAGE_TITLE,
            idle_timeout_seconds=IDLE_TIMEOUT_SECONDS,
            warning_threshold_seconds=WARNING_THRESHOLD_SECONDS,
            poll_interval_milliseconds=POLL_INTERVAL_MILLISECONDS,
        )
