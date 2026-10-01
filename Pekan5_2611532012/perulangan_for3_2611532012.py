# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_1234
# Program ini menggunakan fungsi input()

ulang_2012 = int(input("Masukkan jumlah perulangan : "))

jumlah_2012 = 0 
for i_2012 in range(1, ulang_2012 + 1):
    print(i_2012, end=" ")
    jumlah_2012 = jumlah_2012 + i_2012

    if i_2012 < ulang_2012:
        print(" + ", end="")
    else:
        print(" = ", end="")
print()
print("Jumlah =", jumlah_2012)