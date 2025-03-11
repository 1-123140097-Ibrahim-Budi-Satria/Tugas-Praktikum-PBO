import random
import time

class Robot:
    def __init__(self, nama, hp, atk, defence, accuracy=80):
        self.nama = nama
        self.hp = hp
        self.max_hp = hp  # Menyimpan HP maksimum untuk regenerasi
        self.atk = atk
        self.defence = defence
        self.accuracy = accuracy  # Akurasi serangan dalam persen (0-100)
        self.hidup = True
        self.defence_mode = False  # Status mode defence
    
    def serang(self, target):
        # Cek apakah serangan berhasil berdasarkan accuracy
        hit_chance = random.randint(1, 100)
        if hit_chance > self.accuracy:
            print(f"❌ {self.nama} mencoba menyerang {target.nama} tetapi GAGAL! ❌")
            return
        
        # Hitung damage dengan mempertimbangkan pertahanan
        damage_base = self.atk
        damage_random = random.randint(1, 10)  # Elemen acak
        damage_total = damage_base + damage_random
        
        # Tambahan pengurangan damage jika target dalam mode defence
        defence_bonus = 0
        if target.defence_mode:
            defence_bonus = target.defence  # Bonus pertahanan saat defence mode aktif
            target.defence_mode = False  # Reset defence mode setelah digunakan
            print(f"{target.nama} dalam mode DEFENCE! Damage dikurangi!")
        
        # Kurangi damage berdasarkan pertahanan target
        damage_dikurangi = max(1, damage_total - ((target.defence + defence_bonus) // 2))
        
        # Kurangi HP target
        target.hp -= damage_dikurangi
        
        print(f"✅ {self.nama} menyerang {target.nama} dan memberikan {damage_dikurangi} damage!")
        
        # Cek apakah target masih hidup
        if target.hp <= 0:
            target.hp = 0
            target.hidup = False
            print(f"{target.nama} telah dikalahkan!")
    
    def regen_hp(self):
        # Hitung jumlah HP yang akan diregenerasi (15-25% dari max HP)
        regen_amount = int(self.max_hp * (random.randint(15, 25) / 100))
        
        # Pastikan tidak melebihi HP maksimum
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + regen_amount)
        actual_regen = self.hp - old_hp
        
        print(f"💚 {self.nama} melakukan REGENERASI dan memulihkan {actual_regen} HP! 💚")
    
    def defence(self):
        # Aktifkan mode defence untuk mengurangi damage di serangan berikutnya
        self.defence_mode = True
        print(f"🛡️ {self.nama} memasuki mode DEFENCE! Serangan berikutnya akan dikurangi! 🛡️")
    
    def tampilkan_status(self):
        defence_status = " (🛡️ DEFENCE aktif)" if self.defence_mode else ""
        print(f"{self.nama}: HP={self.hp}/{self.max_hp}, ATK={self.atk}, DEF={self.defence}, ACC={self.accuracy}%{defence_status}")


def pertarungan(robot1, robot2):
    print("\n=== PERTARUNGAN ROBOT DIMULAI ===")
    print(f"{robot1.nama} VS {robot2.nama}")
    print("================================\n")
    
    # Tampilkan status awal
    print("Status awal:")
    robot1.tampilkan_status()
    robot2.tampilkan_status()
    print()
    
    ronde = 1
    pemain_menyerah = False
    
    # Pertarungan berlangsung sampai salah satu robot kalah atau pemain menyerah
    while robot1.hidup and robot2.hidup and not pemain_menyerah:
        print(f"\n--- Ronde {ronde} ---")
        
        # Giliran pemain (robot1)
        print(f"Giliran {robot1.nama} (Anda):")
        print("Pilih aksi:")
        print("1. Attack - Menyerang lawan (Accuracy: {}%)".format(robot1.accuracy))
        print("2. Defence - Mengurangi damage serangan berikutnya")
        print("3. Regenerasi - Memulihkan sebagian HP")
        print("4. Menyerah - Mengakhiri pertarungan")
        
        pilihan_valid = False
        while not pilihan_valid:
            try:
                pilihan = int(input("Masukkan pilihan (1-4): "))
                if 1 <= pilihan <= 4:
                    pilihan_valid = True
                else:
                    print("Pilihan tidak valid. Silakan masukkan angka 1-4.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        
        # Proses pilihan pemain
        if pilihan == 1:  # Attack
            robot1.serang(robot2)
        elif pilihan == 2:  # Defence
            robot1.defence()
        elif pilihan == 3:  # Regenerasi
            robot1.regen_hp()
        elif pilihan == 4:  # Menyerah
            print(f"\n{robot1.nama} memilih untuk MENYERAH!")
            pemain_menyerah = True
            break
            
        if not robot2.hidup:
            break
            
        # Giliran komputer (robot2)
        print(f"\nGiliran {robot2.nama} (Komputer):")
        time.sleep(1)  # Jeda dramatis
        
        # AI sederhana untuk robot2
        if robot2.hp < robot2.max_hp * 0.3 and random.random() < 0.4:
            # Regenerasi jika HP rendah
            robot2.regen_hp()
        elif robot2.hp < robot2.max_hp * 0.5 and random.random() < 0.5:
            # Defence jika HP sedang
            robot2.defence()
        else:
            # Serang jika HP cukup tinggi
            robot2.serang(robot1)
        
        # Tampilkan status setelah pertarungan
        print("\nStatus setelah ronde:")
        robot1.tampilkan_status()
        robot2.tampilkan_status()
        
        ronde += 1
        time.sleep(1)  # Jeda 1 detik antar ronde
    
    # Umumkan hasil pertarungan
    print("\n=== PERTARUNGAN SELESAI ===")
    if pemain_menyerah:
        print(f"{robot2.nama} memenangkan pertarungan karena {robot1.nama} menyerah!")
    elif robot1.hidup:
        print(f"{robot1.nama} memenangkan pertarungan!")
    else:
        print(f"{robot2.nama} memenangkan pertarungan!")

# Contoh penggunaan
if __name__ == "__main__":
    print("=== PERTARUNGAN ROBOT ===")
    nama_robot = input("Masukkan nama robot Anda: ")
    
    # Set tingkat kesulitan dengan mengubah accuracy
    print("\nPilih tingkat kesulitan:")
    print("1. Mudah (Accuracy pemain: 90%, Accuracy komputer: 70%)")
    print("2. Sedang (Accuracy pemain: 80%, Accuracy komputer: 80%)")
    print("3. Sulit (Accuracy pemain: 70%, Accuracy komputer: 90%)")
    
    pilihan_valid = False
    while not pilihan_valid:
        try:
            kesulitan = int(input("Masukkan pilihan (1-3): "))
            if 1 <= kesulitan <= 3:
                pilihan_valid = True
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1-3.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    
    # Set accuracy berdasarkan tingkat kesulitan
    acc_pemain = 90
    acc_komputer = 70
    
    if kesulitan == 2:
        acc_pemain = 80
        acc_komputer = 80
    elif kesulitan == 3:
        acc_pemain = 70
        acc_komputer = 90
    
    # Buat robot pemain dan komputer
    robot_pemain = Robot(nama_robot, hp=100, atk=15, defence=8, accuracy=acc_pemain)
    robot_komputer = Robot("RobotKomputer", hp=90, atk=17, defence=7, accuracy=acc_komputer)
    
    # Mulai pertarungan
    pertarungan(robot_pemain, robot_komputer)