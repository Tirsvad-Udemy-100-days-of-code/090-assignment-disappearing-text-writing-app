[English](Step-1-Empty-Editor) · **Dansk** · [Bahasa Malaysia](Step-1-Empty-Editor-ms)

# Trin 1: Tom editor

![Den tomme editor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-1-empty-editor.png)

Siden åbner med en tom editor og teksten *Start typing. Your text disappears if you stop for more than 5 seconds.* Der vises endnu ingen nedtælling, fordi nedtællingen kun kører, mens der er tekst. Flask leverer siden fra `GET /`.

## Hvad vi fik ud af det

- **Lag.** Koden er delt i `domain`, `application`, `infrastructure` og `presentation`, og importer peger kun indad. En kontrol med import-linter holder det sådan.
- **Ét sted til konstanter.** De 5 sekunder er `IDLE_TIMEOUT_SECONDS` i `constants.py`.
- **App-fabrik.** `create_app()` bygger Flask-appen, så tests kan starte den med et falsk ur.
- **Plan først.** Use casen, dens diagrammer og en wireframe blev skrevet og gennemgået før koden.
