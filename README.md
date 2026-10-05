# Kumpulan Praktikum Komputasi Big Data / Kecerdasan Buatan (NVIDIA DGX)

Repositori ini berisi kumpulan notebook Jupyter yang saya kerjakan untuk mata kuliah
**Praktikum Unggulan Universitas Gunadarma** (dikenal juga sebagai *Praktikum DGX*), mencakup
dua semester:

| Semester | Mata Kuliah | Topik |
|---|---|---|
| 2 | Praktikum Teknologi Kecerdasan Artifisial (Tingkat 1) | NumPy, perbandingan CPU vs GPU, game, YOLO, image processing |
| 3 | Praktikum Komputasi Big Data (Tingkat 2) | Dasar statistik dan analisis data dengan Python |

Semua notebook sudah **lengkap dengan output** (hasil eksekusi ikut tersimpan),
sehingga bisa langsung dibaca tanpa harus menjalankan ulang.

---

## Daftar Isi

1. [Apa Itu Praktikum DGX?](#apa-itu-praktikum-dgx)
2. [Dua Moda Pelaksanaan](#dua-moda-pelaksanaan)
3. [Cara Menjalankan Notebook (UNTUK PEMULA)](#cara-menjalankan-notebook-untuk-pemula)
4. [Daftar Library yang Dibutuhkan](#daftar-library-yang-dibutuhkan)
5. [Struktur Folder](#struktur-folder)
6. [Daftar Praktikum per Pertemuan](#daftar-praktikum-per-pertemuan)
7. [Cara Mengumpulkan Tugas](#cara-mengumpulkan-tugas)
8. [Referensi Resmi](#referensi-resmi)
9. [Troubleshooting](#troubleshooting)

---

## Apa Itu Praktikum DGX?

Universitas Gunadarma menyediakan mesin **superkomputer** yang bisa dipakai seluruh mahasiswa:

| Mesin | GPU | Memori | Keterangan |
|---|---|---|---|
| **NVIDIA DGX-1** | 8 GPU | 16 GB per GPU | 56x lebih baik dari CPU |
| **NVIDIA DGX A100** | 8 GPU | total 320 GB, 6 NVSwitch | 172x lebih cepat dari CPU server |

Tujuan praktikum ini adalah supaya mahasiswa bisa **langsung memakai** mesin tersebut untuk
mengerjakan proyek Big Data, Data Analytics, dan Artificial Intelligence.

---

## Dua Moda Pelaksanaan

Praktikum dijadwalkan **8 kali pertemuan**, dibagi rata antara dua moda:

| Moda | Penjelasan | Kebutuhan |
|---|---|---|
| **HANDS-ON** | Mengakses langsung mesin DGX milik UG | Login ke server DGX (NPM + password studentsite) |
| **SELF STUDY** |MANDIRI menggunakan perangkat pribadi | Laptop sendiri + Python |

**Jadwal sesi** (Senin–Sabtu, masing-masing 2 jam):

| Sesi | Waktu |
|---|---|
| 1 | 07.30 – 09.30 WIB |
| 2 | 09.30 – 11.30 WIB |
| 3 | 12.30 – 14.30 WIB |
| 4 | 14.30 – 16.30 WIB |
| 5 (kelas malam) | 17.30 – 19.30 WIB |

---

## Cara Menjalankan Notebook (UNTUK PEMULA)

Bagian ini.step-by-step. Ikuti urutan dari atas ke bawah, jangan lompat-lompat.

### Prasyarat

Pastikan sudah terinstall:

- **[Python 3.10 ke atas](https://www.python.org/downloads/)** — cek dengan mengetik `python --version` di terminal
- **[Git](https://git-scm.com/downloads)** — untuk mendownload repo ini (opsional, bisa pakai tombol *Code → Download ZIP* di GitHub)

### Langkah 1 — Cek Python sudah ada

Buka **Command Prompt** (Windows) atau **Terminal** (Mac/Linux), lalu ketik:

```bash
python --version
```

Kalau muncul seperti `Python 3.13.5`, berarti sudah siap. Kalau muncul error, install dulu lewat
link di atas, lalu **tutup dan buka ulang terminal**.

### Langkah 2 — Masuk ke folder repositori

Kalau mau pakai Git:

```bash
git clone https://github.com/Dickybulin26/kuliah_praktikum_superkomputer_NVIDIADGXA100.git
cd kuliah_praktikum_superkomputer_NVIDIADGXA100
```

Kalau tidak punya Git, unduh ZIP dari tombol hijau **Code → Download ZIP** di halaman GitHub,
lalu extract (klik kanan → *Extract Here*), lalu `cd` ke folder hasil extract.

### Langkah 3 — Buat virtual environment

Virtual environment adalah "kotak terpisah" khusus untuk Python proyek ini, supaya
library yang diinstall tidak mencampur dengan program lain di laptop.

Di dalam folder repositori, jalankan:

```bash
python -m venv .venv
```

Lalu **aktifkan** virtual environment:

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

Kalau aktif, akan muncul tanda `(.venv)` di awal baris terminal:

```
(.venv) C:\Users\...\kuliah_praktikum_superkomputer_NVIDIADGXA100>
```

### Langkah 4 — Install Jupyter dan library yang diperlukan

Masih di terminal yang sama (yang sudah aktif), jalankan:

```bash
pip install jupyter notebook pandas numpy scipy matplotlib seaborn opencv-python scikit-image pillow networkx ultralytics ipywidgets
```

Tunggu sampai selesai. Kalau muncul deretan panjang `Successfully installed ...`, berarti beres.

### Langkah 5 — Install CuPy (opsional, hanya untuk topik GPU)

CuPy adalah library Python yang mengarahkan perhitungan ke **GPU NVIDIA**, dipakai di beberapa
praktikum (misal perbandingan kecepatan CPU vs GPU).

> **Catatan:** CuPy **hanya bisa jalan kalau ada GPU NVIDIA**. Kalau laptop kamu tidak punya GPU
> NVIDIA atau belum memasang CUDA, **lewati langkah ini**. Notebooks di repo ini tetap bisa
> dijalankan dengan NumPy biasa sebagai pengganti.

Kalau kamu memang punya GPU NVIDIA + CUDA, install sesuai versimu:

```bash
pip install cupy-cuda12x
```

Kalau kamu tidak yakin versi CUDA yang dipakai, jalankan perintah ini untuk melihat daftar
paket CuPy yang tersedia beserta versinya:

```bash
pip index versions cupy-cuda12x
```

### Langkah 6 — Buka Jupyter Notebook

Jalankan:

```bash
jupyter notebook
```

Browser akan otomatis terbuka. Di halaman Jupyter, navigate ke folder `semester 2` atau
`semester 3`, lalu klik file `.ipynb` yang mau dikerjakan.

### Langkah 7 — Menjalankan Notebook

Di Jupyter Notebook, ada beberapa tombol penting:

| Tombol | Fungsi |
|---|---|
| **▶ Run** / `Shift + Enter` | Menjalankan cell yang sedang aktif |
| **Run All** (menu *Cell*) | Menjalankan semua cell dari atas ke bawah, sekaligus |
| **Restart & Run All** | Menjalankan ulang dari awal (paling aman) |

**Tips:** Selalu pakai **Restart & Run All** sebelum mengumpulkan tugas. Ini memastikan
semua output benar-benar berasal dari kode kamu sendiri, bukan sisa output sebelumnya.

### Langkah 8 — Konversi ke PDF (untuk pengumpulan)

Notebook harus dikumpulkan dalam bentuk PDF. Dari Jupyter:

**Cara 1 — ekspor HTML, lalu print dari browser (paling andal):**

```bash
jupyter nbconvert --to html "semester 3/m2/2-Tekrek-M2-Dasar-Statistik-FIKTI-FTI (Informatika, Teknik Elektro).ipynb"
```

1. Buka file `.html` hasil ekspor di Chrome atau Edge
2. Tekan `Ctrl + P`
3. Pilih printer **Save as PDF**
4. Centang **Background graphics** (supaya grafik ikut tercetak)
5. Set margin ke **None**, lalu Klik **Save**

**Cara 2 — langsung dari Jupyter:**

1. Menu *File → Print Preview*
2. Pilih printer **Save as PDF**
3. Centang **Notebook cell backgrounds** dan **Notebook (HTML)**
4. Klik **Save**

> **Hindari `--to pdf`.** Perintah itu memakai LaTeX (`pdflatex`/`xelatex`) yang harus
> diinstall terpisah, dan sering gagal dengan error `pdflatex not found`.
> Cara 1 di atas tidak butuh apa pun tambahan dan hasilnya rapi.

> Tersedia juga video tutorial konversi notebook ke PDF dari pihak MK Praktikum Unggulan:
> [youtu.be/qXELXtnAK7c](https://youtu.be/qXELXtnAK7c)

---

## Daftar Library yang Dibutuhkan

Library di bawah ini sudah otomatis terinstall di Langkah 4. Daftar ini hanya sebagai
referensi kalau kamu ingin tahu fungsi masing-masing.

| Library | Fungsi | Dipakai di |
|---|---|---|
| `pandas` | Membaca dan mengolah data tabular (CSV) | Semua notebook |
| `numpy` | Perhitungan numerik di CPU | Semua notebook |
| `scipy` | Statistik dan scientific computing (hypotesis testing, dll) | Statistik |
| `matplotlib` | Membuat grafik | Visualisasi |
| `seaborn` | Grafik yang lebih rapi dari matplotlib (heatmap, jointplot) | Visualisasi |
| `opencv-python` | Pengolahan citra (gambar) | Semester 2 P8 |
| `scikit-image` | Pengolahan citra lanjutan | Semester 2 P8 |
| `pillow` | Membuka dan menyimpan file gambar | Semester 2 P8 |
| `ultralytics` | Object detection dengan YOLO | Semester 2 P7 |
| `networkx` | Graf dan algoritma pencarian jalur | Semester 2 P6 |
| `ipywidgets` | Membuat interface interaktif (tombol game) | Semester 2 P4 |
| `cupy` | Perhitungan paralel di GPU NVIDIA | Semester 2 P1, P3 |

---

## Struktur Folder

```
kuliah_praktikum_superkomputer_NVIDIADGXA100/
├── README.md                        ← file ini
├── .gitignore
├── semester 2/                      ← Praktikum Kecerdasan Buatan (Tingkat 1)
│   ├── m1/  ... m8/
└── semester 3/                      ← Praktikum Komputasi Big Data (Tingkat 2)
    ├── m1/                          ← Dasar Statistik (data tumor)
    └── m2/                          ← Dasar Statistik (data semen/beton)
```

Setiap folder pertemuan punya format yang kurang lebih sama:

```
semester X/mY/
├── <soal>.ipynb                      ← file kerja utama (isi kode + soal)
├── <NIM>_<Nama>_<soal>.pdf           ← hasil pengumpulan (WAJIB ada)
└── <NIM>_<Nama>_<soal>.html          ← hasil ekspor HTML (opsional)
```

---

## Daftar Praktikum per Pertemuan

### Semester 2 — Praktikum Teknologi Kecerdasan Artifisial (Tingkat 1)

| Pertemuan | Topik | Materi |
|---|---|---|
| M1 | Pengenalan AI dengan Superkomputer NVIDIA DGX A100 | Perbandingan bilangan prima, faktorial, Fibonacci, CPU vs GPU |
| M2 | Python Matriks dan NumPy Array | Pembuatan array, operasi matriks |
| M3 | CPU vs GPU | Perbandingan waktu transpos matriks NumPy vs CuPy |
| M4 | Game dengan Python | Mind Reader Game (menggunakan `ipywidgets`) |
| M5 | AI sederhana | Modifikasi permainan batu gunting kertas dengan sistem AI |
| M6 | Graph Search Path | Pencarian jalur terpendek |
| M7 | Object Detection | Deteksi objek dengan Ultralytics YOLO (`yolov8n.pt`) |
| M8 | Image Processing | Kontur gambar, histogram citra berwarna dan grayscale |

### Semester 3 — Praktikum Komputasi Big Data (Tingkat 2)

| Pertemuan | Topik | Materi |
|---|---|---|
| M1 | Dasar Statistik (data tumor) | Histogram, outlier, boxplot, summary statistics, CDF, effect size, korelasi, kovarians, uji hipotesis, distribusi normal |
| M2 | Dasar Statistik (data semen) | Histogram, boxplot, summary statistics, hubungan antar variabel, correlation map, kovarians, korelasi Pearson & Spearman, uji hipotesis |

Dataset yang dipakai:

- **Data tumor** — Breast Cancer Wisconsin (Diagnostic), 569 observasi
  `https://raw.githubusercontent.com/supasonicx/ATA-praktikum-01/main/data.csv`
- **Data semen/beton** — Concrete Compressive Strength, 1030 observasi
  `https://raw.githubusercontent.com/supasonicx/ATA-praktikum-01/main/concrete.csv`

Kedua dataset dibaca langsung dari URL, jadi **tidak perlu download manual** — tapi notebook
memerlukan koneksi internet saat dijalankan.

---

## Cara Mengumpulkan Tugas

> Panduan lengkap dan terbaru bisa dibaca langsung di
> [Alur Pelaksanaan Praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/alur-pelaksanaan).
> Penjelasan di bawah diringkas dari sana.

### Format penamaan file

Format ini **wajib** dipakai supaya file kamu mudah dikenali:

```
<NIM>_<Nama>_<KodeSoal>.pdf
```

Contoh nyata dari repo ini:

```
20125258_Dicky_1KB04_prak_bigdata_NvidiaDGXA100_p2.pdf
```

| Bagian | Isi |
|---|---|
| `20125258` | NIM kamu |
| `Dicky` | Nama depan saja, tanpa spasi |
| `1KB04` | Kode program studi + fakultas |
| `prak_bigdata_NvidiaDGXA100_p2` | Kode soal praktikum yang dikerjakan |

### Langkah pengumpulan

1. **Ekspor notebook ke PDF.** Pastikan semua output dan grafik ikut ter-render.
2. **Upload ke Virtual Class.** Masuk ke [v-class.gunadarma.ac.id](https://v-class.gunadarma.ac.id)
   menggunakan akun **studentsite**.
3. **Pilih mata kuliah yang benar.** Pastikan mata kuliah yang kamu enroll **sesuai dengan
   TINGKAT dan FAKULTAS** kamu. Salah pilih = tugas tidak terbaca.
4. **Kumpulkan di section yang benar.** Setiap pertemuan punya section pengumpulan sendiri.
   Jangan mengumpulkan di section lain.
5. **Upload sebelum deadline.** Cek batas waktu di Virtual Class. Tidak ada perpanjangan.
6. **Cek nilai.** Nilai praktikum bisa dicek di halaman
   [Cek Nilai Praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/cek-nilai-praktikum).

### Yang WAJIB diketahui

- Kerjakan **pretest, posttest, dan tugas** sesuai batas waktu yang tertera di Virtual Class.
- Pada moda HANDS-ON, pastikan memakai **link DGX yang sesuai dengan fakultas kamu**.
- Login ke Virtual Class harus memakai **akun studentsite yang benar**. Kalau trouble, pakai
  fitur **Live Chat** di Virtual Class.
- Login ke DGX memakai **username = NIM** dan **password = password studentsite**.
- Bagian soal tidak boleh diubah, hanya isi bagian `# CODE HERE`.

### Syarat kelulusan

Mahasiswa dinyatakan **LULUS** hanya kalau memenuhi semua ketentuan berikut:

| Ketentuan | Detail |
|---|---|
| **Absen HANDS-ON** | Batas ketidakhadiran hanya **1 kali** dari 4 sesi HANDS-ON |
| **Kehadiran** | Total kehadiran minimal **70%** (dihitung dari 4 sesi HANDS-ON + 4 sesi SELF STUDY) |
| **Virtual Class** | Harus akses Virtual Class sesuai **TINGKAT, FAKULTAS, dan TAHUN AJARAN** |
| **Tugas** | Pre-Test, Post-Test, dan Tugas harus dikerjakan di **seluruh 8 pertemuan** |
| **Nilai akhir** | Total nilai ≥ batas nilai kelulusan |

Kalau salah satu ketentuan di atas tidak terpenuhi, mahasiswa bisa dinyatakan **TIDAK LULUS**.
Nilai akhir akan terbit di **DNS** (student center) pada waktu yang ditentukan BAAK. Jadwal
praktikum juga bisa dicek di [BAAK](https://baak.gunadarma.ac.id) dengan mencari kelas kamu.

### Kalau salah pilih mata kuliah

Ini masalah yang paling sering terjadi. Solusinya: hapus enrollment yang salah, lalu enroll ulang
dengan benar. Hubungi **asisten praktikum** atau cek
[halaman pengulangan praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/pengulangan-praktikum).

---

## Referensi Resmi

| Sumber | Link |
|---|---|
| **Situs utama MK Praktikum Unggulan UG** | https://www.praktikum-hpc.gunadarma.ac.id/ |
| **Virtual Class (tempat upload tugas)** | https://v-class.gunadarma.ac.id/ |
| Teknis Pelaksanaan | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/teknis-pelaksanaan](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/teknis-pelaksanaan) |
| Alur Pelaksanaan | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/alur-pelaksanaan](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/alur-pelaksanaan) |
| Link Akses DGX | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/link-akses-dgx](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/link-akses-dgx) |
| Tata Tertib Praktikum | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/tata-tertib-praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/tata-tertib-praktikum) |
| Pengulangan Praktikum | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/pengulangan-praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/pengulangan-praktikum) |
| Cek Nilai Praktikum | [praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/cek-nilai-praktikum](https://www.praktikum-hpc.gunadarma.ac.id/pelaksanaan-praktikum/cek-nilai-praktikum) |
| Jadwal Praktikum UG | [praktikum-hpc.gunadarma.ac.id/jadwal-praktikum/jadwal-praktikum-ug](https://www.praktikum-hpc.gunadarma.ac.id/jadwal-praktikum/jadwal-praktikum-ug) |
| **HPC Hub UG** | https://www.hpc-hub.gunadarma.ac.id |
| PSA UG | https://psa.gunadarma.ac.id |
| BAAK UG | https://baak.gunadarma.ac.id |
| Studentsite UG | https://studentsite.gunadarma.ac.id |

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'seaborn'`

Library belum terinstall, atau virtual environment belum aktif.

```bash
# pastikan ada tanda (.venv) di awal baris terminal
.venv\Scripts\activate
pip install seaborn matplotlib pandas numpy scipy
```

### `NoSuchKernel: No such kernel named 'conda-base-py'`

Notebook ini berasal dari mesin lain, sedangkan kernel-nya tidak ada di laptop kamu.

**Solusi:** di Jupyter, klik kanan file notebook → **Change Kernel** → pilih **Python 3**.

### `URLError` / `Failed to establish a new connection`

Dataset tidak bisa diunduh. Cek dulu koneksi internet kamu. Kalau captive portal (jaringan
kampus yang minta login), login dulu ke browser.

### `pdflatex not found` atau `NotImplementedError` saat konversi ke PDF

Masalah ini muncul karena `nbconvert --to pdf` butuh LaTeX yang belum terinstall.
**Tidak perlu repot** — ekspor ke HTML lalu print dari browser:

```bash
jupyter nbconvert --to html "nama-notebook.ipynb"
```

Lalu buka di Chrome, `Ctrl + P`, pilih *Save as PDF*.

### Error `cupy` / `cudaErrorInsufficientDriver`

GPU tidak terdeteksi. Install NVIDIA Driver dan CUDA Toolkit yang sesuai, atau **lewati saja
CuPy** dan pakai NumPy sebagai pengganti.

### Grafik tidak muncul / notebook kosong

- Pastikan kamu sudah menjalankan cell-nya (tombol ▶)
- Kalau masih kosong, pakai **Restart & Run All** dari menu *Cell*
- Kalau grafik error, jalankan ulang cell *import library* paling atas

### di PowerShell muncul error saat aktivasi `.venv`

PowerShell membatasi eksekusi script secara default. Jalankan sekali:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Lalu aktifkan ulang. Atau pakai **Command Prompt** biasa saja.

---

## Kontak

Untuk pertanyaan mengenai penjadwalan, enrollment, atau nilai, hubungi **asisten
praktikum** melalui [halaman kontak MK Praktikum Unggulan](https://www.praktikum-hpc.gunadarma.ac.id/kontak)
atau **[Studentsite UG](https://studentsite.gunadarma.ac.id)**.

---

## Lisensi & Catatan

Repositori ini bersifat pribadi sebagai kumpulan tugas mahasiswa. Materi soal resmi tetap
milik **Universitas Gunadarma** dan dapat diakses gratis di
[praktikum-hpc.gunadarma.ac.id](https://www.praktikum-hpc.gunadarma.ac.id/).
