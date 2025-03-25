def tambah_tugas(daftar_tugas):
    try:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        daftar_tugas.append(tugas)
        print("Tugas berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")

def hapus_tugas(daftar_tugas):
    try:
        if not daftar_tugas:
            raise ValueError("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(daftar_tugas):
            raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        tugas_dihapus = daftar_tugas.pop(nomor - 1)
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
    except ValueError:
        print("Error: Masukkan nomor yang valid.")
    except IndexError as e:
        print(f"Error: {e}")

def tampilkan_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")

def main():
    daftar_tugas = []
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan not in {"1", "2", "3", "4"}:
                raise ValueError("Pilihan tidak valid. Masukkan angka 1, 2, 3, atau 4.")
            if pilihan == "1":
                tambah_tugas(daftar_tugas)
            elif pilihan == "2":
                hapus_tugas(daftar_tugas)
            elif pilihan == "3":
                tampilkan_tugas(daftar_tugas)
            elif pilihan == "4":
                print("Keluar dari program.")
                break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()