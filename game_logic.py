from ascii_art import STAGES
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for guesses
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

         #checks for correctness
        if guess in secret_word:
            print(f"You guessed the letter {guess}.")
        else:
            mistakes += 1
            print("Sorry, that's wrong.")



        if guess in guessed_letters:
            print("You already guessed the letter:", guess)
            continue
        guessed_letters.append(guess)

          #checks win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations, you saved the snowman!")
            print("The secret word was:", secret_word)
            break

         #Checks loss condition
        if mistakes >= max_mistakes:
            print(STAGES[-1])
            print("Sorry, the snowman melted!.")
            print("The secret word was:", secret_word)
            break

        display_game_state(mistakes, secret_word, guessed_letters)