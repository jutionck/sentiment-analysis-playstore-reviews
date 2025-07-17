# Proyek Analisis Sentimen Ulasan Aplikasi Ajaib

## Ringkasan Proyek

Proyek ini bertujuan untuk menganalisis sentimen dari ulasan pengguna aplikasi Ajaib yang diambil dari Google Play Store. Prosesnya dimulai dengan scraping data ulasan, kemudian data tersebut digunakan untuk melatih model deep learning yang mampu mengklasifikasikan sentimen ke dalam tiga kategori: positif, netral, dan negatif.

Model yang digunakan adalah Long Short-Term Memory (LSTM) yang dibangun menggunakan TensorFlow dan Keras. Notebook Jupyter `model_training.ipynb` mencakup semua langkah mulai dari pemrosesan data, pelatihan model, hingga evaluasi dan pengujian dengan data baru.

## Panduan Penggunaan

Panduan ini bertujuan untuk memberikan petunjuk penggunaan yang jelas dan mudah diikuti. Silakan ikuti langkah-langkah berikut:

### Langkah 1: Instalasi Dependensi

Pastikan Anda telah menginstal semua dependensi yang diperlukan. Gunakan perintah berikut untuk menginstal dependensi dari file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Langkah 2: Scraping Data

Untuk memulai, Anda perlu melakukan scraping data ulasan dari Google Play Store. Gunakan skrip berikut untuk mengumpulkan data yang diperlukan:

```bash
python scraping.py
```
Skrip ini akan menghasilkan file `ajaib.co.id_reviews.csv` yang berisi ulasan.

### Langkah 3: Menjalankan Model

Model dilatih dan dievaluasi menggunakan Jupyter Notebook. Setelah semua dependensi terinstal dan data telah di-scrape, jalankan notebook berikut:

```bash
jupyter notebook model_training.ipynb
```
Di dalam notebook, Anda dapat menjalankan setiap sel untuk melihat proses dari awal hingga akhir.