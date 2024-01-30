def profit(info):
    total_sales = info['jumlah_produk'] * info['harga_jual']
    total_cost = info['jumlah_produk'] * info['biaya_produksi']
    profit = total_sales - total_cost
    print(f"Profit bulan ini adalah: {profit}")