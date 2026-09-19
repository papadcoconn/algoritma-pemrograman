# aplikasi absensi karyawan sederhana

print("=== ABSENSI KARYAWAN GOGGLE ===")

# 1. input data absensi karyawan
nama  = input("masukkan nama: ")
tanggal  = int(input("masukkan tanggal: "))

# 2. proses pengisian kehadiran

isi_kehadiran = "hadir" if tanggal > 0 else "tidak hadir"

# 3. tampilkan hasil data absensi karyawan 

print("\n--- absensi karyawan ---")
print("")
print(f"nama karyawan: {nama}")
print(f"tanggal kehadiran: {tanggal}")
print(f"status kehadiran: {isi_kehadiran}")
