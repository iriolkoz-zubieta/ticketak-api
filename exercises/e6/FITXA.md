# E6 — Agenteak: anatomia eta kontrola

**Saioa:** 5 · **Iraupena:** 85 min (A: 30 min, B: 55 min) · **Modua:** bikoteka  
**Entregagarria:** `AGENTS.md`, exekuzio-log-a eta konparaketa laburra

**Izena:** ______________________________  **Taldea:** ______________  **Data:** __________

---

## Helburua

Agente bat ez dela magia ulertzea: **LLM + tresnak + begizta + egoera + baimenak**. Gero, OpenCode agente gisa gainbegiratuta erabiltzea eta `AGENTS.md` bidez mugak ezartzea.

---

# A zatia — Agente baten anatomia (30 min)

## 1. urratsa — Begizta irakurri

```python
def run_agent(goal, tools, max_steps=5):
    messages = [
        {"role": "system", "content": "Helburua lortu tresnak erabiliz."},
        {"role": "user", "content": goal},
    ]
    for step in range(max_steps):
        action = llm(messages, tools)  # {"tool": "...", "args": {...}}
        if action["tool"] == "finish":
            return action["args"]["answer"]
        result = tools[action["tool"]](**action["args"])
        messages.append({"role": "assistant", "content": str(action)})
        messages.append({"role": "tool", "content": str(result)})
    raise RuntimeError("Gehienezko urratsak gainditu dira")
```

Marraztu begizta:

```text
helburua → plana → tresna → behaketa → hurrengo urratsa → ...
```

## 2. urratsa — Tresna bat gehitu

Gehitu `count_lines(path)` tresna: fitxategi bateko lerro-kopurua itzultzen du.

- Probaldu fitxategi batekin.
- Egiaztatu tresna-eskeman agertzen dela.
- Ez gehitu tresna arriskutsurik.

## 3. urratsa — Guardrail bat

Gehitu guardrail bat: `write_file` **debekatuta** `tests/` direktorioan.

- Probaldu guardrailak ukatzen duela.
- Idatzi zer gertatzen den guardrailik gabe.

## A zatia — Onarpena

- [ ] Begizta marraztuta.
- [ ] `count_lines` funtzionatzen du.
- [ ] Guardrailak `tests/` idazketa ukatzen du.
- [ ] Agentearen urratsak azaltzeko gai.

---

# B zatia — Agentea OpenCode-rekin (55 min)

## 1. urratsa — Brancha prestatu

Irakasleak `agent-bug` brancha emango du. Bertan:

- `GET /tickets?status=` balio okerrarekin `500` itzultzen du;
- proba bat falta da;
- balidazioa osatu gabe dago.

```bash
git fetch
git switch agent-bug
git status
```

## 2. urratsa — Mugarik gabe

1. Ireki OpenCode repoaren erroan.
2. Aukeratu **Plan** agenta; eskatu plana:

> Konpondu `GET /tickets?status=` bug-a. Azaldu plana; ez aldatu ezer oraindik.

3. Irakurri plana. Ondoren, aukeratu **Build** agenta eta exekutatu.
4. Gorde:

```bash
git diff --stat
git diff
pytest -q
```

| Metrika | Mugarik gabe |
|---|---|
| Aldatutako fitxategiak | |
| Gehitu/kendutako lerroak | |
| Testak berde? | |
| Denbora | |
| Kostua (gutxi gorabehera) | |
| Aldaketa erlazionatugabeak? | |

## 3. urratsa — Mugekin

Idatzi `AGENTS.md` arau hauekin (edo osatu lehendik dagoena):

- Exekutatu `pytest -q` amaitu aurretik.
- Ez aldatu testak baimenik gabe.
- Ez gehitu dependendentzia berririk baimenik gabe.
- Ezabatu aurretik galdetu.
- Mantendu diff-a txikia eta erlazionatua.
- Ez commit-atu sekreturik.

Berrezarri brancha:

```bash
git reset --hard HEAD
git clean -fd   # untracked fitxategiak ezabatzen ditu; ziurtatu ezer gorde gabe
```

Errepikatu 2. urratsa, orain `AGENTS.md`-rekin. Bete taula:

| Metrika | Mugekin |
|---|---|
| Aldatutako fitxategiak | |
| Gehitu/kendutako lerroak | |
| Testak berde? | |
| Denbora | |
| Kostua (gutxi gorabehera) | |
| Aldaketa erlazionatugabeak? | |

## 4. urratsa — Konparatu

Idatzi 5–8 lerro:

- Zein da aldea?
- Zer arazo ekidin ditu `AGENTS.md`-k?
- Zer egin du agenteak gaizki?
- Noiz behar duzu giza esku-hartzea?

## B zatia — Onarpena

- [ ] Bi exekuzioak egin dira (mugarik gabe / mugekin).
- [ ] `AGENTS.md` arrazoitua.
- [ ] Diffak eta testak erregistratuta.
- [ ] Konparaketa idatzita.
- [ ] AA erregistroan jasota.

---

## Gogoeta

> Agentea azkarra da, baina ez da zurea. Zer da zure erantzukizuna agenteak egindako aldaketen aurrean?
