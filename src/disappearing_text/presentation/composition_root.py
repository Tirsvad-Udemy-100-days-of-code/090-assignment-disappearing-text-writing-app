"""@file
@brief Composition root: builds the Flask application and connects its parts.
"""

from pathlib import Path

from flask import Flask

from disappearing_text.application.ports.clock import Clock
from disappearing_text.application.use_cases.get_writing_state import GetWritingState
from disappearing_text.application.use_cases.type_text import TypeText
from disappearing_text.domain.writing_session import WritingSession
from disappearing_text.infrastructure.system_clock import SystemClock
from disappearing_text.presentation.features.writing.writing_controller import (
    WritingController,
)

## Folder with the templates and static files of the writing feature.
_WRITING_FOLDER = Path(__file__).parent / "features" / "writing"


def create_app(clock: Clock | None = None) -> Flask:
    """@brief Build a Flask application with its own writing session.

    @param clock The source of time; the system clock when None.
    @return The configured Flask application.
    """
    session = WritingSession()
    used_clock = SystemClock() if clock is None else clock
    controller = WritingController(
        TypeText(session, used_clock), GetWritingState(session, used_clock)
    )
    app = Flask(
        __name__,
        template_folder=str(_WRITING_FOLDER / "templates"),
        static_folder=str(_WRITING_FOLDER / "static"),
        static_url_path="/static",
    )
    app.register_blueprint(controller.blueprint())
    return app
