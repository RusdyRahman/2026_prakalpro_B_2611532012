# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh : ulang_1234
# Program ini menggunakan fungsi input()

batas_2012 = int(input("Masukkan nilai batas: "))
for i_2012 in range(batas_2012 + 1):
    for j_2012 in range(batas_2012 + 1):
        print(i_2012 +j_2012, end=" ")
    print() #Pindah ke baris berikutnya