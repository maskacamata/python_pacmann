import libraries.lingkaran as lingkaran
import libraries.persegi_panjang as persegi_panjang
import libraries.segitiga as segitiga
import libraries.produksi as produksi

# dictionary
data = {"biaya_produksi" : 35000,
        "harga_jual" : 50000,
        "jumlah_produk" : 1200,
        "persediaan_sisa" : 100}

produksi.profit(data)

# for key, value in data.items():
#     print( key, '=', value )


# #pilih bangun datar
# response = input("Pilih bangun datar, Lingkaran/Persegi Panjang/Segitiga: ")

# if response == "Lingkaran" or response == "lingkaran":
#     mode = input("hitung luas/keliling? ")
#     if mode == "luas" or mode == "Luas":
#         luas_lingkaran = lingkaran.luas()
#         print(f"Luas lingkaran adalah {luas_lingkaran}")
#     elif mode == "keliling" or mode == "Keliling":
#         keliling_lingkaran = lingkaran.keliling()
#         print(f"Keliling lingkaran adalah {keliling_lingkaran}")