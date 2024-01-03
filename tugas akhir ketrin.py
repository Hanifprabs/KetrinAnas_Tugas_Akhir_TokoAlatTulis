import tkinter as tk
from tkinter import messagebox

def tampilkan_daftar_barang() :
    daftar_barang_window = tk.Toplevel(root)
    daftar_barang_window.title("Daftar Barang Toko Alat Tulis Ketrin")

    daftar_label = tk.Label(daftar_barang_window, text = "Daftar Barang Alat Tulis : ")
    daftar_label.pack()

    daftar_text = """
    1. Pensil - Rp. 2000
    2. Bolpoin - Rp. 3000
    3. Penghapus - Rp. 500
    4. Buku Tulis Kiky 1 Pack - Rp. 38000
    5. Buku Tulis Sidu 1 Pack - Rp. 32500
    6. Stabilo - Rp. 5000
    7. Label - Rp. 3500 
    """
    daftar_barang = tk.Label(daftar_barang_window, text = daftar_text)
    daftar_barang.pack()

def hitung_total_harga(barang, jumlah) :
    harga_barang = {
        1: 2000,
        2: 3000,
        3: 500,
        4: 38000,
        5: 32500,
        6: 5000,
        7: 3500
    }

    if barang in harga_barang :
        harga = harga_barang[barang]
        total = harga * jumlah
        return total 
    else :
        return 0
    
def beli() :
    total_pembelian = 0
    barang_text = barang_entry.get()
    jumlah_text = jumlah_entry.get()

    try :
        barang = int(barang_text)
        jumlah = int(jumlah_text)

        total_pembelian = hitung_total_harga(barang, jumlah)

        messagebox.showinfo("Total Harga", f"Total Harga Pembelian Anda di Toko Alat Tulis Ketrin adalah : Rp. {total_pembelian}")

        barang_entry.delete(0, tk.END)
        jumlah_entry.delete(0, tk.END)
    except ValueError :
        messagebox.showerror("Error!", "Masukkan Harus Berupa Angka.")

def keluar() :
    root.destroy()

root = tk.Tk()
root.title("Toko Alat Tulis Ketrin")

daftar_button = tk.Button(root, text = "Daftar Barang", command = tampilkan_daftar_barang)
daftar_button.pack()

barang_label = tk.Label(root, text = "Masukkan Nomor Barang Yang Ingin Dibeli : ")
barang_label.pack()

barang_entry = tk.Entry(root)
barang_entry.pack()

jumlah_label = tk.Label(root, text = "Masukkan Jumlah Barang : ")
jumlah_label.pack()

jumlah_entry = tk.Entry(root)
jumlah_entry.pack()

beli_button = tk.Button(root, text = "Beli", command = beli)
beli_button.pack()

exit_button = tk.Button(root, text = "Keluar", command = keluar)
exit_button.pack()

root.mainloop()
