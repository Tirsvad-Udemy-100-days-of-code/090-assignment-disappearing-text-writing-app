[English](Step-2-Typing-With-Countdown) · **Dansk** · [Bahasa Malaysia](Step-2-Typing-With-Countdown-ms)

# Trin 2: Skrivning med nedtælling

![Skrivning med nedtælling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-2-typing-with-countdown.png)

Mens skribenten skriver, sender browseren hele teksten til `POST /api/text` ved hver ændring. Serveren husker teksten og tidspunktet for det sidste tastetryk, og siden viser de resterende sekunder. Hvert tastetryk starter nedtællingen forfra ved 5.

## Hvad vi fik ud af det

- **Reglen bor i Python.** `WritingSession.type_text(text, now)` gemmer teksten og genstarter nedtællingen; tiden gives udefra, så der ikke skal bruges et ur i testen.
- **Tilstand på serveren.** Serveren afgør, hvad tilstanden er, så browser og server ikke kan være uenige (se ADR-0002).
- **Use cases.** `TypeText` og `GetWritingState` fører de to systemoperationer fra weblaget til sessionen.
- **Tests med falsk ur.** Adfærden testes uden at vente fem rigtige sekunder.
