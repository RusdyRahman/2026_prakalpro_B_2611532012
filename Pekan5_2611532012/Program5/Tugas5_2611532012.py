# Buat file dengan nama file Tugas5_NIM.py
# Buat program jam pasir menggunakan perulangan for
# Nama variabel ditambah 4 digit terakhir contoh : angka_1234
# Program ini menggunakan fungsi input

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_2012 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border Atas
print("#", end="")
for garis_ganda_2012 in range(4 * n_2012 + 5):
    print("=", end="")
print("#")

# Fase 1 : Jam pasir bagian atas
for baris_2012 in range(n_2012 , 0, -1):
    print("| ", end="")
    for spasi_kiri_2012 in range(2 * (n_2012 - baris_2012)):
        print(" ", end="")
    for angka_2012 in range(baris_2012, 0, -1):
        print(angka_2012, end=" ")
    print("<*>", end="")
    for angka_2012 in range(1, baris_2012 + 1):
        print(" ", end="")
        print(angka_2012, end="")
    for spasi_kanan_2012 in range(2 *(n_2012 - baris_2012)):
        print(" ", end="")
    print(" |", end="") 
    print()
# Fase 2: Jam pasir bagian tengah 
print("|", end="")
for spasi_kiri_2012 in range(2*n_2012 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_2012 in range(2* n_2012 + 1):
    print(" ", end="")
print("|", end="")
print()
# Fase 3: Jam pasir bagian bawah
for baris_2012 in range(1, n_2012 + 1):
    print("| ", end="")
    for spasi_kiri_2012 in range(2 * (n_2012 - baris_2012)):
        print(" ", end="")
    for angka_2012 in range(baris_2012, 0, -1):
        print(angka_2012, end=" ")
    print("<*>", end="")
    for angka_2012 in range(1, baris_2012 + 1):
        print(" ", end="")
        print(angka_2012, end="")
    for spasi_kanan_2012 in range(2 *(n_2012 - baris_2012)):
        print(" ", end="")
    print(" |", end="")
    print()
# Border Bawah
print("#", end="")
for garis_ganda_2012 in range(4 * n_2012 + 5):
    print("=", end="")
print("#")