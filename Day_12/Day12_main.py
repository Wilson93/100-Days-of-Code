import art
import random
print(art.logo)

#def guess
def guess():
    global lives
    computer_number = random.randint(1, 100)
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        player_guess = input("Make a guess:")
        if int(player_guess) > int(computer_number):
            print("Too high.\nGuess again.")
            lives -= 1
            continue
        elif int(player_guess) < int(computer_number):
            print("Too low.\nGuess again.")
            lives -= 1
            continue
        elif int(player_guess) == int(computer_number):
            print("Correct you win!")
            exit()
    print(f"You have {lives} lives remaining! GAME OVER!")
    exit()

# welcome msg
print("Welcome to the Number Guessing Game!")

# thinking of num
print("I'm thinking of a number between 1 and 100")

# choose difficulty
difficulty = (input("Choose a difficulty type 'easy' or 'hard':")).lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid Input")
    exit()

#guess
guess()