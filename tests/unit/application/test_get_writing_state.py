"""@file
@brief Tests of the GetWritingState use case.
"""

from disappearing_text.application.dto.writing_state import WritingState
from disappearing_text.application.use_cases.get_writing_state import GetWritingState
from disappearing_text.application.use_cases.type_text import TypeText
from disappearing_text.domain.writing_session import WritingSession


class FakeClock:
    """@brief A clock whose moment the test sets."""

    def __init__(self, moment: float = 0.0) -> None:
        """@param moment The first moment."""
        self.moment = moment

    def now(self) -> float:
        """@brief The moment set by the test."""
        return self.moment


def _setup() -> tuple[FakeClock, TypeText, GetWritingState]:
    """@brief A clock and both use cases sharing one session."""
    clock = FakeClock(100.0)
    session = WritingSession()
    return clock, TypeText(session, clock), GetWritingState(session, clock)


def test_execute_returns_empty_state_for_new_session() -> None:
    """@brief Nothing typed gives no countdown and no warning."""
    _, _, get_state = _setup()
    assert get_state.execute() == WritingState("", None, False, False)


def test_execute_returns_text_and_seconds_left() -> None:
    """@brief Typed text is returned with the seconds left."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 101.0
    assert get_state.execute() == WritingState("hello", 4.0, False, False)


def test_execute_warns_when_three_seconds_have_passed() -> None:
    """@brief Two seconds left is the warning threshold, inclusive."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 103.0
    state = get_state.execute()
    assert state.seconds_left == 2.0
    assert state.is_warning is True


def test_execute_does_not_warn_just_above_threshold() -> None:
    """@brief Boundary: just above two seconds left is no warning."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 102.999
    assert get_state.execute().is_warning is False


def test_execute_keeps_text_at_exactly_five_seconds() -> None:
    """@brief Boundary: exactly five seconds keeps the text, with a warning."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 105.0
    assert get_state.execute() == WritingState("hello", 0.0, True, False)


def test_execute_clears_text_after_more_than_five_seconds() -> None:
    """@brief Boundary: just over five seconds deletes the text."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 105.001
    assert get_state.execute() == WritingState("", None, False, True)


def test_execute_keeps_reporting_cleared_until_typing_again() -> None:
    """@brief The cleared flag survives later reads and ends on typing."""
    clock, type_text, get_state = _setup()
    type_text.execute("hello")
    clock.moment = 110.0
    get_state.execute()
    clock.moment = 111.0
    assert get_state.execute().was_cleared is True
    type_text.execute("new")
    assert get_state.execute().was_cleared is False


def test_execute_gives_no_warning_for_empty_text() -> None:
    """@brief Empty text means the countdown is stopped."""
    clock, type_text, get_state = _setup()
    type_text.execute("")
    clock.moment = 104.0
    assert get_state.execute() == WritingState("", None, False, False)
