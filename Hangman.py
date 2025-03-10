from random import *
from words import *

def select_random_word(words):
    '''
    chooses random words from the words.py file
    :param words: list/file of random words
    :return: a random word from the list
    '''
    return choice(words)

secret_word = select_random_word(words)
def hangman(secret_word):
    '''
    the classic word based hangman game
    :param secret_word: the secret word guessed by the computer
    :return: if the user won the game or not
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.") # gives the user hint about the length of the word
    guesses = 6 # initialize the no.of guesses to 6
    letters_guessed = [] # initialize an empty list of letters guessed by user
    word_list = list(secret_word) # create a list of alphabets of the secret word

    while guesses != 0 and set(letters_guessed) != set(word_list): # while loop for iterating until user wins or looses
        print("You have", guesses, "guesses remaining.") # informs the user about the number of guesses remaining
        letter_guessed = input("Guess a letter: ") # user input for a letter
        if letter_guessed in word_list: # checks if the letter guessed by user is in the secret word
            letters_guessed.append(letter_guessed) # add the letter guessed in the list of letters guessed
            print("Good guess.")  # informs the user that his/her guess was correct
        else:
            if letter_guessed in letters_guessed: # checks if the letter is already in the list
                print("You have already guessed that letter.") # informs the user that the guessed letter is already in the list
            else:
                print("Not a valid guess.") # else inform the user that his/her guess was not valid
            guesses -= 1 # decrease guesses by 1 as penalty for invalid guess

        # Display the current state of the word
        display_word = ""
        for letter in word_list:
            if letter in letters_guessed:
                display_word += letter
            else:
                display_word += "_ "
        print("Current word:", display_word)

        if guesses <= 0:  # if user ran out of guesses, he/she looses
            print("Sorry, you ran out of guesses.The word was",secret_word)
            break
        if set(letters_guessed) == set(word_list): # if the user guesses all the letters of the word, he/she wins
            print("You won the game! The word was", secret_word)


hangman(secret_word)