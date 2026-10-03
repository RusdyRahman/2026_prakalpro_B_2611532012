print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_2012 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bagian Atas
print("#", end="")
for garis_ganda_2012 in range(4 * n_2012 + 5):
    print("=", end="")
print("#")

# Bagian Tengah
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

print("|", end="")
for spasi_kiri_2012 in range(2*n_2012 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_2012 in range(2* n_2012 + 1):
    print(" ", end="")
print("|", end="")
print()

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

print("#", end="")
for garis_ganda_2012 in range(4 * n_2012 + 5):
    print("=", end="")
print("#")