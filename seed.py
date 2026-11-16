"""Datu sintetikoak sortzeko script-a.

Erabilera:
    python seed.py
    python seed.py --reset
"""

import argparse

from sqlalchemy import func, select

from app.db import Base, SessionLocal, engine
from app.models import Ticket, TicketPriority, TicketStatus

TICKETS = [
    {
        "title": "Erabiltzailea ez da saioa hasten",
        "description": "Saioa hasteko orrian errore bat agertzen da.",
        "status": TicketStatus.open,
        "priority": TicketPriority.high,
        "assignee": "ane",
    },
    {
        "title": "Faktura okerra PDFan",
        "description": "Fakturako zenbatekoa ez dator bat erosketa-historialarekin.",
        "status": TicketStatus.in_progress,
        "priority": TicketPriority.urgent,
        "assignee": "jon",
    },
    {
        "title": "Bilaketa motela da",
        "description": "Bilaketak 5 segundo baino gehiago behar ditu.",
        "status": TicketStatus.blocked,
        "priority": TicketPriority.medium,
        "assignee": "ane",
    },
    {
        "title": "UIan testu bat oker",
        "description": "Hasi botoiaren testua ingelesez agertzen da.",
        "status": TicketStatus.closed,
        "priority": TicketPriority.low,
        "assignee": None,
    },
    {
        "title": "APIak 500 ematen du",
        "description": "Ordainketa egitean errore orokorra itzultzen da.",
        "status": TicketStatus.open,
        "priority": TicketPriority.urgent,
        "assignee": None,
    },
    {
        "title": "Pasahitza berrezartzeko mezua",
        "description": "Berrezartzeko posta ez da iristen.",
        "status": TicketStatus.closed,
        "priority": TicketPriority.medium,
        "assignee": "jon",
    },
    {
        "title": "Izen-ematea ez da osatzen",
        "description": "Azken urratsean formularioa ez da bidaltzen.",
        "status": TicketStatus.open,
        "priority": TicketPriority.medium,
        "assignee": None,
    },
    {
        "title": "Txostenak ez du daturik erakusten",
        "description": "Hileko txostenak zero balioak erakusten ditu.",
        "status": TicketStatus.in_progress,
        "priority": TicketPriority.high,
        "assignee": "ane",
    },
    {
        "title": "Saioa iraungitzen da azkar",
        "description": "Erabiltzailea minutu batzuetan kanporatzen da.",
        "status": TicketStatus.blocked,
        "priority": TicketPriority.high,
        "assignee": "jon",
    },
    {
        "title": "Inprimakia ez da bidaltzen",
        "description": "Harremanetarako inprimakiak ez du erantzunik ematen.",
        "status": TicketStatus.closed,
        "priority": TicketPriority.low,
        "assignee": None,
    },
    {
        "title": "APIaren dokumentazioa ez da irekitzen",
        "description": "/docs bideak errore bat ematen du.",
        "status": TicketStatus.open,
        "priority": TicketPriority.low,
        "assignee": "ane",
    },
    {
        "title": "Jakinarazpenak ez dira iristen",
        "description": "Erabiltzaileek ez dute posta bidezko abisurik jasotzen.",
        "status": TicketStatus.in_progress,
        "priority": TicketPriority.medium,
        "assignee": None,
    },
]


def seed(reset: bool = False) -> None:
    if reset:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        count = db.scalar(select(func.count()).select_from(Ticket))
        if count:
            print(f"{count} ticket daude jada. Erabili --reset berriz sortzeko.")
            return

        db.add_all([Ticket(**data) for data in TICKETS])
        db.commit()
        print(f"{len(TICKETS)} ticket sintetiko txertatu dira.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ticketak-api datu sintetikoak")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Lehendik dagoen datu-basea ezabatu eta berriz sortu.",
    )
    args = parser.parse_args()
    seed(reset=args.reset)
