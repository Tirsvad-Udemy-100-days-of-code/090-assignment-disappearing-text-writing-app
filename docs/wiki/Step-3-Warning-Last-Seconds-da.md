[English](Step-3-Warning-Last-Seconds) · **Dansk** · [Bahasa Malaysia](Step-3-Warning-Last-Seconds-ms)

# Trin 3: Advarsel i de sidste sekunder

![Advarslen i de sidste sekunder](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-3-warning-last-seconds.png)

I de sidste 2 sekunder bliver nedtællingen rød, og siden siger *keep writing*. Browseren spørger `GET /api/state` hver 200. millisekund og viser det, serveren svarer.

## Hvad vi fik ud af det

- **Et flag, ikke et gæt.** Serveren svarer `is_warning`, så reglen "advar ved 2 sekunder tilbage" (`WARNING_THRESHOLD_SECONDS`) findes ét sted.
- **Tilstand som CSS-klasser.** Siden skifter mellem `state-empty`, `state-typing`, `state-warning` og `state-gone`, så udseende og adfærd holdes adskilt.
- **En view-model.** `WritingViewModel` giver skabelonen almindelige værdier; intet domæneobjekt når siden.
- **Polling.** Et lille script og en JSON-rute er nok, så Flask forbliver den eneste afhængighed.
