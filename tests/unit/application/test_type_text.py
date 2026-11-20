"""@file
@brief Tests of the TypeText use case.
"""

import pytest

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


def test_execute_stores_text_in_the_session() -> None:
    """@brief The text reaches the session."""
    session = WritingSession()
    TypeText(session, FakeClock()).execute("hello")
    assert session.text == "hello"


def test_execute_uses_the_moment_of_the_clock() -> None:
    """@brief The countdown starts at the clock's moment."""
    clock = FakeClock(50.0)
    session = WritingSession()
    TypeText(session, clock).execute("hello")
    assert session.seconds_left(52.0) == 3.0


def test_execute_clears_expired_flag() -> None:
    """@brief Typing after a deletion clears the flag."""
    clock = FakeClock(0.0)
    session = WritingSession()
    use_case = TypeText(session, clock)
    use_case.execute("a")
    session.check_timeout(10.0)
    use_case.execute("b")
    assert session.has_expired is False


def test_execute_raises_type_error_for_non_str() -> None:
    """@brief A non-str is rejected."""
    with pytest.raises(TypeError):
        TypeText(WritingSession(), FakeClock()).execute(5)  # type: ignore[arg-type]
