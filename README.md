# 🧮 Kalkulator Sederhana (Tkinter)

## 📌 Deskripsi Tugas

Program ini merupakan implementasi aplikasi kalkulator sederhana berbasis GUI menggunakan Python dan library Tkinter.
Aplikasi ini dibuat untuk memenuhi tugas praktik dengan tujuan memahami konsep dasar:

* Graphical User Interface (GUI)
* Event handling
* Validasi input
* Operasi aritmatika dasar

---

## 🎯 Tujuan

* Mengimplementasikan GUI sederhana menggunakan Tkinter
* Menggunakan event handling pada tombol
* Melakukan validasi input dari pengguna
* Menampilkan hasil perhitungan secara real-time

---

## ⚙️ Spesifikasi Program

Program memiliki fitur sebagai berikut:

* Dua input (Entry) untuk angka pertama dan kedua
* Empat tombol operasi:

  * Penjumlahan (+)
  * Pengurangan (-)
  * Perkalian (*)
  * Pembagian (/)
* Label untuk menampilkan hasil perhitungan
* Validasi input:

  * Menampilkan pesan error jika input bukan angka
* Event handling:

  * Klik tombol langsung menghitung hasil
* Bonus:

  * Mendukung shortcut keyboard (Enter)

---

## 🛠️ Teknologi yang Digunakan

* Python 3
* Tkinter (library bawaan Python)

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall di komputer
2. Jalankan file program dengan perintah:

   ```bash
   python kalkulator_sederhana.py
   ```
3. Masukkan dua angka pada kolom input
4. Klik tombol operasi yang diinginkan

---

## 🧠 Penjelasan Program

### 1. Input Data

Program menggunakan widget `Entry` untuk menerima input dari pengguna.

### 2. Validasi Input

Input divalidasi menggunakan `try-except` untuk memastikan data berupa angka.

### 3. Event Handling

Setiap tombol memiliki event handler yang akan memanggil fungsi perhitungan.

### 4. Proses Perhitungan

Program menggunakan percabangan (`if-elif`) untuk menentukan operasi matematika.

### 5. Output

Hasil perhitungan ditampilkan pada label.
Jika hasil berupa bilangan bulat, maka ditampilkan tanpa desimal.

---

## ⚠️ Penanganan Error

Program menangani beberapa kondisi error, seperti:

* Input bukan angka
* Input kosong
* Pembagian dengan nol

---

## 📚 Kesimpulan

Melalui tugas ini, dapat dipahami bagaimana:

* Membuat aplikasi GUI sederhana
* Mengimplementasikan event-driven programming
* Melakukan validasi input pengguna
* Mengelola alur logika program dengan benar

---

## 👤 Identitas

Nama: Aji Nugroho
Program Studi: S1 Informatika
Mata Kuliah: Algoritma dan Pemrograma II
