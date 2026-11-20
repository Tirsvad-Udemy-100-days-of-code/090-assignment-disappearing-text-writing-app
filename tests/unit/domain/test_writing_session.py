"""@file
@brief Tests of the writing session rules.
"""

import pytest

from disappearing_text.domain.writing_session import WritingSession


def _typed(text: str = "hello", at: float = 100.0) -> WritingSession:
    """@brief A session where text was typed at the given moment."""
    session = WritingSession()
    session.type_text(text, at)
    return session


def test_new_session_is_empty_and_not_expired() -> None:
    """@brief A new session has no text and has not expired."""
    session = WritingSession()
    assert session.text == ""
    assert session.has_expired is False
    assert session.seconds_left(0.0) is None


def test_type_text_stores_the_whole_text() -> None:
    """@brief Typing replaces the text."""
    session = _typed("hello")
    session.type_text("hello world", 101.0)
    assert session.text == "hello world"


def test_check_timeout_keeps_text_when_exactly_five_seconds_passed() -> None:
    """@brief Boundary: exactly the idle timeout does not delete."""
    session = _typed(at=100.0)
    assert session.check_timeout(105.0) is False
    assert session.text == "hello"
    assert session.has_expired is False


def test_check_timeout_clears_text_when_just_over_five_seconds_passed() -> None:
    """@brief Boundary: more than the idle timeout deletes the text."""
    session = _typed(at=100.0)
    assert session.check_timeout(105.001) is True
    assert session.text == ""
    assert session.has_expired is True


def test_check_timeout_keeps_text_when_just_under_five_seconds_passed() -> None:
    """@brief Boundary: just below the idle timeout keeps the text."""
    session = _typed(at=100.0)
    assert session.check_timeout(104.999) is False
    assert session.text == "hello"


def test_check_timeout_returns_false_on_second_call_after_clearing() -> None:
    """@brief Only the call that deletes the text returns True."""
    session = _typed(at=100.0)
    session.check_timeout(110.0)
    assert session.check_timeout(120.0) is False
    assert session.has_expired is True


def test_check_timeout_does_nothing_when_text_is_empty() -> None:
    """@brief Without text there is no countdown and nothing expires."""
    session = _typed("", at=100.0)
    assert session.check_timeout(200.0) is False
    assert session.has_expired is False


def test_type_text_restarts_the_countdown() -> None:
    """@brief Typing again moves the deadline."""
    session = _typed(at=100.0)
    session.type_text("hello!", 104.0)
    assert session.check_timeout(108.0) is False
    assert session.text == "hello!"
    assert session.check_timeout(109.001) is True


def test_type_text_clears_the_expired_flag() -> None:
    """@brief The expired flag stays until the writer types again."""
    session = _typed(at=100.0)
    session.check_timeout(110.0)
    assert session.has_expired is True
    session.type_text("again", 111.0)
    assert session.has_expired is False
    assert session.text == "again"


def test_expired_flag_stays_while_nothing_is_typed() -> None:
    """@brief Repeated checks do not reset the expired flag."""
    session = _typed(at=100.0)
    session.check_timeout(110.0)
    session.check_timeout(111.0)
    assert session.has_expired is True


def test_empty_text_stops_the_countdown() -> None:
    """@brief Typing the empty text gives no seconds left."""
    session = _typed(at=100.0)
    session.type_text("", 101.0)
    assert session.seconds_left(102.0) is None


@pytest.mark.parametrize(
    ("now", "expected"),
    [(100.0, 5.0), (102.0, 3.0), (105.0, 0.0), (107.0, 0.0)],
)
def test_seconds_left_counts_down_and_never_goes_below_zero(
    now: float, expected: float
) -> None:
    """@brief Seconds left is the timeout minus idle time, at least zero."""
    assert _typed(at=100.0).seconds_left(now) == expected


@pytest.mark.parametrize("value", [None, 5, b"x", ["a"]])
def test_type_text_raises_type_error_for_non_str(value: object) -> None:
    """@brief A non-str is rejected."""
    session = WritingSession()
    with pytest.raises(TypeError):
        session.type_text(value, 1.0)  # type: ignore[arg-type]


def test_type_text_keeps_state_when_it_raises() -> None:
    """@brief A rejected call changes nothing."""
    session = _typed("keep", at=100.0)
    with pytest.raises(TypeError):
        session.type_text(1, 103.0)  # type: ignore[arg-type]
    assert session.text == "keep"
    assert session.seconds_left(100.0) == 5.0
