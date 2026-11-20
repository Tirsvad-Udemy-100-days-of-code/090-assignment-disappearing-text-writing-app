**English** · [Dansk](Step-3-Warning-Last-Seconds-da) · [Bahasa Malaysia](Step-3-Warning-Last-Seconds-ms)

# Step 3: Warning in the last seconds

![The warning in the last seconds](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-3-warning-last-seconds.png)

In the last 2 seconds the countdown turns red and the page says *keep writing*. The browser asks `GET /api/state` every 200 milliseconds and shows what the server answers.

## What was gained

- **A flag, not a guess.** The server answers `is_warning`, so the rule "warn at 2 seconds left" (`WARNING_THRESHOLD_SECONDS`) exists once.
- **State as CSS classes.** The page switches between `state-empty`, `state-typing`, `state-warning` and `state-gone`, so style and behaviour stay apart.
- **A view model.** `WritingViewModel` gives the template its plain values; no domain object reaches the page.
- **Polling.** A small script and a JSON route are enough, so Flask stays the only dependency.
