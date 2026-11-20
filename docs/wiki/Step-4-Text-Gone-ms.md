[English](Step-4-Text-Gone) · [Dansk](Step-4-Text-Gone-da) · **Bahasa Malaysia**

# Langkah 4: Teks hilang

![Teks telah hilang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/090-assignment-disappearing-text-writing-app/raw/branch/main/docs/images/step-4-text-gone.png)

Apabila lebih daripada 5 saat berlalu tanpa menaip, pelayan memadam teks. Jawapan keadaan seterusnya menyatakan `was_cleared`, editor dikosongkan dan halaman memaparkan *Your text is gone. Start typing again.* Menaip semula memulakan sesi baharu.

## Apa yang diperoleh

- **Peraturan tepat.** "Lebih daripada 5 saat" bermaksud tepat 5.0 mengekalkan teks dan 5.001 memadamnya; kedua-duanya ialah ujian.
- **Port untuk masa.** `Clock` ialah `Protocol` dalam lapisan aplikasi dan `SystemClock` (masa monotonik) melaksanakannya, jadi masa boleh dipalsukan.
- **Perlindungan perlumbaan.** Skrip mengabaikan jawapan tinjauan yang bermula sebelum tekanan kekunci terakhir dan tidak meninjau semasa penghantaran belum dijawab, supaya teks yang baru ditaip tidak dipadam oleh jawapan lama.
- **Hujung ke hujung dalam kontena.** Tangkapan skrin ini diambil dengan pelayar tanpa kepala dalam Docker, jadi desktop tidak digunakan.
