#CTI 110
#P1HW1 - Calculator
#Norris
#10-3-24


#num=int(input("Enter the integer as the base value: "))
print("-" * 5, "Calculating Exponents", "-" * 5)
x = int(input('Enter an integer as the base value: '))
y = int(input("Enter an integer as the exponent: "))
c = x ** y
print(x,"raised to the power of", y, "is", c,"!!")

print("-" * 5, "Addition and Subtraction", "-" * 5)

start_integer = int(input("Enter a starting integer:"))
add_integer = int(input("Enter an integer to add:"))
sub_integer = int(input("Enter an integer to subtract:"))
final_answer = start_integer + add_integer - sub_integer
print(start_integer,"+", add_integer, "-", sub_integer, "is equal to:", final_answer)



