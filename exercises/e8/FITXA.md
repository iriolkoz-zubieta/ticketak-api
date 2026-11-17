# E8 — MCP (aukeran)

**Saioa:** 6 · **Iraupena:** 25 min · **Modua:** bikoteka  
**Entregagarria:** kontsulta-log-a + arriskuen azalpena

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

MCP (Model Context Protocol) zer den ulertzea: agenteek kanpoko tresnak eta datuak modu estandarrean atzitzeko protokoloa. Garrantzitsuena ez da konfigurazioa, **baimenak** baizik.

## Testuingurua

Irakasleak **irakurketa-soilik** den SQLite MCP zerbitzari bat prestatu du. Zure lana da kontsulta bat egitea, emaitza egiaztatzea eta arriskuak azaltzea.

## 1. urratsa — Egiaztatu

```bash
opencode mcp list
```

- Zer zerbitzari dago?
- Irakurketa-soilik al da?
- Zein tresna eskaintzen ditu?

## 2. urratsa — Kontsulta bat

OpenCode-rekin:

> Erabili SQLite MCP tresna. Zenbat ticket daude `closed` egoeran? Erakutsi kontsulta eta emaitza.

Gorde:

| Elementua | Balioa |
|---|---|
| Prompta | |
| Erabilitako tresna | |
| Kontsulta | |
| Emaitza | |

## 3. urratsa — Egiaztatu

Egiaztatu emaitza SQL kontsulta batekin:

```python
import sqlite3

con = sqlite3.connect("tickets.db")
rows = con.execute(
    "select status, count(*) from tickets group by status"
).fetchall()
print(rows)
```

| Status | MCP emaitza | SQL emaitza | Bat datoz? |
|---|---|---|---|
| open | | | |
| in_progress | | | |
| blocked | | | |
| closed | | | |

## 4. urratsa — Arriskuak

Erantzun:

- Zer gertatuko litzateke MCP zerbitzariak idazketa-baimena izango balu?
- Nola mugatuko zenuke tresna hori?
- Zein datu ez zenuke inoiz MCP bidez erakutsiko?

## Onarpen-checklista

- [ ] MCP zerbitzaria konektatuta.
- [ ] Kontsulta bat egin eta emaitza egiaztatuta.
- [ ] SQL emaitzarekin alderatuta.
- [ ] Arriskuen azalpena idatzita.
- [ ] Ez da idazketarik egin.
- [ ] AA erregistroan jasota.

## Plan B

MCP ez badago eskuragarri, simulatu Python script batekin: tresna-eskema bat eta funtzio bat. Kontzeptua eta baimenak landu.

## Gogoeta

> MCPk agentea ahaltsuago egiten du. Nola ziurtatuko duzu ahalmen hori ez dela arriskutsua?
