# E7 — Skill bat sortu

**Saioa:** 6 · **Iraupena:** 30 min · **Modua:** bikoteka  
**Entregagarria:** `.opencode/skills/api-endpoint/SKILL.md` + proba-log-a

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Lan errepikakor bat estandartzeko **skill** bat sortzea. Skill bat ez da prompt luze bat beti itsatsita: behar denean kargatzen den argibide-multzo bat da.

## Testuingurua

Proiektuan endpoint berriak gehitu ohi dira. Urratsak beti berdinak dira: eskema, ibilbidea, zerbitzua, probak eta dokumentazioa. Skill batek urrats horiek koherenteak izatea lortzen du.

## 1. urratsa — Karpeta sortu

OpenCode V2-k proiektu-mailako skillak `.opencode/skills/` karpetan bilatzen ditu:

```text
.opencode/
└── skills/
    └── api-endpoint/
        └── SKILL.md
```

Skillaren **IDa** karpeta-izena da: `api-endpoint`.

## 2. urratsa — `SKILL.md` idatzi

Erabili txantiloi hau:

```markdown
---
name: API Endpoint
description: Erabili FastAPI endpoint berri bat gehitzeko, Pydantic ereduarekin, probekin eta dokumentazioarekin.
---

# FastAPI endpoint berria

## Noiz erabili
Endpoint berri bat edo CRUD eragiketa bat gehitzean.

## Sarrerak
- Baliabidearen izena
- Eremuak eta motak
- Baimen-arauak

## Urratsak
1. Sortu Pydantic eskema `app/schemas.py`-n.
2. Gehitu ibilbidea `app/main.py`-n.
3. Gehitu zerbitzu-funtzioa `app/services.py`-n.
4. Idatzi probak `tests/`-n.
5. Eguneratu README.

## Onarpen-checklista
- [ ] Proba guztiak berde
- [ ] Sarrera balidatuta
- [ ] Erroreak 4xx moduan
- [ ] Dokumentazioa eguneratuta

## Adibidea
Endpoint bat: `GET /tickets/{id}`.
```

> **Gakoa:** `description` eremua argia izan behar da. Hori da OpenCode-k skill-a noiz erabili behar den erabakitzeko ikusten duena.

## 3. urratsa — Probatu

OpenCode-rekin:

> Erabili `@api-endpoint` skill-a. Gehitu `GET /tickets/{id}` endpoint bat, probekin eta dokumentazioarekin. Ez aldatu lehendik dauden testak.

Egiaztatu:

- Skill-a kargatu da?
- Urratsak jarraitu ditu?
- Probak sortu ditu?
- README eguneratu du?
- Diff-a txikia da?

## 4. urratsa — Hobetu

Idatzi:

| Zer falta zen? | Zer gehitu duzu? | Emaitza |
|---|---|---|
| | | |
| | | |

Adibidez: errore-kodeak, 404 kasua, Pydantic adibidea, testen izenak.

## Onarpen-checklista

- [ ] `.opencode/skills/api-endpoint/SKILL.md` sortuta.
- [ ] `name` eta `description` argiak.
- [ ] Noiz erabili, sarrerak, urratsak, checklista eta adibidea.
- [ ] OpenCode-rekin probatuta.
- [ ] Hobekuntza bat dokumentatuta.
- [ ] AA erregistroan jasota.

## Gogoeta

> Zergatik da hobea skill bat prompt luze bat itsastea baino? Noiz ez litzateke skill bat erabiliko?
