nama = "muhammad rusdy rahman"
nim = "2611532012"
clean = nama.strip()
space = clean.find(" ")

if space == -1:
    nama_pertama = clean
else:
    nama_pertama = clean[:space]
username = nama_pertama.lower() + nim[-3:]
intake = nim[-4:-2] + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ":" + nama.title())
print("NIM".ljust(10) + ":" + nim)
print("Username".ljust(10) + ":" + username)
print("Intake".ljust(10) + ":" + intake)
print("=" * 30)