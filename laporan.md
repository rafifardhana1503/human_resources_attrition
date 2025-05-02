# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan kini memiliki lebih dari 1.000 karyawan yang tersebar di berbagai wilayah.

Meskipun telah berkembang menjadi perusahaan besar, Jaya Jaya Maju masih menghadapi tantangan dalam pengelolaan karyawannya. Salah satu dampaknya adalah tingginya angka attrition rate, yaitu rasio karyawan yang keluar dibandingkan dengan total karyawan, yang saat ini melebihi 10%.

Untuk mengatasi permasalahan ini, manajer departemen HR memutuskan untuk menganalisis faktor-faktor yang menyebabkan tingginya attrition rate dan membuat dashboard bisnis yang dapat membantu memantau faktor-faktor tersebut secara efektif.

### Permasalahan Bisnis
1. **Menganalisis Faktor-Faktor yang Menyebabkan Tingginya Attrition Rate**\
   Apa saja faktor yang memengaruhi keputusan karyawan untuk keluar?
2. **Memprediksi Potensi Risiko Karyawan Melakukan Attrition**\
   Bagaimana cara memprediksi karyawan yang berisiko keluar lebih awal?   
3. **Membangun Visualisasi Data yang Informatif**
   Bagaimana membuat tim HR dapat memantau faktor-faktor risiko tersebut melalui visualisasi yang mudah dipahami?

### Cakupan Proyek
1. **Menganalisa Data Karyawan**
   - Melakukan eksplorasi mendalam terhadap data (EDA) untuk menemukan tren dan wawasan penting yang berkaitan dengan keluarnya karyawan dari perusahaan.
   - Mengidentifikasi faktor-faktor utama yang memiliki pengaruh signifikan terhadap keputusan karyawan untuk berhenti bekerja.
2. **Membangun Model Machine Learning Prediksi**
   - Membangun model machine learning untuk memperkirakan kemungkinan seorang karyawan akan mengundurkan diri.
   - Model ini bertujuan membantu HR mengidentifikasi karyawan berisiko tinggi agar bisa segera mencari cara solutif sebelum karyawan memutusukan untuk berhenti bekerja.
3. **Membuat Business Dashboard**
   - Merancang dashboard interaktif yang menyajikan visualisasi dari faktor-faktor kunci penyebab attrition.
   - Dashboard ini akan menjadi alat bantu bagi manajer HR dalam memantau kondisi karyawan dan mengendalikan angka attrition secara tepat.
4. **Merekomendasikan Strategi Efektif**
   - Menyusun saran strategis berdasarkan temuan data dan hasil prediksi guna membantu HR dalam menurunkan angka attrition di masa mendatang.

### Persiapan
Perusahaan menyediakan dataset yang memuat data terkait karyawan, mencakup aspek demografis, latar belakang pekerjaan, gaji, serta divisi tempat bekerja. Data ini berguna untuk menganalisis pola dan keterkaitannya dengan angka keluarnya karyawan.

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

**Setup environment:**\
1. Prasyarat Tools
   - Google Colab: [Google Colab](https://colab.research.google.com/)
   - Google Looker Studio: [Looker Studio](https://lookerstudio.google.com/u/0/navigation/reporting)
2. Clone Repository\
   Clone Repository menggunakan git
   ```
   git clone https://github.com/rafifardhana1503/human_resources_attrition
   cd human_resources_attrition
   ```
3. Setup Google Colab
   ```
   Python 3.11.12
   ```
   Penggunaan Google Colab sudah menyediakan versi Python terbaru secara default. Sebagian besar library populer sudah kompatibel, sehingga tidak perlu menginstall requirements.txt 
4. Setup Looker Studio
   - Membuat **Blank Report**
   - Koneksikan data dengan **Upload File csv** `employee_data_cleaned.csv`
   - Kemudian klik **Add Data to Report**
   - Sesuaikan layout menggunakan **Responsive Layout**
   - Dataset dan canvas dashboard telah tersedia dan dapat digunakan untuk visualisasi data
5. Setelah seluruh proses setup selesai, Anda bisa menjalankan skrip utama atau mulai melakukan proses prediksi.
   - Untuk menjalankan analisis utama terdapat pada notebook.ipynb
   - Untuk mencoba prediksi menggunakan data dummy
     ```
     python prediction.py
     ```   

## Business Dashboard
Perancangan Business Dahboard diharapkan dapat membantu departemen HR untuk monitoring berbagai faktor yang mempengaruhi attrition rate karyawan. Dashboard ini memberikan visualisasi data yang informatif terhadap faktor resiko utama karyawan keluar, pola data, dan korelasi antar variabel,

Dashboard ini mencakup
1. **KPI (Key Performance Indicator) Section**\
   Section ini berisikan gambaran umum terkait attrition pada perusahaan Jaya Jaya Maju
   - **Overall Attrition (%)**: Menampilkan persentase attrition (karyawan keluar) terhadap total karyawan, yaitu **16.92%**. Dapat memberikan gambaran seberapa besar attrition rate pada perusahaan.
   - **Total Employees**: Menampilkan jumlah keseluruhan karyawan perusahaan, yaitu **1,058** karyawan
   - **Total Attrtion**: Menampilkan jumlah karyawan yang keluar, yaitu **179** karyawan
2. **Attrition by Marital Status**
   - Menampilkan bar chart yang menunjukkan bahwa karyawan dengan status **Single** memiliki angka attrition tertinggi (**92 karyawan**), diikuti dengan status **Married** (**62 karyawan**) dan **Divorced** (**23 karyawan**)
3. **Attrition by Age**
   - 
5.     

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
