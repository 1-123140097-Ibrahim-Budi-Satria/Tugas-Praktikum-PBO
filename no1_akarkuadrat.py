import math

def akar_kuadrat():
    while True:
        try:
            angka = float(input('Masukkan angka: '))
            if angka < 0:
                print('Input tidak valid. Angka harus positif.')
                continue
            elif angka == 0:
                print('Akar kuadrat dari 0 adalah 0.')
                break
            else:
                hasil = math.sqrt(angka)
                print(f'Akar kuadrat dari {angka} adalah {hasil}.')
                break
        except ValueError:
            print('Input tidak valid. Masukkan angka yang valid.')

if __name__ == '__main__':
    akar_kuadrat()