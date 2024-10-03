#CTI 110
#P1LAB2 - Receipt
#Norris
#10-1-24

print("P1Lab2")
#For today, lets do a restaurant that only sells burgers and fries

num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 0.99
sales_tax = .07


print("Can I take your order?")

num_burgers = int(input ("How many burgers would you like? "))
print("You ordered", num_burgers, "burgers")

num_fries = int(input("How many fries? "))
print("Okay, that's", num_fries, "fries")

burger_total= num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = (burger_total + fry_total)
sales_tax = sales_tax * meal_total
total_ptax = sales_tax + meal_total
print("-" * 20)
print(num_burgers, "🍔 burger(s)\t$", format (burger_total,".2f"))
print(num_fries, "🍟 fries\t\t$", format(fry_total, ".2f"))
print("-" * 20)
print("Tax: $ ", format(sales_tax, ".2f"))
print("Total\t\t$",format(sales_tax + meal_total, ".2f"))
