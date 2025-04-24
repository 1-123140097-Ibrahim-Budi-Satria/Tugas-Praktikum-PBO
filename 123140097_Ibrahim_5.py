import tkinter as tk
import json
import os
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("Catatan Harian")

catatan = []

def tambah_catatan():
    judul = entry_judul.get().strip()
    isi = text_isi.get("1.0", "end").strip()
    if not judul or not isi:
        return messagebox.showerror("Error", "Judul dan isi tidak boleh kosong.")
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
    catatan.append({"judul": f"{waktu} - {judul}", "isi": isi})
    listbox.insert("end", catatan[-1]["judul"])
    entry_judul.delete(0, "end")
    text_isi.delete("1.0", "end")

def tampilkan_catatan(event):
    if not listbox.curselection(): return
    idx = listbox.curselection()[0]
    text_isi.config(state="normal")
    text_isi.delete("1.0", "end")
    text_isi.insert("end", catatan[idx]["isi"])
    text_isi.config(state="disabled")

def hapus_catatan():
    if not listbox.curselection():
        return messagebox.showerror("Error", "Pilih catatan yang akan dihapus.")
    if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus catatan ini?"):
        idx = listbox.curselection()[0]
        listbox.delete(idx)
        del catatan[idx]
        text_isi.config(state="normal")
        text_isi.delete("1.0", "end")

def edit_catatan():
    if not listbox.curselection():
        return messagebox.showerror("Error", "Pilih catatan yang akan diedit.")
    idx = listbox.curselection()[0]
    judul = entry_judul.get().strip()
    isi = text_isi.get("1.0", "end").strip()
    if not judul or not isi:
        return messagebox.showerror("Error", "Judul dan isi tidak boleh kosong.")
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
    catatan[idx] = {"judul": f"{waktu} - {judul}", "isi": isi}
    listbox.delete(idx)
    listbox.insert(idx, catatan[idx]["judul"])
    listbox.selection_set(idx)

def simpan_ke_file():
    with open("catatan.json", "w") as f:
        json.dump(catatan, f)

def muat_dari_file():
    if os.path.exists("catatan.json"):
        with open("catatan.json", "r") as f:
            data = json.load(f)
            catatan.extend(data)
            for item in data:
                listbox.insert("end", item["judul"])

def keluar():
    simpan_ke_file()
    root.destroy()

def tentang():
    messagebox.showinfo("Tentang", "Catatan Harian v1.0\nDibuat dengan Tkinter")

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Keluar", command=keluar)
menu.add_cascade(label="File", menu=file_menu)
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="Tentang", command=tentang)
menu.add_cascade(label="Bantuan", menu=help_menu)
root.config(menu=menu)

entry_judul = tk.Entry(root, width=40)
entry_judul.grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=5)

tk.Button(root, text="Tambah Catatan", command=tambah_catatan).grid(row=1, column=0, sticky="we", padx=5)
tk.Button(root, text="Edit Catatan", command=edit_catatan).grid(row=1, column=1, sticky="we", padx=5)
tk.Button(root, text="Hapus Catatan", command=hapus_catatan).grid(row=1, column=2, sticky="we", padx=5)

frame_kiri = tk.Frame(root)
frame_kanan = tk.Frame(root)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=3)

frame_kiri.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
frame_kanan.grid(row=2, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

listbox = tk.Listbox(frame_kiri)
listbox.pack(side="left", fill="both", expand=True)
scrollbar = tk.Scrollbar(frame_kiri, command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)
listbox.bind("<<ListboxSelect>>", tampilkan_catatan)
text_isi = tk.Text(frame_kanan, wrap="word")
text_isi.pack(fill="both", expand=True)

muat_dari_file()
root.mainloop()