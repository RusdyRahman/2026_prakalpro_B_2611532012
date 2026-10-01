# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : nested_1234
# Program ini menggunakan fungsi input()

batas_2012 = int(input("Masukkan nilai batas: "))
for i_2012 in range(1, batas_2012 + 1):
    for j_2012 in range(1, batas_2012+ 1):
        print("*", end="")
    print() # Pindah ke baris berikutnya