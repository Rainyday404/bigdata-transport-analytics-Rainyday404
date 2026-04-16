# 🛒 E-Commerce Sales Dashboard & Batch Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Ubuntu WSL](https://img.shields.io/badge/Ubuntu_WSL-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

Proyek ini merupakan bagian dari tugas **Big Data Analytics** yang mengimplementasikan *Batch Processing* menggunakan **Apache Spark (PySpark)** untuk pipeline data, dan **Microsoft Power BI** untuk visualisasi data interaktif.

##  Deskripsi Proyek
Sistem ini dibangun untuk memproses data mentah transaksi e-commerce dalam jumlah besar. Pipeline PySpark bertugas untuk membersihkan data, melakukan transformasi, dan menghitung agregasi metrik bisnis utama. Hasil akhir dari pemrosesan ini diekspor ke dalam direktori `serving` berformat CSV, yang kemudian dihubungkan ke Power BI untuk divisualisasikan menjadi sebuah *dashboard* analitik yang komprehensif.

##  Teknologi & Tools yang Digunakan
- **Bahasa Pemrograman:** Python 3.x
- **Big Data Framework:** Apache Spark (PySpark)
- **Visualisasi Data:** Microsoft Power BI Desktop
- **Environment:** WSL (Windows Subsystem for Linux) - Ubuntu
- **Version Control:** Git & GitHub
- **IDE:** Visual Studio Code (VS Code)

##  Metrik Bisnis yang Dihitung
Pipeline Spark dalam proyek ini dirancang untuk menghitung 3 Key Performance Indicators (KPI) utama:
1. **Total Revenue:** Menghitung total keseluruhan pendapatan dari semua transaksi yang diproses.
2. **Top Products:** Mengidentifikasi produk dengan jumlah penjualan (kuantitas) terbanyak.
3. **Revenue Category:** Menganalisis total pendapatan yang dihasilkan oleh masing-masing kategori produk (Electronics, Computing, Accessories).

---

##  Output Wajib yang Dikumpulkan

Berikut adalah dokumentasi dan bukti pengerjaan sesuai dengan kriteria tugas:

### 1. Screenshot Dashboard Power BI
Visualisasi hasil pemrosesan data menggunakan PySpark yang ditampilkan melalui Power BI.
![Dashboard Power BI](screenshots/dashboard_Power_BI.png)

### 2. File Power BI
File visualisasi mentah telah disertakan di dalam *repository* ini dengan nama:
- `bigdata_dashboard.pbix`

### 3. Screenshot Folder Serving Dataset (`data/serving`)
Bukti bahwa *script* PySpark berhasil mengekspor data hasil agregasi ke dalam direktori *serving* dalam bentuk tabel/partisi CSV.
![Folder Serving Dataset](screenshots/folder_serving_dataset.png)

### 4. Screenshot Terminal Saat Menjalankan Script
Bukti eksekusi *script* analisis `python scripts/analytics_layer.py` yang berjalan sukses tanpa error di terminal WSL/Ubuntu.

**Bagian 1:**
![Eksekusi Terminal 1](screenshots/terminal_saat_menjalankan_analytics_layer_1.png)

**Bagian 2:**
![Eksekusi Terminal 2](screenshots/terminal_saat_menjalankan_analytics_layer_2.png)

### 5. Hasil Pemrosesan Analytics Layer
Berikut adalah rincian bukti hasil eksekusi untuk masing-masing metrik yang diproses oleh Apache Spark:

**Total Revenue:**
![Total Revenue](screenshots/total_revenue_hasil_eksekusi_analytics_layer.png)

**Top Products:**
![Top Products](screenshots/top_products_hasil_eksekusi_analytics_layer.png)

**Category Revenue:**
![Category Revenue](screenshots/category_revenue_hasil_eksekusi_analytics_layer.png)

---

## 📂 Struktur Proyek
```text
bigdata-project/
│
├── data/
│   ├── raw/                 # Data transaksi mentah
│   └── serving/             # Data agregasi hasil pemrosesan Spark
│
├── scripts/
│   ├── analytics_layer.py   # Script utama PySpark untuk transformasi data
│   ├── batch_pipeline_enterprise.py
│   └── visualization_layer.py
│
├── screenshots/             # Folder berisi bukti screenshot tugas
│   ├── dashboard_Power_BI.png
│   ├── folder_serving_dataset.png
│   ├── terminal_saat_menjalankan_analytics_layer_1.png
│   ├── terminal_saat_menjalankan_analytics_layer_2.png
│   └── ... (screenshot hasil metrik lainnya)
│
├── venv/                    # Virtual Environment Python
├── .gitignore
├── README.md
└── bigdata_dashboard.pbix   # File Dashboard Power BI

```

##  Prasyarat & Cara Menjalankan Proyek

**Prasyarat Sistem:**
Pastikan sistem (Linux/WSL) sudah terinstal Python 3, Java (OpenJDK 11/8), dan Apache Spark.

**Langkah-langkah Eksekusi Script:**

1. Aktifkan *virtual environment*:
```bash
source venv/bin/activate

```


2. Instal *library* PySpark (jika belum ada):
```bash
pip install pyspark

```


3. Jalankan *script* utama PySpark:
```bash
python scripts/analytics_layer.py

```



**Cara Menggunakan Power BI Desktop:**

1. Pastikan Anda telah menginstal aplikasi **Microsoft Power BI Desktop**.
2. Buka file `bigdata_dashboard.pbix` yang ada di *repository* ini dengan cara klik ganda (*double-click*).
3. Karena sumber data (CSV) bersifat lokal, Anda mungkin perlu menyesuaikan jalurnya (*Data Source Settings*):
* Pergi ke menu **Home** > **Transform Data** > **Data source settings**.
* Ubah jalur file (Change Source) agar mengarah ke folder `data/serving` yang ada di komputermu.


4. Jika jalur sudah benar, klik tombol **Refresh** pada menu *Home* untuk memuat data terbaru hasil pemrosesan PySpark.

---

*Dibuat oleh Rain/Hujan (Ivan Dwika Bagaskara) untuk pemenuhan tugas praktikum Big Data Technology.*