MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Prompt user (espresso/latte/cappuccino
def prompt():
    off = False
    while not off:
        user_selection = input("What would you like to drink? (espresso/latte/cappuccino)\n")
        # add off to prompt to turn off machine
        if user_selection == "off":
            off = True
        # print report that shows resource values (water/milk/coffee/money)
        elif user_selection == "report":
            print(resources)
        elif resources_sufficient(user_selection):
            process_coins(user_selection)


# Check if resources sufficient
def resources_sufficient(user_selection):
    #import ipdb; ipdb.set_trace()
    if resources["water"] >= MENU[user_selection]["ingredients"]["water"]:
        if user_selection == "espresso" or resources["milk"] >= MENU[user_selection]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[user_selection]["ingredients"]["coffee"]:
                return True
            else:
                print("Insufficient resources machine requires servicing")
                exit()
        else:
            print("Insufficient resources machine requires servicing")
            exit()
    else:
        print("Insufficient resources machine requires servicing")
        exit()

# Process coins
def process_coins(user_selection):
    print(f"Your total is {MENU[user_selection]["cost"]:.2f}. Please insert change.")
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickles = input("Nickles: ")
    pennies = input("Pennies: ")
    total = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) % 0.01)
    change = total - MENU[user_selection]["cost"]
    # check if transaction successful
    if total == MENU[user_selection]["cost"]:
        print("Transaction approved.")
        make_coffee(user_selection)
    elif total > MENU[user_selection]["cost"]:
        print(f"Transaction approved. Here is your change: {change:.2f}")
        make_coffee(user_selection)
    else:
        print("Incorrect amount. Refund issued.")

# make a coffee
def make_coffee(user_selection):
    # subtract resources
    resources["water"] -= MENU[user_selection]["ingredients"]["water"]
    if user_selection != "espresso":
        resources["milk"] -= MENU[user_selection]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_selection]["ingredients"]["coffee"]
    print(f"Here is your {user_selection} enjoy!")

prompt()