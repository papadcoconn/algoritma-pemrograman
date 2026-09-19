# aplikasi hitung belajar sederhana

print("=== KASIR TOKO ALFAMART ===")

# 1. input data dari pembeli 1
nama_barang  = input("masukkan nama_barang: ")
harga = int(input("masukkan harga barang: "))
jumlah = int(input("masukkan jumlah barang : "))

# 2. proses hitung total
total_bayar = harga * jumlah

# 3. tampilkan hasil data dari pembeli 1

print("\n--- NOTA PEMBAYARAN ---")
print(f"Kamu membeli: {jumlah} {nama_barang}")
print(f"total yang harus dibayar: Rp {total_bayar}")
print(f"------------------------------------")
print(f"terimakasih telah berbelanja di kami")


