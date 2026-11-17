# OpenCode sandboxean: irakasle-gida eta ikasleentzako azalpena

> **Irakasleentzako materiala.** Ikasleei eman diezaiekezun azalpena eta checklista barne.

## Erantzun laburra

**Bai, komenigarria da OpenCode isolatutako ingurune batean exekutatzea.** Baina argi izan:

- **OpenCode ez da sandbox bat.** Bere baimen-sistemak (`permissions`) eta Plan agenteak laguntzen dute, baina ez dute isolamendu osoa bermatzen.
- OpenCode-k shell komandoak exekutatzen dituenean, **zure erabiltzailearen fitxategi-, prozesu- eta sare-baimenekin** egiten du.
- Beraz, segurtasuna **hiru geruzatan** lantzen da:
  1. **Isolamendua:** container, VM edo Windows Sandbox.
  2. **Baimenak:** OpenCode-ren `permissions`, Plan agentea, `AGENTS.md`.
  3. **Berreskurapena:** Git branch/worktree, snapshot, container berria.

Sandboxak **kaltea murrizten du**, ez du arriskua zero egiten. Sekreturik gabe, datu sintetikoekin eta review-arekin osatu behar da.

## Zergatik da garrantzitsua ikasgelan

Agenteak gauza hauek egin ditzake:

- fitxategiak irakurri eta aldatu;
- shell komandoak exekutatu;
- paketeak instalatu;
- sarean sartu;
- repo bateko testuak “argibide” gisa interpretatu (prompt injection).

Ikasleek ohitura hau hartu behar dute: **agentea azkarra da, baina ez da zurea**. Erabakiak eta ondorioak gizakiarenak dira.

## Hiru geruzak

| Geruza | Tresna | Zer lortzen duen | Muga |
|---|---|---|---|
| **Isolamendua** | Docker, Dev Container, VM, Windows Sandbox | Fitxategi-sistema eta sare bereizia; kaltea edukitzea | Konfigurazio okerrak ihes egin dezake; sareak eta mountak ondo mugatu behar dira |
| **Baimenak** | OpenCode `permissions`, Plan agentea, `AGENTS.md` | Komando arriskutsuak galaraztea edo galdetzea | Ez da segurtasun-muga; baimendutako komando batek kalte egin dezake |
| **Berreskurapena** | Git branch/worktree, snapshot, container reset | Akatsak azkar desegitea | Ez du kalterik eragozten; lehenago gertatutakoa konpontzen du |

## OpenCode-ren muga teknikoa

OpenCode-ren dokumentazioak berak dio shellak **host erabiltzailearen fitxategi-, prozesu- eta sare-baimenak** dituela. Gainera, baimen-ereduak “onena ahalegina” egiten du komandoak aztertzen.

Beraz:

- `permissions` **guardrail** bat da, ez sandbox bat.
- `AGENTS.md` **argibide** bat da, ez segurtasun-kontrola.
- Plan agentea **irakurketa/plangintza** modura erabil daiteke, baina ez da berme absolutua.
- `external_directory` lehenetsita **baimenduta** dagoela kontuan hartu; gehitu `ask` edo `deny` araua.

