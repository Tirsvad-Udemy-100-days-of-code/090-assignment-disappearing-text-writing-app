**English** · [Dansk](Step-2-Typing-With-Countdown-da) · [Bahasa Malaysia](Step-2-Typing-With-Countdown-ms)

# Step 2: Typing with countdown

![Typing with the countdown](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-2-typing-with-countdown.png)

While the writer types, the browser sends the whole text to `POST /api/text` on every change. The server keeps the text and the time of the last key press, and the page shows the seconds left. Every key press restarts the countdown at 5.

## What was gained

- **The rule lives in Python.** `WritingSession.type_text(text, now)` stores the text and restarts the countdown; time is passed in, so no clock is needed to test it.
- **Server-side state.** The server decides what the state is, so the browser and the server cannot disagree (see ADR-0002).
- **Use cases.** `TypeText` and `GetWritingState` carry the two system operations from the web layer to the session.
- **Tests with a fake clock.** The behaviour is tested without waiting five real seconds.
