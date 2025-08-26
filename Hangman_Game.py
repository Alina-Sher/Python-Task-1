# TASK 1: Hangman Game
# - 5 predefined words
# - 6 incorrect guesses allowed
# - plain console I/O, no graphics or emojis

import random

def choose_word(words):
    """Allow user to pick a test word or use a random one."""
    print("Choose mode:")
    print("  R - Random word")
    print("  T - Test a specific word from the predefined list (useful for checking behavior)")
    choice = input("Enter R or T (default R): ").strip().lower()

    if choice == "t":
        print("\nPredefined words:")
        for i, w in enumerate(words, start=1):
            print(f"  {i}. {w}")
        sel = input("Enter the number of the word to use (1-{}), or press Enter for random: ".format(len(words))).strip()
        try:
            idx = int(sel)
            if 1 <= idx <= len(words):
                return words[idx - 1]
        except Exception:
            pass

    # default: random
    return random.choice(words)

def hangman():
    words = ["apple", "table", "chair", "house", "water"]  # 5 predefined words
    word = choose_word(words)
    word = word.lower()

    guessed_letters = set()   # letters guessed so far
    wrong_letters = set()     # wrong guesses
    attempts_left = 6

    print("\nWelcome to Hangman Game!")
    print(f"The word has {len(word)} letters.\n")

    # current display as list of characters (underscore for unknown)
    display = ["_"] * len(word)

    while attempts_left > 0 and "_" in display:
        # show current state
        print("Word:      ", " ".join(display))
        if guessed_letters:
            print("Guessed:   ", " ".join(sorted(guessed_letters)))
        else:
            print("Guessed:    (none)")
        print("Attempts left:", attempts_left)

        # get input
        guess = input("Enter a letter: ").strip().lower()

        # validation: must be a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).\n")
            continue

        # already guessed?
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # record the guess
        guessed_letters.add(guess)

        # check if letter is in word; reveal all occurrences
        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    display[i] = guess
            print("Correct guess!\n")
        else:
            wrong_letters.add(guess)
            attempts_left -= 1
            print("Wrong guess! Attempts left:", attempts_left, "\n")

    # result
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