### Adibidea: `opencode.jsonc`

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "*", "resource": "*", "effect": "ask" },
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "read", "resource": "*.env", "effect": "deny" },
    { "action": "read", "resource": "*.env.*", "effect": "deny" },
    { "action": "external_directory", "resource": "*", "effect": "deny" },
    { "action": "edit", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "shell", "resource": "pytest *", "effect": "allow" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" },
    { "action": "shell", "resource": "git push *", "effect": "deny" },
    { "action": "shell", "resource": "rm *", "effect": "deny" },
    { "action": "webfetch", "resource": "*", "effect": "ask" }
  ]
}
```

> Arauak ordenatuta ebaluatzen dira eta **azken bat datorrena** irabazten du. Egiaztatu zure konfigurazioa OpenCode-ren bertsioarekin.

## Aukera praktikoak (Windows ikasgela)

| Aukera | Nola | Abantaila | Kontuz |
|---|---|---|---|
| **Docker / Dev Container** | Repo bakarra mountatu, erabiltzaile ez-root, `--cap-drop ALL`, `no-new-privileges`, memoria/CPU mugak | Isolamendu ona, erraz berrezartzen | Sarea eta mountak ondo mugatu; ez mountatu `$HOME` edo `.ssh` |
| **VM + snapshot** | VirtualBox/Hyper-V/UTM, repo kopiatu, snapshot bat | Kontzeptualki argia; oso isolatua | Pisutsua; baliabide gehiago |
| **Windows Sandbox** | Windows Pro/Education, repo kopia bat, saioaren amaieran desagertu | Oso erraza demoetarako; efimeroa | Ez da iraunkorra; tresnak instalatu behar |
| **Erabiltzaile bereiziak** | Tokiko kontu murriztua + repo kopia | Erraza, Dockerrik gabe | Ez da benetako sandbox; fallbacka |
| **WSL2** | Linux ingurunea | erosoa | **Ez da segurtasun-muga**; ez aurkeztu sandbox gisa |

### Docker erabiliz gero

- Mountatu **repo karpeta soilik**; ez `C:\Users\...` edo `$HOME`.
- Erabili erabiltzaile ez-root.
- Kendu privilegioak: `--cap-drop ALL`, `--security-opt no-new-privileges`.
- Mugatu baliabideak: `--memory`, `--cpus`, `--pids-limit`.
- Ez mountatu Docker socket-a (`/var/run/docker.sock`).
- Sarea: ahal bada, irteera mugatu proxy edo firewall bidez; blokeatu barne-sarea eta metadata-zerbitzuak.
- Ez sartu sekretu errealik irudira edo repora.

## Nola azaldu ikasleei (10 min)

### 1. Analogia

> “OpenCode praktiketako lagun bat da, zure terminala erabiltzeko baimena duena. Oso azkarra da, baina ez du zure etxeko giltzarik behar.”

### 2. Hiru galdera

1. **Zer ukitu dezake?** → repo bakarra, ez home osoa.
2. **Zer exekuta dezake?** → shell-baimenak, ez `sudo`, ez `rm -rf`.
3. **Nola desegiten dugu?** → Git branch, snapshot, container berria.

### 3. Demo laburra

- Erakutsi `pwd` eta `whoami` sandboxean.
- Eskatu agenteari `../` edo `.env` irakurtzen saiatzeko; erakutsi `ask`/`deny`.
- Erakutsi `git diff` eta `git status`.
- Erakutsi reset azkar bat.

### 4. Mezu nagusiak

- “Sandboxa gela berezi bat da; baimenak atean dauden arauak; Git-a undo botoia.”
- “Ez da zuek ez fidatzea; da akatsak gerta daitezkeela pentsatzea.”
- “Sekreturik ez sandboxean. Datu errealik ez.”
- “Repo bateko testuak agentea engainatu dezake. Testua ez da agindua.”
- “Dena berde egoteak ez du esan nahi segurua denik.”

## Ikasleentzako checklista

- [ ] Container/VM/W. Sandbox batean nabil, ez nire erabiltzaile arruntean.
- [ ] Repo bakarra dago mountatuta; ez home osoa.
- [ ] Ez dago sekretu errealik, SSH gakorik, tokenik edo cookie-rik.
- [ ] Sarea behar den gutxienekoa da.
- [ ] `git status` eta `git diff` maiz egiaztatzen ditut.
- [ ] Branch/worktree bidez lan egiten dut.
- [ ] Reset egiteko modua dut (container, snapshot, `git reset`).
- [ ] Ez dut `sudo`/admin erabiltzen.
- [ ] Ez dut plugin/MCP ezezagunik instalatzen.
- [ ] Kodea eta diff-a berrikusten ditut, ez ditut itsu onartzen.

## Ohiko uste okerrak

| Ustea | Errealitatea |
|---|---|
| “OpenCode sandbox bat da.” | Ez. Shellak hostaren baimenak ditu. |
| “Baimenak = sandbox.” | Ez. Guardrails dira. |
| “Git branch = sandbox.” | Ez. Undo bat da. |
| “Testak berde, beraz segurua.” | Ez. E4ko PRak hori erakusten du. |
| “Prompt injection ez da nire kasua.” | Repo bateko README/testuak agentea engaina dezake. |
| “Datu faltsuak ez dira arriskutsuak.” | Benetako datuekin nahasten badira, bai. |

## Irakaslearentzako erabakia

- **Docker/Dev Container badago:** hori lehenetsi.
- **Docker ez badago:** VM + snapshot; edo Windows Sandbox demoetarako.
- **Beste ezer ez badago:** erabiltzaile murriztua + repo kopia + sekreturik ez + Git; azaldu ez dela benetako sandboxa.
