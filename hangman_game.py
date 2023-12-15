import random
def choose_word():
    words = ["red","green","blue","pink"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_game():
    chosen_word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("Attempts left:", attempts)
        current_display = display_word(chosen_word, guessed_letters)
        print("Current word:", current_display)

        guess = input("guess a letter: ")

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guess that")
            elif guess in chosen_word:
                print("very good you guess")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts -= 1
                guessed_letters.append(guess)
       

        if "_" not in display_word(chosen_word, guessed_letters):
            print("You guessed the word:", chosen_word)
            break

    if attempts == 0:
        print(" You lost the game")
hangman_game()