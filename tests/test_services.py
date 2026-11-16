"""Egoera-aldaketen arauen probak."""

import pytest

from app.models import TicketStatus
from app.services import validate_status_transition


@pytest.mark.parametrize(
    ("current", "new"),
    [
        (TicketStatus.open, TicketStatus.open),
        (TicketStatus.open, TicketStatus.in_progress),
        (TicketStatus.in_progress, TicketStatus.blocked),
        (TicketStatus.blocked, TicketStatus.in_progress),
        (TicketStatus.in_progress, TicketStatus.closed),
        (TicketStatus.closed, TicketStatus.open),
    ],
)
def test_allowed_transitions(current, new):
    validate_status_transition(current, new)


@pytest.mark.parametrize(
    ("current", "new"),
    [
        (TicketStatus.open, TicketStatus.blocked),
        (TicketStatus.open, TicketStatus.closed),
        (TicketStatus.closed, TicketStatus.in_progress),
        (TicketStatus.blocked, TicketStatus.closed),
    ],
)
def test_invalid_transitions(current, new):
    with pytest.raises(ValueError):
        validate_status_transition(current, new)
