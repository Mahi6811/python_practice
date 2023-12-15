import random

def choose_word():
    topics = ["programming", "python", "hangman", "list", "loop", "function"]
    return random.choice(topics)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        print("Attempts left: ", attempts_left)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess.")
            attempts_left -= 1
        else:
            print("Correct guess!")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
