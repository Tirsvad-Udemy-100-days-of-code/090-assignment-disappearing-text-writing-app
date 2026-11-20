"""@file
@brief Tests of the constants of the writing app.
"""

from disappearing_text import constants


def test_idle_timeout_is_five_seconds() -> None:
    """@brief The assignment asks for five seconds of idle time."""
    assert constants.IDLE_TIMEOUT_SECONDS == 5


def test_warning_comes_before_the_timeout() -> None:
    """@brief The warning threshold lies inside the idle timeout."""
    assert 0 < constants.WARNING_THRESHOLD_SECONDS < constants.IDLE_TIMEOUT_SECONDS
