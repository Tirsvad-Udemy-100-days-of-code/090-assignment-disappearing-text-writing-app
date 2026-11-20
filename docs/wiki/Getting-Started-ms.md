[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

Anda memerlukan Python 3.13 atau lebih baharu. Flask ialah satu-satunya kebergantungan masa jalan; pytest dan alat lain datang dengan tambahan `dev`.

## Cipta dan guna persekitaran maya setempat

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

Keluar dari persekitaran dengan `deactivate`.

## Jalankan

```bash
python -m disappearing_text
```

Buka <http://127.0.0.1:5000> dan mula menaip. Berhenti lebih daripada 5 saat dan teks akan hilang.

## Uji

```bash
python -m pytest
```

## Apa yang diperoleh

Persediaan yang boleh diulang: sesiapa sahaja boleh mengklon repositori, mencipta `.venv` dan mendapat hasil yang sama. Tetapan projek berada dalam `pyproject.toml`, jadi tiada konfigurasi tersembunyi.
