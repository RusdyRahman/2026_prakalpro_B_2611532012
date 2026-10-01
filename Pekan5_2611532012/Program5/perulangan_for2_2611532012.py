# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_1234
# Program ini menggunakan fungsi input()

ulang_2012 = int(input("Masukkan jumlah perulangan : "))
print("Perulangan ke-0 sampai ke-", ulang_2012-1)
for i_2012 in range(ulang_2012):
    print(i_2012, end="")
print()
print("Perulangan ke-1 sampai ke-", ulang_2012)
for i_2012 in range(1,ulang_2012+1):
    print(i_2012, end="")