# import random, art, and data
import random
import art
import game_data

# score
score = 0

# define prompt
def prompt(previous_winner=None):
    # art
    print(art.logo)
    # random selection (random.choice(game_data.data))
    # use higher from prior prompt
    if previous_winner:
        a = previous_winner
    else:
        a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    # re-roll if same choice is picked for A and B
    while a == b:
        b = random.choice(game_data.data)
    # compare A: name, description, country
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    # art
    print(art.vs)
    # against B:
    print(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}")
    return a, b

# define higher or lower logic
def higher_lower(a, b):
    # get follower_count
    if a["follower_count"] > b["follower_count"]:
        winner = a
    else:
        winner = b
    return winner

# define game
def game():
    global score
    game_over = False
    a, b = prompt()
    while not game_over:
        winner = higher_lower(a, b)
        selection = input("Who do you think has the bigger following? choose 'A' or 'B': ").upper().strip()
        if selection == "A" and winner == a:
            score += 1
            print("\n" * 20)
            print(f"Correct! Your score: {score}")
            prompt(a)
        elif selection == "B" and winner == b:
            score += 1
            print("\n" * 20)
            print(f"Correct! Your score: {score}")
            prompt(b)
        else:
            print(f"Incorrect! Better luck next time! Score: {score} ")
            return


game()
