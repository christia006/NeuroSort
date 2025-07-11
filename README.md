<div align="center">

# **🧠 NeuroSort — Smart Local Document Classification & Search**

*Read, understand, and classify documents directly on your PC — no internet, no API keys, no privacy risk.*

[![last commit](https://img.shields.io/badge/last%20commit-today-brightgreen)](#)
[![Python](https://img.shields.io/badge/python-100%25-yellow?logo=python&logoColor=white)](#)
[![local AI](https://img.shields.io/badge/runs%20locally-100%25-success)](#)

*Built with the tools and technologies:*

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-00A6E8?logo=spacy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-f7931e?logo=scikit-learn&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-d74e09?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Optional%20UI-ff4b4b?logo=streamlit&logoColor=white)

![Local AI](https://img.shields.io/badge/Local%20AI%20Model-💻-important)
![Fast Search](https://img.shields.io/badge/Fast%20TF--IDF%20Search-⚡-success)
![Private](https://img.shields.io/badge/Privacy%20First-🔒-blue)

</div>


## 🔄 Cara Kerja Program

1. 📂 **Pemindaian Dokumen Lokal**  
   Sistem membaca semua file `.txt`, `.pdf`, dan `.docx` dari folder `data/sample_documents/`.

2. 🧹 **Preprocessing Teks**  
   - Tokenisasi kata dan kalimat menggunakan spaCy  
   - Menghapus stopwords, simbol, dan kata tidak penting

3. 🧠 **Klasifikasi & Pemberian Label Otomatis**  
   - Menggunakan TF-IDF untuk memahami konteks isi  
   - Sistem menentukan label/kategori dokumen secara otomatis

4. 🔍 **Pencarian Kontekstual**  
   - Ketika pengguna mengetik query seperti “language understanding technology”, sistem akan mencocokkan konten dokumen dengan query  
   - Mengembalikan hasil berdasarkan skor kemiripan (cosine similarity)

5. 🗂️ **Penyimpanan Metadata ke PostgreSQL**  
   Semua informasi—judul, isi, label, skor pencarian, tanggal dibaca—disimpan untuk efisiensi akses di masa mendatang.

---


## 🖼️ Visualisasi Program

| Tahapan | Gambar |
|--------|--------|
| 💡 Konsep Kecerdasan Buatan | ![](image/ai%20concept.png) |
| 📊 Teknik Analisis Data | ![](image/data%20analysis%20teknik.png) |
| 🌐 Panduan Pengembangan Web | ![](image/website%20development%20guide.png) |
| 🔐 Jaringan & Proteksi Data | ![](image/network%20dan%20data.png) |
| 🌐 Pemahaman Bahasa | ![](image/languange%20understanding.png) |
| 🧠 Arsitektur Pemrosesan | ![](image/common.png) |
| 🚪 Keluar atau Simpan Hasil | ![](image/exit.png) |
| 🔁 Proses Perubahan & Ekstraksi | ![](image/change.png) |
| 🗃️ Struktur Database | ![](image/databases.png) |
| 📋 Tampilan Isi Tabel PostgreSQL | ![](image/tampilan%20isi%20tabel%20document.png) |


---
@christian J Hutahaean

