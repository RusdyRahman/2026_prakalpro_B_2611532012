n = int(input("Masukkan jumlah perulangan: "))
kas ={}

for i in range (n):
    nama, nominal = input().split()
    kas[nama] = kas.get(nama, 0) + int(nominal)

donatur = ""
terbesar = 0

for name, total in kas.items():
    print(f"{name}: {total}")
    if total > terbesar:
        terbesar = total
        donatur = name
print(f"Total cash: ", sum(kas.values()))
print(f"Top contributor: {donatur} ({terbesar})")