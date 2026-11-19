number_of_rows = 4
seats_per_row = 5
# Write your code below

seating = []
for i in range(number_of_rows):
    row = []
    for j in range(seats_per_row):
        row.append(".")
    seating.append(row)

while True:
    # Tampilkan denah
    for i in range(number_of_rows):
        print(f"Row {i + 1}:", " ".join(seating[i]))

    row_num = int(input("Row (0 to stop): "))
    if row_num == 0:
        break

    seat_num = int(input("Seat: "))

    if row_num < 1 or row_num > number_of_rows or seat_num < 1 or seat_num > seats_per_row:
        print("Invalid seat.")
    elif seating[row_num - 1][seat_num - 1] == "X":
        print("Seat already taken.")
    else:
        seating[row_num - 1][seat_num - 1] = "X"
        print("Seat booked.")

# Hitung kursi yang terisi
taken = 0
for i in range(number_of_rows):
    for j in range(seats_per_row):
        if seating[i][j] == "X":
            taken += 1

print(f"Seats taken: {taken}")