import random
from hangman_art import word_list # List of words for the game
from hangman_art import HANGMANPICS # ASCII art for the hangman stages

# Randomly select a word from the list
chosen_word = random.choice(word_list)

lives = 6 # Initial number of lives
placeholder = ""
word_length = len(chosen_word)

# Create the initial placeholder (e.g., "_____")
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = [] # Stores letters that are correct and revealed in the word
used_letters = [] # Stores all letters guessed so far

# Main game loop
while not game_over:
    guess = input("Enter a letter: ").lower()

    # Initialize the display for the current turn
    display = ""

    # Check the guessed letter against the chosen word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            # Add the letter to correct_letters and used_letters only once per guess to track what has been revealed and what has been used
            if guess not in correct_letters:
                correct_letters.append(guess)
            if guess not in used_letters:
                used_letters.append(guess)
        elif letter in correct_letters:
            display += letter # Keep letters that were already correctly guessed
        else:
            display += "_" # Unrevealed letter

    print(display)
    print(f"Used letters are: {used_letters}") # Show all letters guessed

    # If the guess is wrong
    if guess not in chosen_word:
        lives -= 1 # Decrement lives
        print(f"-1 life. Lives: {lives}")
        # Add the incorrect guess to used_letters only if it hasn't been added yet (handles the case where the letter is added in the loop above if it was correct)
        if guess not in used_letters:
            used_letters.append(guess)

        # Check for game loss
        if lives == 0:
            print("Game Over! No lives remaining.")
            game_over = True

    # Check for game win (no underscores left in the display)
    if "_" not in display:
        game_over = True
        print("Congratulations! You Won.")

    # Print the current hangman image corresponding to the remaining lives
    print(HANGMANPICS[lives])
