print("kode prediksi/bagian a")
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)
print("Kode perbaikan untuk bagian a/ bagian predksi")
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)
print()

print("Bagian B / Bagian Buat Kode")
phone = input("Masukkan Nomor Hp:")
awal = phone[:4]
akhir = phone[-3:]
jumlah_bintang = len(phone) - 7
masked = awal + "*" * jumlah_bintang + akhir
print(masked)
print()

print("Bagian C/ Bagian mencocokkan tabel")
phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)
print()
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)
print()
phone = "0812345678"
masked = phone[:4] + "*" * 3 + phone[-3:]
print(masked)
print()
phone = "082611532012"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)