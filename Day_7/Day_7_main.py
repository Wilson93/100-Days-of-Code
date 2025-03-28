import random
import hangman_art
import hangman_words
# Update the word list to use the 'word_list' from hangman_words.py

lives = 6
word_list = hangman_words.word_list

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""
    if guess in correct_letters:
        print("Youve already guessed that!")
        continue
    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

    print("Word to guess: " + display)

    #  If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess you loose a life!")
        if lives == 0:
            game_over = True

            # Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"Your word was {chosen_word}!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
