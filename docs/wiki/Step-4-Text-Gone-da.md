[English](Step-4-Text-Gone) · **Dansk** · [Bahasa Malaysia](Step-4-Text-Gone-ms)

# Trin 4: Teksten er væk

![Teksten er væk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-4-text-gone.png)

Når der går mere end 5 sekunder uden skrivning, sletter serveren teksten. Det næste tilstandssvar siger `was_cleared`, editoren tømmes, og siden viser *Your text is gone. Start typing again.* Skriver du igen, starter en ny session.

## Hvad vi fik ud af det

- **En præcis regel.** "Mere end 5 sekunder" betyder, at præcis 5,0 beholder teksten og 5,001 sletter den; begge er tests.
- **En port til tid.** `Clock` er en `Protocol` i applikationslaget, og `SystemClock` (monoton tid) implementerer den, så tiden kan forfalskes.
- **Løbsbeskyttelse.** Scriptet ignorerer et pollsvar, der startede før det seneste tastetryk, og poller ikke, mens en afsendelse mangler svar, så nyskrevet tekst aldrig slettes af et gammelt svar.
- **End to end i en container.** Disse skærmbilleder er taget med en headless browser i Docker, så skrivebordet ikke blev brugt.
