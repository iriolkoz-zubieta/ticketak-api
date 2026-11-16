"""Negozio-logika: ticketen CRUD-a eta egoera-aldaketen arauak."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas

ALLOWED_TRANSITIONS: dict[models.TicketStatus, set[models.TicketStatus]] = {
    models.TicketStatus.open: {models.TicketStatus.in_progress},
    models.TicketStatus.in_progress: {
        models.TicketStatus.blocked,
        models.TicketStatus.closed,
    },
    models.TicketStatus.blocked: {models.TicketStatus.in_progress},
    models.TicketStatus.closed: {models.TicketStatus.open},
}


def validate_status_transition(
    current: models.TicketStatus, new: models.TicketStatus
) -> None:
    """Egoera-aldaketa baimenduta dagoen egiaztatu.

    Egoera bera ezartzea ez da errorea (PATCH idempotentea delako).
    """

    if current == new:
        return
    allowed = ALLOWED_TRANSITIONS.get(current, set())
    if new not in allowed:
        raise ValueError(
            f"Egoera-aldaketa ez da baimenduta: {current.value} -> {new.value}"
        )


def create_ticket(db: Session, data: schemas.TicketCreate) -> models.Ticket:
    ticket = models.Ticket(**data.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def list_tickets(
    db: Session,
    status: models.TicketStatus | None = None,
    priority: models.TicketPriority | None = None,
) -> list[models.Ticket]:
    stmt = select(models.Ticket).order_by(models.Ticket.id)
    if status is not None:
        stmt = stmt.where(models.Ticket.status == status)
    if priority is not None:
        stmt = stmt.where(models.Ticket.priority == priority)
    return list(db.scalars(stmt).all())


def get_ticket(db: Session, ticket_id: int) -> models.Ticket | None:
    return db.get(models.Ticket, ticket_id)


def update_ticket(
    db: Session, ticket: models.Ticket, data: schemas.TicketUpdate
) -> models.Ticket:
    updates = data.model_dump(exclude_unset=True)

    for field in ("title", "description", "status", "priority"):
        if field in updates and updates[field] is None:
            raise ValueError(f"{field} eremua ezin da null izan")

    new_status = updates.get("status")
    if new_status is not None:
        validate_status_transition(ticket.status, new_status)

    for field, value in updates.items():
        setattr(ticket, field, value)

    db.commit()
    db.refresh(ticket)
    return ticket


def delete_ticket(db: Session, ticket: models.Ticket) -> None:
    db.delete(ticket)
    db.commit()
