"""@file
@brief Use case: the writer changed the text.
"""

from disappearing_text.application.ports.clock import Clock
from disappearing_text.domain.writing_session import WritingSession


class TypeText:
    """@brief Passes the new text and the current moment to the session."""

    def __init__(self, session: WritingSession, clock: Clock) -> None:
        """@brief Create the use case.

        @param session The one writing session.
        @param clock The source of the current moment.
        """
        self._session = session
        self._clock = clock

    def execute(self, text: str) -> None:
        """@brief Record the whole text as typed now.

        @param text The whole text as the writer has it now.
        @raises TypeError When text is not a str.
        """
        self._session.type_text(text, self._clock.now())
