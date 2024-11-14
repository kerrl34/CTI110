# Liam Kerr
# 11-14-2024
# Norris
# P4Lab2
# CTI 110
# Ask for a number that is 0 or higher


'''count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1
print("Done")



# input validation
num = int(input("Type a number from 1 to 3"))
while num < 1 or num > 3:
    print("Please try again")
    num = int(input("Type a number from 1  to 3:"))
print("You entered: ", num)'''



def times_table():
    num = int(input("Enter an integer: "))
    while (num < 0):
        print("No negative numbers please.")
        num = int(input("Enter an integer: "))
    print("You entered: ", num)

    for num2 in range(1,13):
        answer = num * num2
        print(num, "*", num2, "=", answer)
        

def main():
    times_table()
    again = input("Do you want to run the program again? ")
    while (again == "yes" or again=="Yes"):
        times_table()
        again = input("Do you want to run the program again? ")
    print("Goodbye!")
        

# Start the program
main()

