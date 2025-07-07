# 🧠 NeuroSort — Klasifikasi & Pencarian Dokumen Cerdas Berbasis AI Lokal

**NeuroSort** adalah aplikasi AI lokal yang dapat membaca, memahami, mengklasifikasikan, dan mencari dokumen berbasis isi langsung dari komputer pribadi, tanpa koneksi internet, tanpa API key, dan tanpa risiko privasi.

---

# 🎯 Contoh Kasus Nyata 



| **Domain**              | **Studi Kasus**                                                                                             | **Solusi dengan NeuroSort**                                                                                                                                          |
|--------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Hukum & Legal**        | Firma hukum ingin mencari dokumen kontrak berdasarkan konteks isi, bukan hanya judul atau kata kunci        | NeuroSort mengindeks dokumen kontrak menggunakan TF-IDF dan spaCy, memungkinkan pencarian semantik seperti "klausul kerahasiaan" meskipun tidak disebutkan eksplisit |
| **Perusahaan Riset**     | Peneliti ingin mengelompokkan ribuan file laporan ilmiah sesuai bidang (misal, bioteknologi, AI, dsb)       | Sistem klasifikasi NeuroSort mengklasifikasikan dokumen secara otomatis berdasarkan kemiripan semantik dan metadata yang disimpan di PostgreSQL                     |
| **Pendidikan**           | Dosen ingin mencari materi kuliah lama yang membahas topik tertentu meskipun judul file tidak jelas         | Dengan pencocokan konteks isi dokumen, dosen dapat mengetik query seperti "penjelasan supervised learning" dan sistem akan mencocokkan file yang relevan             |
| **Media & Arsip**        | Editor majalah ingin mengelola arsip artikel lama dengan pengelompokan otomatis                             | NeuroSort menyortir dan mengklasifikasikan artikel ke dalam topik-topik utama (politik, kesehatan, teknologi, dll.) untuk memudahkan pencarian                      |
| **Organisasi Pemerintah**| Pegawai ingin mencari notulen rapat yang relevan dengan suatu kebijakan                                     | Sistem memungkinkan pencarian cerdas seperti "kebijakan subsidi pendidikan" tanpa harus menelusuri semua dokumen satu per satu                                      |


---

## ⚙️ Teknologi Inti

- **Python 3.10+**
- **spaCy** untuk NLP
- **scikit-learn (TF-IDF)** untuk representasi isi dokumen
- **PostgreSQL + SQLAlchemy** untuk penyimpanan data
- **Streamlit** (opsional) untuk antarmuka visual

---

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

## 🔍 Contoh Pencarian & Hasil yang Diharapkan

| 💬 Query                          | 🔎 Hasil yang Diharapkan                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------|
| **artificial intelligence concepts**  | Dokumen seperti *NLP Basics*, *Machine Learning Overview* akan muncul teratas            |
| **data analysis techniques**         | Dokumen tentang *Data Science*, *Machine Learning*                                       |
| **website development guide**       | Dokumen seperti *Web Development Basics* paling relevan                                  |
| **network and data protection**     | *Cybersecurity Fundamentals* akan jadi prioritas utama                                   |
| **language understanding technology** | *NLP Basics* harus muncul paling relevan                                                 |
| **common cyber threats**            | *Cybersecurity Fundamentals* akan muncul kembali di posisi teratas                       |

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


