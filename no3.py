nama = str(input("Masukkan nama: "))
nim = str(input("Masukkan NIM: "))
res = str(input("Masukkan resolusi tahun ini: "))

with open('ME.txt', 'w') as f:
    f.write(nama)
    f.write(nim)
    f.write(res)