[English](Step-3-Warning-Last-Seconds) · [Dansk](Step-3-Warning-Last-Seconds-da) · **Bahasa Malaysia**

# Langkah 3: Amaran pada saat terakhir

![Amaran pada saat terakhir](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-3-warning-last-seconds.png)

Dalam 2 saat terakhir kira detik bertukar merah dan halaman menyatakan *keep writing*. Pelayar bertanya `GET /api/state` setiap 200 milisaat dan memaparkan jawapan pelayan.

## Apa yang diperoleh

- **Bendera, bukan tekaan.** Pelayan menjawab `is_warning`, jadi peraturan "beri amaran pada baki 2 saat" (`WARNING_THRESHOLD_SECONDS`) wujud di satu tempat.
- **Keadaan sebagai kelas CSS.** Halaman bertukar antara `state-empty`, `state-typing`, `state-warning` dan `state-gone`, supaya gaya dan tingkah laku berasingan.
- **Model paparan.** `WritingViewModel` memberi templat nilai biasa; tiada objek domain sampai ke halaman.
- **Tinjauan berkala.** Skrip kecil dan laluan JSON sudah memadai, jadi Flask kekal satu-satunya kebergantungan.
