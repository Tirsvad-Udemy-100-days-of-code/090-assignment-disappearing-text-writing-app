[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Du skal bruge Python 3.13 eller nyere. Flask er den eneste kørselsafhængighed; pytest og de øvrige værktøjer kommer med `dev`-tillægget.

## Opret og brug et lokalt virtuelt miljø

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

Forlad miljøet med `deactivate`.

## Kør

```bash
python -m disappearing_text
```

Åbn <http://127.0.0.1:5000> og begynd at skrive. Hold pause i mere end 5 sekunder, og teksten er væk.

## Test

```bash
python -m pytest
```

## Hvad vi fik ud af det

En gentagelig opsætning: alle kan klone repositoriet, oprette et `.venv` og få samme resultat. Projektets indstillinger ligger i `pyproject.toml`, så der er ingen skjult konfiguration.
