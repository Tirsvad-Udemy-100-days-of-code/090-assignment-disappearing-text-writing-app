"""@file
@brief Use case: read the state of the writing session.
"""

from disappearing_text.application.dto.writing_state import WritingState
from disappearing_text.application.ports.clock import Clock
from disappearing_text.constants import WARNING_THRESHOLD_SECONDS
from disappearing_text.domain.writing_session import WritingSession


class GetWritingState:
    """@brief Checks the idle timeout and describes the session."""

    def __init__(self, session: WritingSession, clock: Clock) -> None:
        """@brief Create the use case.

        @param session The one writing session.
        @param clock The source of the current moment.
        """
        self._session = session
        self._clock = clock

    def execute(self) -> WritingState:
        """@brief Delete the text if it timed out, then return the state.

        @return The state of the writing session after the check.
        """
        now = self._clock.now()
        self._session.check_timeout(now)
        seconds_left = self._session.seconds_left(now)
        is_warning = (
            seconds_left is not None and seconds_left <= WARNING_THRESHOLD_SECONDS
        )
        return WritingState(
            text=self._session.text,
            seconds_left=seconds_left,
            is_warning=is_warning,
            was_cleared=self._session.has_expired,
        )
