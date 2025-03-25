from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string dan tidak boleh kosong.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Usia hewan harus berupa bilangan bulat positif.")
        self.__name = name  
        self.__age = age    

    @abstractmethod
    def make_sound(self):
        pass 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string dan tidak boleh kosong.")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Usia hewan harus berupa bilangan bulat positif.")
        self.__age = age

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet! Tweet!"

def animal_sound(animal):
    print(f"{animal.get_name()} ({animal.get_age()} tahun) berkata: {animal.make_sound()}")

def main():
    zoo = []
    while True:
        print("\nPilih aksi:")
        print("1. Tambah hewan")
        print("2. Tampilkan semua hewan")
        print("3. Keluar")
        try:
            pilihan = input("Masukkan pilihan (1/2/3): ").strip()
            if pilihan == "1":
                jenis = input("Masukkan jenis hewan (Dog/Cat/Bird): ").strip().capitalize()
                name = input("Masukkan nama hewan: ").strip()
                age = int(input("Masukkan usia hewan: "))
                if jenis == "Dog":
                    zoo.append(Dog(name, age))
                elif jenis == "Cat":
                    zoo.append(Cat(name, age))
                elif jenis == "Bird":
                    zoo.append(Bird(name, age))
                else:
                    print("Jenis hewan tidak dikenal. Pilih Dog, Cat, atau Bird.")
            elif pilihan == "2":
                if not zoo:
                    print("Tidak ada hewan di kebun binatang.")
                else:
                    print("Daftar Hewan di Kebun Binatang:")
                    for animal in zoo:
                        animal_sound(animal)
            elif pilihan == "3":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()