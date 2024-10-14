 # Liam Kerr
 # 10-11-24
 # P2HW2
 # This program  does some basic math on numbers that are entered

    #// Step 1: Ask user to enter their budget
    #PRINT "Enter your budget: "
    #INPUT budget

    #// Step 2: Ask user to enter travel destination
    #PRINT "Enter your travel destination: "
    #INPUT destination

    #// Step 3: Ask user for amount they will spend on gas
    #PRINT "Enter the amount you will spend on gas: "
    #INPUT gas_expense

    # Step 4: Ask user for amount they will spend on accommodation/hotel
    #PRINT "Enter the amount you will spend on accommodation/hotel: "
    #INPUT accommodation_expense

    #// Step 5: Ask user for amount they will spend on food
    #PRINT "Enter the amount you will spend on food: "
    #INPUT food_expense

    #// Step 6: Add expenses
    #total_expenses = gas_expense + accommodation_expense + food_expense

    #// Step 7: Subtract expenses from budget
    #remaining_budget = budget - total_expenses

    #// Step 8: Display results
    #PRINT "------------ Travel Expenses ------------"
    #PRINT "Travel Destination: " + destination
    #PRINT "Total Expenses: $" + total_expenses
    #PRINT "Remaining Budget: $" + remaining_budget



budget = float(input("Enter your budget: "))


destination = input("Enter your travel destination: ")


gas_expense = float(input("Enter the amount you will spend on gas: "))


accommodation_expense = float(input("Enter the amount you will spend on accommodation/hotel: "))


food_expense = float(input("Enter the amount you will spend on food: "))


total_expenses = gas_expense + accommodation_expense + food_expense


remaining_budget = budget - total_expenses

print("------------ Travel Expenses ------------")
print(f"\nTravel Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

