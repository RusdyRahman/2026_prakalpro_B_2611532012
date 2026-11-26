all_student = input("Input Data Siswa: ").split()
student = set(all_student)
all_submitted = input("Input Data Siswa yang telah selesai: ").split()
submitted = set(all_submitted)

Not_Submitted = student - submitted

print("Submitted :",len(submitted), "students" )
print("Not submitted :", len(Not_Submitted), "students")

for number in student:
    if number not in submitted:
        print((number))
