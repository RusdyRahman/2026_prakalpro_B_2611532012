# Buat Program dengan nama file 
# Program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_1234
# Program ini menggunakan fungsi input()
tinggi_2012 = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk setiap baris
for i_2012 in range(1, tinggi_2012 + 1):
    # Cetak spasi di awal baris
    print(" " * (tinggi_2012 - i_2012), end="")
    # Cetak bintang diikuti spasi
    print("* " * i_2012)