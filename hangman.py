import random

# List of predefined words
words = ["python", "apple", "banana", "orange", "school"]

# Choose a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=== Welcome to Hangman ===")

while incorrect_guesses < max_attempts:
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")

# Game over if attempts are exhausted
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)