total = 0

while True:
    angka = int(input("Enter a number: "))
    
    if angka < 0:
        break  # Bilangan negatif menghentikan loop
    elif angka == 0:
        continue  # Bilangan 0 dilewati
    else:
        print(f"Positive number: {angka}")  # Menampilkan bilangan positif
        total += angka  # Menjumlahkan bilangan positif

print(f"Total: {total}")  # Menampilkan total setelah loop selesai8