"""@file
@brief Tests of the system clock adapter.
"""

from disappearing_text.infrastructure.system_clock import SystemClock


def test_now_returns_a_float() -> None:
    """@brief The moment is a number of seconds."""
    assert isinstance(SystemClock().now(), float)


def test_now_never_goes_back() -> None:
    """@brief A later call is not earlier than a previous one."""
    clock = SystemClock()
    first = clock.now()
    assert clock.now() >= first
