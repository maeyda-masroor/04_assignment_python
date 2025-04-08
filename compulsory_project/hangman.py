import random
import string
words = ["apple", "balloon", "cat", "door", "elephant", "fan", "grass", "high", "icecream", 
         "jug", "kangaroo", "lemon", "mango", "nuts", "orange", "pear", "queen", "rock", 
         "sun", "uniform", "year", "zebra"]

def get_valid_word(words):
    word = random.choice(words).upper()  # Convert word to uppercase
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()  # Ensure no spaces or dashes
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of valid uppercase letters
    used_letters = set()  # Letters guessed by the user

    while len(word_letters) > 0:
        # Show used letters
        print("You have chosen these letters:", ", ".join(used_letters))
        
        # Show current progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_list))  # Fixed incorrect string join
        
        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:  # New valid letter
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:  # Already guessed letter
            print("You already guessed that letter!")
        else:  # Invalid input
            print("Invalid character. Please enter a letter.")

        # Check if the game is won
        if len(word_letters) == 0:
            print("Congratulations! You guessed the word:", word)
            break

hangman()
