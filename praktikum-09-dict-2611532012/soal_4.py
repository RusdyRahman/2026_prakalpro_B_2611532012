all_students = input("Input Data Siswa: ").split()
students = set(all_students)
all_submitted = input("Input Data Siswa yang telah selesai: ").split()
submitted = set(all_submitted)

Not_Submitted = students - submitted

print("Submitted :", len(submitted), "students" )
print("Not submitted :", len(Not_Submitted), "students")

for number in students:
    if number not in submitted:
        print((number))
