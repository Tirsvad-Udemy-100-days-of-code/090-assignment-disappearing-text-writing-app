[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

# Refleksi

## Cara projek ini didekati

Kerja mengikut proses rancang dahulu: Business Case, Analisis Pihak Berkepentingan, Pelan Projek dan empat pencapaian datang dahulu. Kemudian satu kes guna direka (model domain, rajah jujukan, rajah kelas) sebelum sebarang kod. Setiap pencapaian ialah satu cabang dan satu pull request. Peraturan yang memadam teks ditulis dahulu sebagai kelas Python biasa dengan ujian, dan Flask ditambah di atasnya.

## Apa yang sukar

- Memutuskan di mana pemasa berada. Pemasa dalam JavaScript cepat, tetapi tidak boleh diuji dengan pytest. Menyimpannya di pelayan menjadikan peraturan boleh diuji dan pelayar sekadar paparan mudah.
- Perlumbaan antara menaip dan tinjauan berkala: jawapan tinjauan lama boleh melaporkan teks telah dipadam sebaik penulis menaip huruf baharu. Skrip kini mengabaikan jawapan yang bermula sebelum tekanan kekunci terakhir.
- Mengekalkan dokumen, rajah dan kod selari apabila reka bentuk berubah (lapisan web direka hanya selepas teras siap).

## Apa yang mudah

- Peraturan itu sendiri: satu kelas dengan tiga kaedah kecil.
- Menguji dengan jam palsu: tiada ujian menunggu lima saat.
- Flask: kilang aplikasi, satu blueprint dan dua laluan sudah cukup.

## Apa yang perlu diperbaiki lain kali

- Uji skrip pelayar secara automatik. Kini hanya tangkapan skrin dari kontena menunjukkan ia berfungsi.
- Lukis wireframe dahulu dan semak dengan pembaca sebelum reka bentuk.
- Mulakan alat tangkapan skrin lebih awal, supaya setiap langkah ditangkap semasa dibina.

## Pembelajaran terbesar

Pastikan peraturan di luar rangka kerja. Apabila peraturan ialah kod biasa yang menerima masa sebagai nilai, ia mudah diuji dan lapisan web boleh kekal nipis.

## Apa yang akan saya lakukan secara berbeza

Menambah ujian hujung ke hujung kecil dalam kontena yang menaip, menunggu dan menyemak halaman, supaya tangkapan skrin menjadi hasil sampingan ujian dan bukan skrip berasingan.
