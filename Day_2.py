print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10 12 15 "))
tip = (percentage / 100) * bill
people = int(input("How many people to split the bill? "))
print(round((bill + tip) / people, 2))