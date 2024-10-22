#CTI 110
#P3Lab1
#Kerrl
#10-22-24

def main():
    print("Choose Your Own Adventure")
    go_home()

def go_home():
    print("You decided to go home.")
    print("But should you get some food?")
    print("1. Get tacos from local food truck")
    print("2. Get Chinese")
    choice = int(input())
    if choice == 1:
        get_mexican()
    elif choice == 2:
        get_chinese()

def get_mexican():
    print("You went to get tacos from a local food truck.")

def get_chinese():
    print("You ordered chinese food.")

# the user wanted mexican
def get_mexican():
    print("You arrived at the food truck, it's running but there is no one inside.")
    print("What do you want to do?")
    print("1. Check the area")
    print("2. Leave and go back home.")
    choice = int(input())
    if choice == 1:
            check_area()
    elif choice == 2:
            leave_area()


def leave_area():
    print("You went home and survived!")

def check_area():
    print("You went around the side and noticed that the door is open and there is blood smeared across the ground.")
    print("Do you want to continue looking?")
    print("1. Yes")
    print("2. No and go home")
    choice = int(input())
    if choice == 1:
        keep_looking()
    elif choice == 2:
        leave_area()

def keep_looking():
    print("You noticed that the blood leads to a nearby alley and you follow it.")
    print("BOOOM!, you hear a loud bang from inside the closest building and see that the back door is still open.")
    print("Do you want to check it out?")
    print("1. Yes")
    print("2. No, I want to go home.")
    choice = int(input())
    if choice == 1:
        go_inside()
    elif choice == 2:
        leave_area()

def go_inside():
        print("You see a man wearing a pig mask chopping up the food truck owner.")
        print("Do you (call out) to the man wearing the mask or (run away)?")
        choice = input()
        if choice == "call out":
            call_out()
        elif choice == "run away":
            leave_area()

def call_out():
    print("The man turned around and killed you.")
    print("The end.")
            



# start the program
main()

