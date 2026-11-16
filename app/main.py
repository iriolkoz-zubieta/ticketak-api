"""FastAPI aplikazioa: ticketak kudeatzeko APIa."""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from . import models, schemas, services
from .db import get_db

app = FastAPI(
    title="ticketak-api",
    description="Laguntza-txartelen kudeaketarako API didaktikoa.",
    version="0.1.0",
)

DbSession = Annotated[Session, Depends(get_db)]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/tickets",
    response_model=schemas.TicketRead,
    status_code=status.HTTP_201_CREATED,
)
def create_ticket(
    payload: schemas.TicketCreate,
    db: DbSession,
) -> models.Ticket:
    return services.create_ticket(db, payload)


@app.get("/tickets", response_model=list[schemas.TicketRead])
def list_tickets(
    db: DbSession,
    status: models.TicketStatus | None = None,
    priority: models.TicketPriority | None = None,
) -> list[models.Ticket]:
    return services.list_tickets(db, status=status, priority=priority)


@app.get("/tickets/{ticket_id}", response_model=schemas.TicketRead)
def get_ticket(ticket_id: int, db: DbSession) -> models.Ticket:
    ticket = services.get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket ez da aurkitu",
        )
    return ticket


@app.patch("/tickets/{ticket_id}", response_model=schemas.TicketRead)
def update_ticket(
    ticket_id: int,
    payload: schemas.TicketUpdate,
    db: DbSession,
) -> models.Ticket:
    ticket = services.get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket ez da aurkitu",
        )

    try:
        return services.update_ticket(db, ticket, payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: int, db: DbSession) -> Response:
    ticket = services.get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket ez da aurkitu",
        )

    services.delete_ticket(db, ticket)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
