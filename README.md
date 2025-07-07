# 🧠 NeuroSort — Aplikasi Klasifikasi & Pencarian Dokumen Secara Lokal

**NeuroSort** adalah aplikasi pintar yang bisa mengklasifikasikan dokumen dan melakukan pencarian berdasarkan isi dokumen, semua dilakukan di komputer lokal kamu. Tanpa butuh internet, tanpa API key, dan tanpa risiko data bocor.

## 🔍 Apa yang Bisa Dilakukan

- Baca file `.txt`, `.pdf`, dan `.docx` dari folder lokal.
- Deteksi isi dokumen dan secara otomatis memberi kategori.
- Cari dokumen berdasarkan kata kunci atau kalimat yang kamu tulis.
- Simpan semua data metadata ke PostgreSQL.

## 🛠 Teknologi yang Dipakai

- Python (versi 3.10 ke atas)
- PostgreSQL (akses pakai pgAdmin 4)
- NLP pakai spaCy + TF-IDF dari scikit-learn
- Streamlit kalau mau antarmuka GUI

## 💡 Kenapa Dibuat

Kita sering punya banyak dokumen, tapi susah nyari yang kita butuh. Proyek ini bantu kamu cari dan kelola dokumen dengan sistem yang mirip pencarian pintar seperti Google Drive, tapi semuanya offline dan kamu yang punya kontrol penuh. Cocok lah yang peduli privasi dan ingin solusi praktis tapi canggih.
