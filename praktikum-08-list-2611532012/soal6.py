LAST_DIGIT = 2  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = [ 31500, 42000, 33500, 36500, 29000, 38500, 34500]
# Write your code below

for i in range (len(expenses)):
   print(f"Day{i+1}: {expenses[i]}")
total = 0
highest = expenses[0]
days_above = 0
highest_day = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day += 1
    if expenses[i] > daily_limit:
        days_above += 1
avarage = (total/len(expenses))

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Avarage: {avarage:.1f}")
print(f"Highest: day {highest_day + 1} ({highest})")
print(f"Days above limit: {days_above}")
