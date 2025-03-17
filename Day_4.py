rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rps = [rock, paper, scissors]
rps_dictionary = {"rock":rock, "paper":paper, "scissors":scissors}
computer_choice = random.choice(rps)
choice = input("Rock, Paper, Scissors! What do you choose?\n").strip().lower()
if choice in rps_dictionary:
    print("You chose: " + rps_dictionary[choice])
    print("Computer chose: " + computer_choice)
else:
    print("invalid choice!")
if computer_choice == choice:
    print("DRAW!")
if "rock" in choice:
    if computer_choice == scissors:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif "paper" in choice:
    if computer_choice == rock:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif "scissors" in choice:
    if computer_choice == paper:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
