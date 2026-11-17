# E4 eta E6 — Irakasle-gida laburra

> **Irakasleentzako materiala.** Erantzunak eta analisi-teknikoak ditu; ez partekatu ikasleekin.

## E4 — AAk sortutako PR baten review-a

### Datu azkarrak

| Elementua | Balioa |
|---|---|
| Brancha | `pr-ai` |
| Iraupena | 45 min |
| Ikasle-fitxa | `exercises/e4/FITXA.md` |
| Helburua | Kodea berrikustea, ez soilik probak pasatzea |
| Materiala | `git diff main...pr-ai`, review checklista |

### Prestaketa

```bash
git switch pr-ai
git diff main...pr-ai
pytest -q
```

- Testak **berde** daude (25 passed), baina kodea ez da segurua. Hori da ikasgaia.
- **Ez instalatu** PR honetako dependendentziak; `requests==2.31.0` zaharkitua da eta review-a lehenago egin behar da.
- Ez egin merge `main`-era.

### Espero diren 6 arazoak

| # | Arazoa | Kokapena | Larritasuna | Konponbide esperoa |
|---|---|---|---|---|
| 1 | SQL injection | `app/services.py:57-68` (61-65) | Altua | ORM `select` + `ilike`, edo `text()` parametrizatua `:q` erabiliz |
| 2 | Sekretu gogor-kodetua | `app/notifications.py:3` | Altua | `os.getenv("AI_API_KEY")`, `.env.example`, gakoa errotatu |
| 3 | `except:` hutsa | `app/notifications.py:17` | Ertaina | `except requests.RequestException`, loga, errorea ez ezkutatu |
| 4 | Balidaziorik eza | `app/main.py:47-52`, `app/services.py:57-65` | Ertaina/altua | `Query(min_length=1, max_length=100)`, `status` enum, `status` parametroa ez interpolatu |
| 5 | Assertionik gabeko testa | `tests/test_search.py:19-20` | Ertaina | Statusa, emaitza-kopurua eta ertz-kasuak egiaztatu |
| 6 | Dependendentzia zaharkitua | `pyproject.toml:16` | Ertaina | Eguneratu edo kendu; `pip-audit` / justifikatu |

### Fix-adibideak

**1. SQL injection — ORM bidez:**

```python
from sqlalchemy import or_, select


def search_tickets(db, query, status=None):
    stmt = select(models.Ticket).where(
        or_(
            models.Ticket.title.ilike(f"%{query}%"),
            models.Ticket.description.ilike(f"%{query}%"),
        )
    )
    if status is not None:
        stmt = stmt.where(models.Ticket.status == status)
    return list(db.scalars(stmt).all())
```

**Edo `text()` parametrizatua:**

```python
sql = text(
    "SELECT * FROM tickets "
    "WHERE title LIKE :q OR description LIKE :q"
)
rows = db.execute(sql, {"q": f"%{query}%"}).mappings().all()
```

**2. Sekretua:**

```python
import os

AI_API_KEY = os.environ["AI_API_KEY"]
```

Gehitu `.env.example` garbia, ez commit-atu `.env`, eta errotatu gakoa.

**3. `except:`:**

```python
except requests.RequestException as exc:
    logger.warning("AI summary bidalketa huts egin du: %s", exc)
```

**4. Balidazioa:**

```python
from typing import Annotated
from fastapi import Query

q: Annotated[str, Query(min_length=1, max_length=100)],
status: models.TicketStatus | None = None,
```

**5. Testa:**

```python
def test_search_tickets(client):
    response = client.get("/tickets/search?q=API")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert client.get("/tickets/search?q=").status_code == 422
```

**6. Dependendentzia:**

- `requests==2.31.0` zaharkitua da; eguneratu edo kendu.
- Egiaztatu `pip-audit` edo antzeko tresnarekin.
- Ez instalatu PR-a berrikusi aurretik.

### Saioaren gidoia

| Denbora | Jarduera |
|---|---|
| 0–5 | Brancha, diff-a eta helburua |
| 5–20 | Banakako review-a checklistarekin |
| 20–30 | AAri review-a eskatu eta konparatu |
| 30–40 | Konponketa bat aukeratu eta commit egin |
| 40–45 | Debrief: zer ez zuen probak harrapatu? |

### Ohiko akatsak

- "Testak berde daude, beraz ondo dago" esatea.
- Estilo-arazoak lehenestea SQL injection/sekretuaren aurrean.
- "Erabili ORM" esatea, baina konponbide zehatzik ez ematea.
- `requests` instalatzea eta ingurunea aldatzea.
- `except:` eta `except Exception` nahastea.
- Status-parametroaren SQL injection-a ez ikustea.

### Debrief-galderak

1. Zergatik pasatzen dute testek arazoak daudenean?
2. Zein arazo konponduko zenuke lehenengo, eta zergatik?
3. Nola eragotziko zenuke sekretu bat commit-ean?
4. Zer egin behar du giza review-ak AAren review-ak egiten ez duena?

### Ebaluazioa

- Gutxienez **5/6 arazo**.
- Larritasuna eta kokapena argi.
- Konponbide zehatza, ez orokorra.
- Commit txiki bat.
- Ez du testik ahuldu.
- Kodea hitzez hitz azaltzeko gai.

