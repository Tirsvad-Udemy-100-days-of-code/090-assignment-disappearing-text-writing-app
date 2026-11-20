"""@file
@brief The state of the writing session as the presentation sees it.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WritingState:
    """@brief Snapshot of the writing session.

    @param text The text the writer has now.
    @param seconds_left Seconds until the text is deleted, or None without text.
    @param is_warning True when the text is about to be deleted.
    @param was_cleared True when the text was deleted and not typed again since.
    """

    text: str
    seconds_left: float | None
    is_warning: bool
    was_cleared: bool
