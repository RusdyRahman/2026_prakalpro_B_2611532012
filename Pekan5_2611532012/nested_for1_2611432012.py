# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# ama variabel ditambah 4 digit nim terakhir contoh : nested_1234
# Program ini menggunakan fungsi input()

batas_2012 = int(input("Masukkan batas perulangan: "))
for line_2012 in range(1, batas_2012 + 1):
    for j_2012 in range(1,(-1 * line_2012 + batas_2012 + 1)):
        print(".", end="")
    print(line_2012)