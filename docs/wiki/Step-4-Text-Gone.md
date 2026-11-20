**English** · [Dansk](Step-4-Text-Gone-da) · [Bahasa Malaysia](Step-4-Text-Gone-ms)

# Step 4: Text gone

![The text is gone](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-4-text-gone.png)

When more than 5 seconds pass without typing, the server deletes the text. The next state answer says `was_cleared`, the editor is emptied and the page shows *Your text is gone. Start typing again.* Typing again starts a new session.

## What was gained

- **An exact rule.** "More than 5 seconds" means exactly 5.0 keeps the text and 5.001 deletes it; both are tests.
- **A port for time.** `Clock` is a `Protocol` in the application layer and `SystemClock` (monotonic time) implements it, so time can be faked.
- **A race guard.** The script ignores a poll answer that started before the latest key press and does not poll while a send is unanswered, so freshly typed text is never erased by an old answer.
- **End to end in a container.** These screenshots were taken with a headless browser in Docker, so the desktop was not used.
