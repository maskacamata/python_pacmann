from math import pi

def luas():
    print("Luas lingkaran")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = pi * jari_jari * jari_jari
    return luas

def keliling():
    print("Keliling lingkaran")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    keliling = 2 * pi * jari_jari
    return keliling