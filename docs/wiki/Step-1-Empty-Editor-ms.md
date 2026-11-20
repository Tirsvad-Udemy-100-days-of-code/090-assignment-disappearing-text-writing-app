[English](Step-1-Empty-Editor) · [Dansk](Step-1-Empty-Editor-da) · **Bahasa Malaysia**

# Langkah 1: Editor kosong

![Editor kosong](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-1-empty-editor.png)

Halaman dibuka dengan editor kosong dan teks *Start typing. Your text disappears if you stop for more than 5 seconds.* Belum ada kira detik kerana kira detik hanya berjalan apabila ada teks. Flask menyajikan halaman ini dari `GET /`.

## Apa yang diperoleh

- **Lapisan.** Kod dibahagi kepada `domain`, `application`, `infrastructure` dan `presentation`, dan import hanya menuju ke dalam. Semakan import-linter mengekalkannya.
- **Satu tempat untuk pemalar.** 5 saat ialah `IDLE_TIMEOUT_SECONDS` dalam `constants.py`.
- **Kilang aplikasi.** `create_app()` membina aplikasi Flask, supaya ujian boleh memulakannya dengan jam palsu.
- **Rancang dahulu.** Kes guna, rajahnya dan wireframe ditulis dan disemak sebelum kod.
