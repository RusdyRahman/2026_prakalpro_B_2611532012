menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
d = 2 
sales = [
    [15, 12, 12 ],
    [13, 14, 10 ],
    [12, 12, 10 + d]
]
# Write your code below

print("Total per Day")
for i in range(number_of_days):
    total_day = 0
    for j in range(len(menus)):
      total_day += sales[i][j]
    print(f"Day: {i+1}: {total_day}")

menu_totals = []
for j in range (len(menus)):
    total_menu = 0
    for i in range(number_of_days):
       total_menu += sales[i][j]
    menu_totals.append ((menus[j], total_menu))
print("Total per Menu :", menu_totals)

best_name = ""
best_total = -1
for name, total in menu_totals:
   if total > best_total:
    best_name = name
    best_total = total
print(f"Best Seller: {best_name} {best_total}")