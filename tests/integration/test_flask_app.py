"""@file
@brief Integration tests of the Flask application with a fake clock.
"""

from typing import Any

import pytest
from flask import Flask
from flask.testing import FlaskClient

from disappearing_text.constants import (
    IDLE_TIMEOUT_SECONDS,
    POLL_INTERVAL_MILLISECONDS,
    WARNING_THRESHOLD_SECONDS,
)
from disappearing_text.presentation.composition_root import create_app


class FakeClock:
    """@brief A clock whose moment the test sets."""

    def __init__(self, moment: float = 100.0) -> None:
        """@param moment The first moment."""
        self.moment = moment

    def now(self) -> float:
        """@brief The moment set by the test."""
        return self.moment


@pytest.fixture
def clock() -> FakeClock:
    """@brief The fake clock shared by the app and the test."""
    return FakeClock()


@pytest.fixture
def app(clock: FakeClock) -> Flask:
    """@brief An app built on the fake clock."""
    return create_app(clock)


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """@brief A test client of the app."""
    return app.test_client()


def _type(client: FlaskClient, text: str) -> dict[str, Any]:
    """@brief Post the text and return the state JSON."""
    response = client.post("/api/text", json={"text": text})
    assert response.status_code == 200
    body = response.get_json()
    assert isinstance(body, dict)
    return body


def _state(client: FlaskClient) -> dict[str, Any]:
    """@brief Read the state JSON."""
    response = client.get("/api/state")
    assert response.status_code == 200
    body = response.get_json()
    assert isinstance(body, dict)
    return body


def test_page_returns_editor_with_textarea(client: FlaskClient) -> None:
    """@brief GET / serves the page with the text area and its state."""
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "<textarea" in html
    assert "autofocus" in html
    assert 'id="editor"' in html
    assert 'id="countdown"' in html
    assert 'id="status"' in html
    assert 'data-state="state-empty"' in html
    assert "Write without stopping" in html
    assert "/static/writing.js" in html
    assert "/static/writing.css" in html


def test_state_is_empty_for_new_session(client: FlaskClient) -> None:
    """@brief A new session has no text and no countdown."""
    state = _state(client)
    assert state["text"] == ""
    assert state["seconds_left"] is None
    assert state["is_warning"] is False
    assert state["was_cleared"] is False


def test_state_carries_timing_constants(client: FlaskClient) -> None:
    """@brief The state JSON has the three timing values."""
    state = _state(client)
    assert state["idle_timeout_seconds"] == IDLE_TIMEOUT_SECONDS
    assert state["warning_threshold_seconds"] == WARNING_THRESHOLD_SECONDS
    assert state["poll_interval_milliseconds"] == POLL_INTERVAL_MILLISECONDS


def test_typing_keeps_text_with_full_countdown(client: FlaskClient) -> None:
    """@brief At the same instant the text is kept with 5 seconds left."""
    body = _type(client, "hello")
    assert body["text"] == "hello"
    assert body["seconds_left"] == 5
    assert _state(client)["text"] == "hello"


def test_text_is_kept_at_exactly_five_seconds(
    client: FlaskClient, clock: FakeClock
) -> None:
    """@brief Boundary: exactly 5 seconds keeps the text."""
    _type(client, "hello")
    clock.moment += 5.0
    state = _state(client)
    assert state["text"] == "hello"
    assert state["was_cleared"] is False


def test_text_is_cleared_just_after_five_seconds(
    client: FlaskClient, clock: FakeClock
) -> None:
    """@brief Boundary: 5.001 seconds clears the text and flags it."""
    _type(client, "hello")
    clock.moment += 5.001
    state = _state(client)
    assert state["text"] == ""
    assert state["was_cleared"] is True
    assert state["seconds_left"] is None


def test_typing_again_resets_was_cleared(client: FlaskClient, clock: FakeClock) -> None:
    """@brief Typing after the clear ends the text gone state."""
    _type(client, "hello")
    clock.moment += 6.0
    assert _state(client)["was_cleared"] is True
    assert _type(client, "again")["was_cleared"] is False


def test_warning_flag_at_two_seconds_left(
    client: FlaskClient, clock: FakeClock
) -> None:
    """@brief The warning starts at 2 seconds left, inclusive."""
    _type(client, "hello")
    clock.moment += 2.9
    assert _state(client)["is_warning"] is False
    clock.moment = 103.0
    state = _state(client)
    assert state["seconds_left"] == 2
    assert state["is_warning"] is True


def test_post_rejects_non_object_body(client: FlaskClient) -> None:
    """@brief A JSON list is answered with 400 and an error."""
    response = client.post("/api/text", json=["hello"])
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_rejects_body_that_is_not_json(client: FlaskClient) -> None:
    """@brief A plain text body is answered with 400."""
    response = client.post("/api/text", data="hello", content_type="text/plain")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_rejects_missing_text(client: FlaskClient) -> None:
    """@brief An object without text is answered with 400."""
    response = client.post("/api/text", json={"other": "x"})
    assert response.status_code == 400
    assert "error" in response.get_json()


@pytest.mark.parametrize("value", [1, None, ["a"], {"a": 1}, True])
def test_post_rejects_text_that_is_not_a_string(
    client: FlaskClient, value: object
) -> None:
    """@brief Each non-string text is answered with 400."""
    response = client.post("/api/text", json={"text": value})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_rejected_post_leaves_state_unchanged(client: FlaskClient) -> None:
    """@brief A 400 does not change the text."""
    _type(client, "hello")
    client.post("/api/text", json={"text": 1})
    assert _state(client)["text"] == "hello"


def test_static_files_are_served(client: FlaskClient) -> None:
    """@brief The script and the style sheet are served under /static."""
    script = client.get("/static/writing.js")
    style = client.get("/static/writing.css")
    assert script.status_code == 200
    assert style.status_code == 200
    script.close()
    style.close()


def test_apps_do_not_share_sessions() -> None:
    """@brief Each create_app call builds its own session."""
    first = create_app(FakeClock()).test_client()
    second = create_app(FakeClock()).test_client()
    first.post("/api/text", json={"text": "only first"})
    assert _state(second)["text"] == ""


def test_create_app_without_clock_uses_system_clock() -> None:
    """@brief The default app works with the real clock."""
    client = create_app().test_client()
    assert _type(client, "hi")["text"] == "hi"
