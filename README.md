# 🧮 Kalkulator Sederhana (Tkinter)

## 📌 Deskripsi

Program ini merupakan aplikasi kalkulator sederhana berbasis Graphical User Interface (GUI) menggunakan Python dan library Tkinter.
Aplikasi ini dibuat untuk memenuhi tugas praktik dengan tujuan memahami konsep dasar pemrograman GUI dan event-driven programming.

---

## 🎯 Tujuan

Tujuan dari pembuatan program ini adalah:

* Mengimplementasikan GUI menggunakan Tkinter
* Menerapkan event handling pada aplikasi
* Melakukan validasi input dari pengguna
* Mengimplementasikan operasi aritmatika dasar

---

## ⚙️ Fitur Program

Program memiliki fitur sebagai berikut:

### 🔢 Input

* Dua field input untuk angka pertama dan kedua

### ➕ Operasi

* Penjumlahan (+)
* Pengurangan (-)
* Perkalian (*)
* Pembagian (/)

### 🖥️ Output

* Menampilkan hasil perhitungan secara langsung
* Menampilkan operasi yang digunakan

### ⚠️ Validasi

* Menampilkan pesan error jika input kosong
* Menampilkan pesan error jika input bukan angka
* Menangani pembagian dengan nol

### ⌨️ Event Handling

* Klik tombol langsung menghitung hasil
* Tekan tombol **Enter** untuk menghitung dengan operasi terakhir
* Mendukung input dari keyboard (+, -, *, /)

### 🔄 Fitur Tambahan

* Tombol **Reset** untuk menghapus input dan hasil
* Hasil otomatis dihapus saat user mengetik input baru
* Format hasil:

  * Bilangan bulat ditampilkan tanpa desimal
  * Bilangan desimal tetap ditampilkan

---

## 🛠️ Teknologi yang Digunakan

* Python 3
* Tkinter (library bawaan Python)

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Jalankan file program dengan perintah:

   ```bash
   python kalkulator_sederhana.py
   ```
3. Masukkan angka pada kedua input
4. Pilih operasi atau gunakan keyboard

---

## 🧠 Penjelasan Singkat Program

### 1. Input & Validasi

Program mengambil input dari user menggunakan widget `Entry`, kemudian melakukan validasi:

* Input tidak boleh kosong
* Input harus berupa angka

### 2. Proses Perhitungan

Program menggunakan percabangan (`if-elif`) untuk menentukan operasi yang dipilih.

### 3. Event Handling

Setiap tombol memiliki fungsi yang akan langsung menjalankan perhitungan.
Selain itu, program juga menangani input dari keyboard menggunakan event binding.

### 4. Manajemen State

Program menyimpan operasi terakhir yang digunakan agar tombol **Enter** dapat menjalankan operasi yang sama.

---

## ⚠️ Penanganan Error

Program menangani beberapa kondisi error:

* Input kosong
* Input bukan angka
* Pembagian dengan nol

---

## 📚 Kesimpulan

Melalui pembuatan program ini, dapat dipahami:

* Cara membuat aplikasi GUI sederhana
* Konsep event-driven programming
* Pentingnya validasi input
* Pengelolaan alur logika program yang tepat

---

## 👤 Identitas

Nama: Aji Nugroho
Program Studi: S1 Informatika
Mata Kuliah: Algoritma dan Pemrograman II
