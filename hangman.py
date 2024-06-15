import random

def generate_word():
    fruits = ["apple", "banana", "orange", "mango", "grapefruit"]
    return random.choice(fruits)

def display_board(guessed_letters, secret_word):
    word_display = []
    for letter in secret_word:
        if letter in guessed_letters:
            word_display.append(letter)
        else:
            word_display.append("_")
    print("Current word: " + " ".join(word_display))

def play_game():
    secret_word = generate_word()
    guessed_letters = []
    wrong_guesses = 6

    print("Welcome to Hangman!")
    print("You have", wrong_guesses, "wrong guesses left.")

    while wrong_guesses > 0:
        display_board(guessed_letters, secret_word)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses -= 1
            print("Incorrect guess. You have", wrong_guesses, "wrong guesses left.")
        else:
            print("Good guess!")

        # Check if all letters in the secret word have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            display_board(guessed_letters, secret_word)
            print("Congratulations! You guessed the word", secret_word)
            return

    display_board(guessed_letters, secret_word)
    print("You lost! The word was", secret_word)

if __name__ == "__main__":
    play_game()
