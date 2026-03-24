import tkinter as tk

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x250")

# Entry untuk input pertama
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Entry untuk input kedua
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Label untuk menampilkan hasil
hasil_label = tk.Label(root, text="Hasil: ")
hasil_label.pack(pady=5)


# Fungsi untuk melakukan operasi penjumlahan
def ambil_input():
    try:
        # Ambil value dari entry dan ubah ke float
        angka1 = float(entry1.get())
        angka2 = float(entry2.get())
        print("DEBUG angka1:", angka1)
        print("DEBUG angka2:", angka2)

        return angka1, angka2
    except:
        # Kalau input bukan angka, tampilkan error
        hasil_label.config(text="Hasil: Input harus berupa angka!")
        return None, None


# Fungsi untuk melakukan operasi sesuai dengan tombol yang ditekan
def hitung(operasi):
    angka1, angka2 = ambil_input()
    # Kalau input error, stop sistem
    if angka1 is None or angka2 is None:
        return

    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            hasil_label.config(text="Hasil: Tidak bisa dibagi dengan nol!")
            return
        hasil = angka1 / angka2

    # Menampilkan hasil
    if hasil.is_integer():
        hasil = int(hasil)

    hasil_label.config(text=f"Hasil: {hasil}")


# Tombol untuk operasi penjumlahan
btn_tambah = tk.Button(root, text="+", command=lambda: hitung("+"))
btn_tambah.pack()

# Tombol untuk operasi pengurangan
btn_kurang = tk.Button(root, text="-", command=lambda: hitung("-"))
btn_kurang.pack()

# Tombol untuk operasi perkalian
btn_kali = tk.Button(root, text="*", command=lambda: hitung("*"))
btn_kali.pack()

# Tombol untuk operasi pembagian
btn_bagi = tk.Button(root, text="/", command=lambda: hitung("/"))
btn_bagi.pack()


# Fungsi Enter Key
def enter_key(event):
    hitung("+")  # Default operasi penjumlahan saat Enter ditekan


root.bind('<Return>', enter_key)

# def hitung(operasi):
#     print("Operasi:", operasi)  # DEBUG

root.mainloop()