---

## E6 — Agenteak: autonomia kontrolpean

### Datu azkarrak

| Elementua | Balioa |
|---|---|
| Brancha | `agent-bug` |
| Iraupena | 85 min (A: 30, B: 55) |
| Ikasle-fitxa | `exercises/e6/FITXA.md` |
| Helburua | Agentea gainbegiratzea, `AGENTS.md` bidez mugak ezartzea |
| Materiala | `agent-bug`, OpenCode, `AGENTS.md` minimoa |

### Prestaketa

```bash
git switch agent-bug
pytest -q
```

- Testak **berde** daude (23 passed), baina bug bat dago.
- Egiaztatu:

```text
GET /tickets?status=done  → 500
GET /tickets?status=open  → 200
```

- `AGENTS.md` minimoa da, fase 1ean agenteak arau gutxi izateko.

### Bugaren analisia

| Elementua | Kokapena | Azalpena |
|---|---|---|
| Endpointa | `app/main.py:38-43` | `status`/`priority` `str` gisa onartzen dira; FastAPI-k ez du enum balidaziorik egiten |
| Zerbitzua | `app/services.py:44-57` | `TicketStatus(status)` / `TicketPriority(priority)` `ValueError` jaurtitzen du; ez da harrapatzen |
| Ondorioa | `GET /tickets?status=done` | `ValueError` → `500 Internal Server Error` |
| Testa | `tests/test_tickets.py` | Invalid statusaren assertions kendu da; horregatik ez da bug-a detektatzen |

### Konponbide posibleak

**Aukera gomendatua — enumak berrezarri:**

```python
def list_tickets(
    db: DbSession,
    status: models.TicketStatus | None = None,
    priority: models.TicketPriority | None = None,
) -> list[models.Ticket]:
    return services.list_tickets(db, status=status, priority=priority)
```

FastAPI-k `422` itzuliko du balio okerrarekin.

**Beste aukera — zerbitzuan balidatu eta 422ra mapatu:**

```python
try:
    status_value = models.TicketStatus(status)
except ValueError as exc:
    raise ValueError(f"status okerra: {status}") from exc
```

Baina `ValueError` ezin da `500` bihurtu; endpointak `HTTPException(422)` bihurtu behar du.

**Gehitu testak:**

```python
def test_invalid_status_returns_422(client):
    assert client.get("/tickets?status=done").status_code == 422


def test_invalid_priority_returns_422(client):
    assert client.get("/tickets?priority=critical").status_code == 422
```

### Saioaren gidoia

| Denbora | Jarduera |
|---|---|
| 0–5 | Brancha, bug-a eta helburua |
| 5–15 | E6a: agente-miniaren anatomia |
| 15–40 | Fase 1: mugarik gabe, Plan → Build |
| 40–50 | Atsedena |
| 50–75 | Fase 2: `AGENTS.md` eta berriz exekutatu |
| 75–85 | Konparaketa eta debrief |

### `AGENTS.md` minimoa → fase 2

Fase 1ean:

```markdown
# Proiektuaren arauak

Proiektu didaktikoa da. Mantendu kodea argia eta erraz irakurtzeko modukoa.
```

Fase 2an gehitu:

```markdown
## Komandoak
- Probak: `pytest -q`
- Lint: `ruff check .`

## Arauak
- Exekutatu probak amaitu aurretik.
- Ez aldatu testak baimenik gabe.
- Ez gehitu dependendentzia berririk baimenik gabe.
- Ezabatu aurretik galdetu.
- Mantendu diff-a txikia eta erlazionatua.
- Ez commit-atu sekreturik.
- Balio okerrek `422` itzuli behar dute, ez `500`.
```

### Ohiko agente-porrotak

- `try/except` gehitu eta `500` edo `[]` itzultzea, `422` izan beharrean.
- Testak aldatzea `500` espero izateko.
- Balidazioa leku okerrean jartzea.
- Diff handia eta erlazionatugabea.
- Testak ez exekutatzea `AGENTS.md` minimoa delako.
- Dependendentzia berri bat gehitzea.
- Status-aldaketen arauak haustea.

### Debrief-galderak

1. Non egon behar du balidazioak: FastAPI geruzan, zerbitzuan edo bietan?
2. Zergatik ez zuen testak bug-a harrapatu?
3. Zer aldatu zuen `AGENTS.md`-k agentearen portaeran?
4. Noiz esku hartu behar du gizakiak?
5. Zer egingo zenuke agenteak testak aldatzen baditu?

### Ebaluazioa

- Bug-a konponduta.
- `422` balio okerretarako.
- Test berriak gehitu dira.
- Ez da testik ahuldu.
- Diff txikia eta erlazionatua.
- `AGENTS.md` arrazoitua.
- Konparaketa eta gogoeta idatzita.

### Brancha berrezartzeko

```bash
git reset --hard HEAD
git clean -fd   # untracked fitxategiak ezabatzen ditu; ziurtatu ezer gorde gabe
```

---

## Oharrak

- Branchak lokalak dira; ez push egin irakasleak berariaz eskatu ezean.
- `pr-ai` eta `agent-bug` ez dira `main`-era mergeatuko.
- E4ko PR-a ez da instalatu behar; review-a da ariketa.
