**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

You need Python 3.13 or newer. Flask is the only runtime dependency; pytest and the other tools come with the `dev` extra.

## Create and use a local virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## Run

```bash
python -m disappearing_text
```

Open <http://127.0.0.1:5000> and start typing. Stop for more than 5 seconds and the text is gone.

## Test

```bash
python -m pytest
```

## What was gained

A repeatable setup: anyone can clone the repository, create a `.venv`, and have the same result. The project settings live in `pyproject.toml`, so there is no hidden configuration.
