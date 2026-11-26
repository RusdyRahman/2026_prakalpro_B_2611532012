schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}
# 6a : Mencari Hari dengan mata kuliah terbanyak
print("Bagian A")
max_count = 0
busiest_day = ""
for day, coures in schedule.items():
    if len(coures) > max_count:
        max_count = len(coures)
        busiest_day = day

print(f"Busiest day: {busiest_day} {max_count}")
print()
print("Bagian B")
#6b : Menghitung berapa hari sebuah mata kuliah muncul
course = input("Masukkan nama mata kuliah: ")
count = 0

for day, courses in schedule.items():
    if course in courses:
        count+= 1

print(f"{course}: {count} days")