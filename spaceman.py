#Project 5
#Spaceman Game
#Template created by: Lindsay Jamieson
#Sam Treadwell
#10/31/2022

import random

def pick_random_word():
    words = ['smile', 'pineapple', 'kangaroo', 'laugh', 'family', 'umbrella', 'drink', 'taste', 'gecko', 'trash', 'amazing', 'elephant', 'piano', 'fuzzy', 'sauce', 'jelly', 'bingo', 'floppy', 'hyper', 'crazy']
    choose = random.choice(words)
    return choose

def create_hidden_word():
    random_word = pick_random_word()
    hidden_word = len(random_word) * ["*"]
    return hidden_word, random_word

def word_found(random_word, hidden_word):
    return ''.join(hidden_word) == random_word

def replace_character(random_word, hidden_word, guess):
    random_word = list(random_word)
    hidden_word = list(hidden_word)
    counter = 0
    while counter < len(hidden_word):
        if guess == random_word[counter]:
            hidden_word[counter] = guess
        counter += 1
    hidden_word = ''.join(hidden_word)
    return hidden_word

def main():
    print("-----------------------------------------------------------------------")
    print("WELCOME TO SPACEMAN: THE HIDDEN WORD GAME!")
    print("")
    print("Your goal is to uncover the hidden word")
    print("Guesses with the correct letters will reveal letters in the hidden word")
    print("You have 5 guesses to reveal the hidden word")
    print("-----------------------------------------------------------------------")
    print("Below you will see the HIDDEN WORD:")

    hidden_word, random_word = create_hidden_word()
    print(hidden_word)

    counter = 0
    while counter < 5:
        guess = str(input("\nGuess a character in the hidden word: "))

        while not guess.isalpha():
            new_guess = str(input("\nPlease guess an alphabetical character in the hidden word: "))
            guess = new_guess

        if guess in random_word:
            print("\nYour guess WAS in the hidden word")
            print(f"\nYou have {5 - counter} guesses left")
            hidden_word = replace_character(random_word, hidden_word, guess)

        else:
            counter += 1
            print("\nYour guess WAS NOT in the hidden word")
            print(f"\nYou have {5 - counter} guesses left")
            hidden_word = replace_character(random_word, hidden_word, guess)

        print(hidden_word)

        if hidden_word == random_word:
            print("\nYou guessed the hidden word!")
            break

    else:
        print("\nYou are out of guesses!")

if __name__ == "__main__":
    main()