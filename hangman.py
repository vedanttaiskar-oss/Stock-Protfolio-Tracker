import random

word_list = [ "algorithm", "compiler", "database", "network", "software",
             "hardware", "internet", "keyboard", "variable", "function",
             "iteration", "recursion", "debugging", "bandwidth", "firewall",
             "protocol", "syntax", "runtime", "pointer", "boolean",
             "interface", "framework", "threading", "encryption", "memory",
             "processor", "assembly", "binary", "cache", "stack",
             "queue", "linked", "sorting", "searching", "array",
             "object", "class", "inheritance", "polymorphism", "abstraction",
             "operating", "virtual", "machine", "terminal", "command",
             "repository", "version", "control", "deployment", "testing"]

hangman_stages = [
    """
   -----
   |   |
       |
       |
       |
       |
--------""",
    """
   -----
   |   |
   O   |
       |
       |
       |
--------""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
--------""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
--------""",
    """
   -----
   |   |
   O   |
  /|\  |
       |
       |
--------""",
    """
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
--------""",
    """
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
--------""",
]

def play_hangman():
    secret_word = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = []
    max_wrong = 6

    while True:
        wrong_count = len(wrong_guesses)
        print(hangman_stages[wrong_count])

        display_word = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print(f"\nWord: {display_word}")
        print(f"Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"Chances left: {max_wrong - wrong_count}")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nYou Win! The word was: '{secret_word}'")
            break

        if wrong_count >= max_wrong:
            print(f"\nGame Over! The word was: '{secret_word}'")
            break

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one letter!")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("Already guessed!")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            wrong_guesses.append(guess)
            print("Wrong!")

    again = input("\nPlay again? (yes/no): ").lower()
    if again == "yes" or again == "y":
        play_hangman()
    else:
        print("Thanks for playing!")

play_hangman()