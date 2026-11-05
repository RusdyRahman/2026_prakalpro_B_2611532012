total = 0

while True:
    bil = int(input("Enter a number: "))
    if bil < 0:
        break
    if bil == 0:
        continue
    print("Positive number:", bil)
    total += bil

print("Total:", total)