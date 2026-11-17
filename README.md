# ticketak-api

Laguntza-txartelen kudeaketarako API didaktikoa: **FastAPI + SQLite + pytest**.

Proiektu hau DAW 2. mailako AA tailerrerako starter repo-a da. Baseline-ak ticketen CRUD-a, egoera-aldaketak eta iragazketak lantzen ditu; **etiketak (tags) ez daude**, azken erronkan (E9) gehituko dira.

## Azkar hasteko

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

python -m pip install -e ".[dev]"
python seed.py --reset
uvicorn app.main:app --reload
```

- APIa: <http://127.0.0.1:8000>
- Dokumentazio interaktiboa: <http://127.0.0.1:8000/docs>
- Osasun-egiaztapena: <http://127.0.0.1:8000/health>

## Endpointak

| Metodoa | Bidea | Deskribapena |
|---|---|---|
| `GET` | `/health` | Zerbitzuaren egoera |
| `POST` | `/tickets` | Ticket berria sortu (`201`) |
| `GET` | `/tickets?status=&priority=` | Ticketak zerrendatu eta iragazi |
| `GET` | `/tickets/{id}` | Ticket bat lortu (`404` ez bada) |
| `PATCH` | `/tickets/{id}` | Eremu batzuk eguneratu |
| `DELETE` | `/tickets/{id}` | Ticket-a ezabatu (`204`) |

### Adibidea

```bash
curl -X POST http://127.0.0.1:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{
    "title": "APIak 500 ematen du",
    "description": "Ordainketa egitean errore orokorra itzultzen da.",
    "status": "open",
    "priority": "urgent",
    "assignee": "ane"
  }'
```

```bash
curl "http://127.0.0.1:8000/tickets?status=open&priority=urgent"
```

## Egoera-aldaketak

| Unetik | Nora | Baimenduta |
|---|---|---|
| `open` | `in_progress` | Bai |
| `in_progress` | `blocked` | Bai |
| `in_progress` | `closed` | Bai |
| `blocked` | `in_progress` | Bai |
| `closed` | `open` | Bai (berriz ireki) |
| Besteak | | Ez (`422`) |

Egoera bera ezartzea ez da errorea.

## Proiektuaren egitura

```
ticketak-api/
├── app/
│   ├── main.py        # FastAPI aplikazioa
│   ├── models.py      # SQLAlchemy modeloak
│   ├── schemas.py     # Pydantic eskemak
│   ├── services.py    # negozio-logika
│   └── db.py          # datu-basearen konexioa
├── tests/
│   ├── conftest.py
│   ├── test_tickets.py
│   └── test_services.py
├── exercises/
│   └── e5/            # segurtasun-ariketako fixtureak
├── seed.py
├── AGENTS.md
└── pyproject.toml
```

## Probak

```bash
pytest -q
```

Proba bakoitzak SQLite memoria-barneko datu-basea erabiltzen du; ez du `tickets.db` fitxategia ukitzen.

## Datu sintetikoak

```bash
python seed.py          # datuak txertatu (lehendik badaude, ez du ezer egiten)
python seed.py --reset  # datu-basea ezabatu eta berriz sortu
```

## Irakaskuntza-materialak

- `exercises/README.md`: ikasle-fitxen indizea (E1–E9).
- `exercises/AA_ERREGISTROA.md`: prompten erregistroa eta amaierako deklarazioa.
- `exercises/e5/`: **helburu didaktikoko material ez-segurua** — sekretu faltsuak, datu pertsonal faltsuak eta prompt injection baten adibidea. Ez da inoiz produkzioan erabili behar, eta ez da `app/` kodean sartzen.

## Irakaskuntza-branchak

| Brancha | Erabilera |
|---|---|
| `main` | Baseline garbia |
| `pr-ai` | E4: AAk sortutako PR-a, 6 arazoekin |
| `agent-bug` | E6b: `GET /tickets?status=` bug-a eta `AGENTS.md` minimoa |

```bash
git switch pr-ai      # E4
git switch agent-bug  # E6b
git switch main       # baseline
```

Ez egin merge branch hauetatik `main`-era; ariketa-materiala da.

## Oharrak

- Baseline-an **ez dago etiketarik**; E9 ariketan gehitzen dira.
- Datu guztiak sintetikoak dira. Ez erabili bezero errealen daturik.
- `AGENTS.md` fitxategiak agentearentzako arauak ditu.
