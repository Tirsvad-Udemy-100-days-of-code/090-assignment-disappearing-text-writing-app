**English** · [Dansk](Step-1-Empty-Editor-da) · [Bahasa Malaysia](Step-1-Empty-Editor-ms)

# Step 1: Empty editor

![The empty editor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-1-empty-editor.png)

The page opens with an empty editor and the text *Start typing. Your text disappears if you stop for more than 5 seconds.* No countdown shows yet, because the countdown only runs while there is text. Flask serves this page from `GET /`.

## What was gained

- **Layers.** The code is split in `domain`, `application`, `infrastructure` and `presentation`, and imports only point inward. A check with import-linter keeps it so.
- **One place for constants.** The 5 seconds is `IDLE_TIMEOUT_SECONDS` in `constants.py`.
- **App factory.** `create_app()` builds the Flask app, so tests can start it with a fake clock.
- **Plan first.** The use case, its diagrams and a wireframe were written and reviewed before the code.
