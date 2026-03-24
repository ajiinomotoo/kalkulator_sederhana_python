import tkinter as tk

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x250")

# Entry untuk input pertama
tk.Label(root, text="Angka Pertama").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Entry untuk input kedua
tk.Label(root, text="Angka Kedua").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Label untuk menampilkan hasil
hasil_label = tk.Label(root, text="Hasil: ")
hasil_label.pack(pady=5)

operasi_label = tk.Label(root, text="Operasi: ")
operasi_label.pack()


# Fungsi untuk melakukan operasi penjumlahan
def ambil_input():
    if entry1.get() == "" or entry2.get() == "":
        hasil_label.config(text="⚠️ Input tidak boleh kosong")
        return None, None
    try:
        # Ambil value dari entry dan ubah ke float
        angka1 = float(entry1.get())
        angka2 = float(entry2.get())
        # print("DEBUG angka1:", angka1)
        # print("DEBUG angka2:", angka2)

        return angka1, angka2
    except ValueError:
        # Kalau input bukan angka, tampilkan error
        hasil_label.config(text="⚠️ Input harus berupa angka")
        return None, None


# Fungsi untuk melakukan operasi sesuai dengan tombol yang ditekan
last_operator = "+"

def hitung(operasi):
    global last_operator
    last_operator = operasi
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
    operasi_label.config(text=f"Operasi: {operasi}")


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: hitung("+")).grid(row=0,
                                                                      column=0)
tk.Button(frame, text="-", width=5, command=lambda: hitung("-")).grid(row=0,
                                                                      column=1)
tk.Button(frame, text="*", width=5, command=lambda: hitung("*")).grid(row=0,
                                                                      column=2)
tk.Button(frame, text="/", width=5, command=lambda: hitung("/")).grid(row=0,
                                                                      column=3)


# Fungsi Enter Key
def enter_key(event):
    hitung(last_operator)


def clear_hasil(event):
    hasil_label.config(text="Hasil: ")


entry1.bind("<Key>", clear_hasil)
entry2.bind("<Key>", clear_hasil)

root.bind('<Return>', enter_key)


def handle_key(event):
    if event.char == "+":
        hitung("+")
    elif event.char == "-":
        hitung("-")
    elif event.char == "*":
        hitung("*")
    elif event.char == "/":
        hitung("/")


def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    hasil_label.config(text="Hasil: ")
    operasi_label.config(text="Operasi: ")
    entry1.focus()

tk.Button(root, text="Reset", command=reset).pack(pady=5)

# def hitung(operasi):
#     print("Operasi:", operasi)  # DEBUG

root.bind_all("<Key>", handle_key)

root.mainloop()
