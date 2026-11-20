"""@file
@brief The system implementation of the clock port.
"""

import time


class SystemClock:
    """@brief Clock backed by the monotonic system clock."""

    def now(self) -> float:
        """@brief The current moment in seconds; never goes back."""
        return time.monotonic()
