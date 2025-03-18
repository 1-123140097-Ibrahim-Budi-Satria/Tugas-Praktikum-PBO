import math
class Kalku:
    def __init__(self, nilai=0):
        self.nilai = nilai
    
    def __str__(self):
        return f"{self.nilai}"
    
    def __repr__(self):
        return f"Kalku({self.nilai})"
    
    def __add__(self, other):
        if isinstance(other, Kalku):
            return Kalku(self.nilai + other.nilai)
        
    def __sub__(self, other):
        if isinstance(other, Kalku):
            return Kalku(self.nilai - other.nilai)
        
    def __mul__(self, other):
        if isinstance(other, Kalku):
            return Kalku(self.nilai * other.nilai)
        
    def __truediv__(self, other):
        if isinstance(other, Kalku):
            return Kalku(self.nilai / other.nilai)
        
    def __pow__(self, other):
        if isinstance(other, Kalku):
            return Kalku(self.nilai ** other.nilai)
        
    def log(self, base=math.e):
        if self.nilai <= 0:
            raise ValueError("Logaritma hanya didefinisikan untuk nilai positif")
        if base <= 0 or base == 1:
            raise ValueError("Basis logaritma harus positif dan tidak sama dengan 1")
        return Kalku(math.log(self.nilai, base))
    
nilai1 = Kalku(10)
nilai2 = Kalku(2)

print(f"Angka pertama (a) : {nilai1}")
print(f"Angka kedua (b) : {nilai2}")
print(f"a + b : {nilai1 + nilai2}")
print(f"a - b : {nilai1 - nilai2}")
print(f"a * b : {nilai1 * nilai2}")
print(f"a / b : {nilai1 / nilai2}")
print(f"a ** b : {nilai1 ** nilai2}")
print(f"log a : {nilai1.log()}")