jumlah = int(input("Masukkan jumlah siswa: "))
dict = {}
for i in range(jumlah):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = input(f"Masukkan nilai untuk {nama}: ")
    dict[nama] = nilai

print("dictionary = ", dict)