# Ketentuan Proyek Eksperimen SML

Kita gas Kriteria 1 dulu. Target kita langsung sikat sampai level Advanced (4 poin) biar alur pipeline-nya solid. Inti dari tahap ini adalah ngubah proses preprocessing yang awalnya manual di notebook jadi otomatis pakai script dan jalan di GitHub Actions. Kebiasaan merancang arsitektur sistem yang terpisah antara antarmuka dan mesin pemrosesan bakal kepakai banget buat mahamin konsep otomatisasi di sini.

Berikut step-by-step eksekusinya:

## 1. Siapkan Struktur Folder & Repositori
Bikin repositori GitHub baru dengan visibilitas Public agar bisa diperiksa oleh tim reviewer. Di direktori lokalmu, bikin folder utama (misalnya pakai username kamu naumi atau mpay1) dengan struktur wajib seperti ini:

```text
Eksperimen_SML_naumi/
├── .github/
│   └── workflows/
│       └── preprocessing.yml
├── namadataset_raw/
│   └── data_mentah.csv
├── preprocessing/
│   ├── Eksperimen_naumi.ipynb
│   └── automate_naumi.py
└── namadataset_preprocessing/
    └── data_bersih.csv
```

## 2. Selesaikan Level Basic (Notebook)
Buka file `Eksperimen_naumi.ipynb` di folder `preprocessing`. Di sini kamu wajib menggunakan Template Eksperimen MSML dari Dicoding sebagai kerangka dasarnya. Pastikan notebook kamu dijalankan tanpa error dan mencakup tiga hal ini:

*   **Data Loading**: Tarik data dari folder `namadataset_raw`.
*   **EDA (Exploratory Data Analysis)**: Cek distribusi, visualisasi, korelasi, dll.
*   **Preprocessing**: Lakukan pembersihan data, encoding, scaling, dll.

## 3. Naik ke Level Skilled (Script Automasi)
Setelah notebook-nya aman, kita konversi proses preprocessing tadi jadi kode modular. Buka `automate_naumi.py` dan buat fungsi Python yang isinya adalah langkah-langkah pembersihan data persis seperti yang kamu lakukan di notebook. Pastikan script ini menghasilkan dan menyimpan data yang sudah siap latih ke folder `namadataset_preprocessing`.

## 4. Tembus Level Advanced (GitHub Actions)
Kita bikin supaya setiap kali ada perubahan yang di-push ke GitHub, script `automate_naumi.py` jalan sendiri. Buka file `.github/workflows/preprocessing.yml` dan isi dengan konfigurasi GitHub Actions. Pastikan workflow ini di-setting agar setelah preprocessing selesai, sistem akan mengembalikan atau melakukan commit dataset terbaru yang sudah diproses kembali ke repositorimu.

Kalau kamu udah push semua struktur di atas ke GitHub dan Actions-nya sukses berjalan tanpa error, Kriteria 1 udah aman.
