height = int(input("Enter Height:"))

for row in range (1, height + 1):
    for column in range (height - row + 1):
        print("*", end=" ")
    print()