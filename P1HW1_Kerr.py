# Liam Kerr
# 10-10-24
# P1HW1
# This program calculates exponents and addition and subtraction



print("----- Calcuating Exponents -----")


base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))

exponent_total = base_value**exponent_value


print(base_value, "raised to the power of", exponent_value, "is", exponent_total)


print("----- Addition and Subtraction -----")

starting_integer = int(input("Enter a starting integer: "))
adding_integer = int(input("Enter an integer to add: "))
subtracting_integer = int(input("Enter an integer to subtract: "))
add_total = starting_integer + adding_integer - subtracting_integer

print(starting_integer, "+", adding_integer, "-", subtracting_integer, "=", add_total)






