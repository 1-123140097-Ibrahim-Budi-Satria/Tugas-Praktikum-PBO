import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
    
class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.blood_type = random.choice(father.blood_type) + random.choice(mother.blood_type)
        if 'A' in self.blood_type and 'B' in self.blood_type:
            self.blood_type = 'AB'
        elif 'A' in self.blood_type:
            self.blood_type = 'A'
        elif 'B' in self.blood_type:
            self.blood_type = 'B'
        else:
            self.blood_type = 'O'

goldar_ayah = input("Masukkan golongan darah ayah (A/B/AB/O): ")
goldar_ibu = input("Masukkan golongan darah ibu (A/B/AB/O): ")

ayah = Father(goldar_ayah)
ibu = Mother(goldar_ibu)

anak = Child(ayah, ibu)

print(f"Golongan darah anak adalah {anak.blood_type}")