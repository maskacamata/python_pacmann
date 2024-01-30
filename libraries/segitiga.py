def luas():
    print("Luas segitiga")
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = alas * tinggi / 2
    return luas

def keliling():
    print("Keliling persegi panjang")
    sisi_1 = float(input("Masukkan panjang sisi 1: "))
    sisi_2 = float(input("Masukkan panjang sisi 2: "))
    sisi_3 = float(input("Masukkan panjang sisi 3: "))
    keliling = sisi_1 + sisi_2 + sisi_3
    return keliling