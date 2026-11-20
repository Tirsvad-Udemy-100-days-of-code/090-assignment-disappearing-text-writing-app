[English](Step-2-Typing-With-Countdown) · [Dansk](Step-2-Typing-With-Countdown-da) · **Bahasa Malaysia**

# Langkah 2: Menaip dengan kira detik

![Menaip dengan kira detik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-2-typing-with-countdown.png)

Semasa penulis menaip, pelayar menghantar keseluruhan teks ke `POST /api/text` pada setiap perubahan. Pelayan menyimpan teks dan masa tekanan kekunci terakhir, dan halaman menunjukkan saat yang tinggal. Setiap tekanan kekunci memulakan semula kira detik pada 5.

## Apa yang diperoleh

- **Peraturan berada dalam Python.** `WritingSession.type_text(text, now)` menyimpan teks dan memulakan semula kira detik; masa diberi dari luar, jadi tiada jam diperlukan untuk menguji.
- **Keadaan di pelayan.** Pelayan menentukan keadaan, jadi pelayar dan pelayan tidak boleh bercanggah (lihat ADR-0002).
- **Kes guna.** `TypeText` dan `GetWritingState` membawa dua operasi sistem dari lapisan web ke sesi.
- **Ujian dengan jam palsu.** Tingkah laku diuji tanpa menunggu lima saat sebenar.
