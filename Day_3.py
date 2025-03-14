print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Runescape.")
print("Your mission is to beg for gold at the GE.")
while True:
    choice = input("You cross the Lumbridge Bridge. Go left past the cow pen or right into Al-Kharid?\n").strip().lower()
    if "right" in choice:
        print("You dont have enough money! BACK TO LUMBRIDGE!")
    elif "left" in choice:
        print("You walk past the Lumbridge cows and chickens")
        choice = input("You see the Varrock gates go straight into the gates or left and around?\n").strip().lower()
        if "straight" in choice:
            print("You get blasted back a dark wizard! BACK TO LUMBRIDGE!")
        elif "left" in choice:
            print("You narrowly avoid the wizards as you make your way to Gertrudes house!")
            choice = input("As you make your way to the gates of the GE a noob in ranger boots appears and sends you a trade offer. do you accept or decline\n").strip().lower()
            if "accept" in choice:
                print("It's Trevor! and he scams you for all your worth! BACK TO LUMBRIDGE!")
            elif "decline" in choice:
                print("GZ! you made it all the way to the GE! Thanks for playing!")
                exit()
    else:
        print("Incorrect input.")

