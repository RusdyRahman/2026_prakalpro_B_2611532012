# soal5 bagian (A)
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

username = input("Username: ")

ada_simbol = False
for karakter in username:
    if not karakter.isalnum():
        ada_simbol = True
        break

awalan_angka = False
for karakter in username:
    if not username[0].isalpha():
        awalan_angka = True
        break

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif ada_simbol:
    print("Invalid: letters and digits only")
elif awalan_angka:
    print("Invalid: must start with a letter")
else:
    print("Valid")
print()

