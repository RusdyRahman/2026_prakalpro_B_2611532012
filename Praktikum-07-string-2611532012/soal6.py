full_name = input("Masukkan Nama: ")
nim = (input("Masukkan NIM: "))
clean = full_name.strip()
space = clean.find(" ")

if space == -1 :
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]
print(username)