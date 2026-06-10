import random

# List of words for the game
word_list = ["u.no", "ludo", "chess", "foot ball", "cricket"]

# Select a random word
secret_word = random.choice(word_list)

# Store guessed letters
guessed = []

# Number of chances
chances = 6

print("Welcome to Hangman Game")

while chances > 0:

    display = ""

    # Show guessed letters and hide remaining letters
    for letter in secret_word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completed
    if "_" not in display:
        print("Congratulations! You guessed the word:", secret_word)
        break

    user_letter = input("Enter a letter: ").lower()

    # Check if already guessed
    if user_letter in guessed:
        print("You already entered this letter.")
        continue

    guessed.append(user_letter)

    # Check correct or wrong guess
    if user_letter not in secret_word:
        chances -= 1
        print("Wrong guess!")
        print("Remaining chances:", chances)

# If all chances are over
if chances == 0:
    print("\nGame Over")
    print("The correct word was:", secret_word)