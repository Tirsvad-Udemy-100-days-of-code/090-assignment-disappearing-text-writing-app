"""@file
@brief Controller that maps HTTP requests to the writing use cases.
"""

from dataclasses import asdict

from flask import Blueprint, Response, jsonify, render_template, request

from disappearing_text.application.use_cases.get_writing_state import GetWritingState
from disappearing_text.application.use_cases.type_text import TypeText
from disappearing_text.presentation.features.writing.writing_view_model import (
    WritingViewModel,
)


class WritingController:
    """@brief Serves the page and the two JSON routes of the writing session."""

    def __init__(self, type_text: TypeText, get_state: GetWritingState) -> None:
        """@brief Create the controller.

        @param type_text The use case that stores the typed text.
        @param get_state The use case that reads the writing state.
        """
        self._type_text = type_text
        self._get_state = get_state

    def blueprint(self) -> Blueprint:
        """@brief Build the blueprint with the three routes.

        @return A blueprint with GET /, GET /api/state and POST /api/text.
        """
        blueprint = Blueprint("writing", __name__)
        blueprint.add_url_rule("/", "page", self._page, methods=["GET"])
        blueprint.add_url_rule("/api/state", "state", self._state, methods=["GET"])
        blueprint.add_url_rule("/api/text", "text", self._text, methods=["POST"])
        return blueprint

    def _page(self) -> str:
        """@brief Render the editor page.

        @return The HTML of the page.
        """
        return render_template(
            "writing_view.html", view=WritingViewModel.from_constants()
        )

    def _state(self) -> Response:
        """@brief Answer with the writing state.

        @return The state as JSON.
        """
        return self._state_response()

    def _text(self) -> Response | tuple[Response, int]:
        """@brief Store the posted text and answer with the new state.

        @return The state as JSON, or 400 with an error message.
        """
        body = request.get_json(silent=True)
        if not isinstance(body, dict):
            return self._error("The body must be a JSON object.")
        text = body.get("text")
        if not isinstance(text, str):
            return self._error("The field 'text' must be a string.")
        self._type_text.execute(text)
        return self._state_response()

    def _state_response(self) -> Response:
        """@brief Map the state of the use case to a JSON response.

        @return The state and the timing values as JSON.
        """
        payload = asdict(self._get_state.execute())
        view = WritingViewModel.from_constants()
        payload["idle_timeout_seconds"] = view.idle_timeout_seconds
        payload["warning_threshold_seconds"] = view.warning_threshold_seconds
        payload["poll_interval_milliseconds"] = view.poll_interval_milliseconds
        return jsonify(payload)

    @staticmethod
    def _error(message: str) -> tuple[Response, int]:
        """@brief Build a 400 answer.

        @param message What is wrong with the request.
        @return The JSON error and the status code 400.
        """
        return jsonify({"error": message}), 400
