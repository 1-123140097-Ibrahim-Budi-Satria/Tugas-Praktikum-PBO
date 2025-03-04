height = int(input("Masukkan tinggi segitiga: ")) 
for i in range(height): 
    print(' ' * (height - i - 1) + '*' * (i*2 + 1))