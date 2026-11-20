"""@file
@brief Tests of the WritingViewModel.
"""

import dataclasses

import pytest

from disappearing_text.constants import (
    IDLE_TIMEOUT_SECONDS,
    POLL_INTERVAL_MILLISECONDS,
    WARNING_THRESHOLD_SECONDS,
)
from disappearing_text.presentation.features.writing.writing_view_model import (
    WritingViewModel,
)


def test_from_constants_uses_wireframe_title() -> None:
    """@brief The title is the one of the wireframe."""
    assert WritingViewModel.from_constants().title == "Write without stopping"


def test_from_constants_reads_the_timing_constants() -> None:
    """@brief The three timing values come from the constants module."""
    model = WritingViewModel.from_constants()
    assert model.idle_timeout_seconds == IDLE_TIMEOUT_SECONDS
    assert model.warning_threshold_seconds == WARNING_THRESHOLD_SECONDS
    assert model.poll_interval_milliseconds == POLL_INTERVAL_MILLISECONDS


def test_view_model_is_frozen() -> None:
    """@brief A view model cannot be changed after creation."""
    model = WritingViewModel.from_constants()
    with pytest.raises(dataclasses.FrozenInstanceError):
        model.title = "other"  # type: ignore[misc]
