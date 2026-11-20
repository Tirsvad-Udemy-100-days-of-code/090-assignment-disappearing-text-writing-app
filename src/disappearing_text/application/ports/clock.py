"""@file
@brief Port for the current moment.
"""

from typing import Protocol


class Clock(Protocol):
    """@brief Tells the current moment in seconds."""

    def now(self) -> float:
        """@brief The current moment in seconds, from a clock that never goes back."""
        ...
