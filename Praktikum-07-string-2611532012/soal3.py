# Soal Bagian A
print("Bagian A")
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:])
print()
# Soal Bagian B
print("Bagian B")
text = "Muhammad Rusdy Rahman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
