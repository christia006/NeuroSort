# 🧠 NeuroSort — Mesin Klasifikasi dan Pencarian Dokumen Lokal Berbasis NLP

**NeuroSort** adalah aplikasi klasifikasi dokumen pintar dan mesin pencarian semantik yang berjalan sepenuhnya secara lokal. Dengan bantuan teknik NLP dan machine learning, NeuroSort mampu mengklasifikasikan serta mencari dokumen berdasarkan isi secara kontekstual — tanpa koneksi internet, tanpa API key, dan tanpa kompromi privasi.

## 🎯 Tujuan Proyek

- Membuat sistem klasifikasi dokumen otomatis berbasis konten menggunakan NLP (spaCy, TF-IDF).
- Menyediakan fitur pencarian semantik berbasis vektorisasi dan cosine similarity.
- Menyimpan metadata dokumen (nama file, kategori, path, tanggal) secara terstruktur di PostgreSQL.
- Mendemonstrasikan kemampuan software engineer dalam membangun pipeline NLP dan integrasi database secara skalabel dan modular.

## 🧩 Fitur Utama

- Input dokumen: `.txt`, `.pdf`, `.docx` dari folder lokal.
- Klasifikasi otomatis: dokumen diklasifikasikan ke topik/topik utama berdasarkan isi.
- Pencarian cerdas: ketikkan pertanyaan atau kata kunci dan temukan dokumen relevan.
- Penyimpanan metadata di PostgreSQL (terhubung via SQLAlchemy).
- Antarmuka berbasis CLI atau Streamlit (opsional GUI).

## 🛠️ Teknologi yang Digunakan

- Python 3.10+
- spaCy · scikit-learn · SQLAlchemy
- PostgreSQL (dikelola via pgAdmin 4)
- Streamlit (opsional untuk antarmuka)

## 📌 Mengapa Proyek Ini Relevan dengan Google

Google adalah perusahaan yang sangat fokus pada pengelolaan dan pencarian informasi. **NeuroSort** meniru arsitektur dasar mesin pencari internal Google (seperti Gmail Search atau Google Drive Smart Search), namun sepenuhnya dijalankan secara lokal. Proyek ini mencerminkan:

- Pemikiran sistemik
- Privasi pengguna
- Arsitektur modular dan skalabel
