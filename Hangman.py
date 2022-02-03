import string
from word import choose_word
from images import IMAGES


name=input("enter your name = ")
print("welcome to the game Hangman ! ",name)

def get_guessed_word(secret_word, letters_guessed):
    guess=""
    for i in secret_word:
        if i in letters_guessed:
            guess+=i
        else:
            guess+="_"
    return guess

def get_available_letter(letter_guessed):
    letters_left = string.ascii_lowercase
    for i in letter_guessed:
        letters_left=letters_left.replace(i," ")

    return letters_left


def hangman(secret_word):
    letters_guessed=[]
    remaining_lives=len(secret_word)
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print(" ")
    # print(secret_word)

    while remaining_lives>0:
        print(" You have chance to guess word is :- ",remaining_lives)
        print(" ")
        guess = input("Please guess a letter :- ")
        letter = guess.lower()
        if len(letter)>1 or not letter.isalpha():
            print("Invalid letter")
        else:
            if letter in secret_word:
                letters_guessed.append(letter)
                guess_letter=get_guessed_word(secret_word, letters_guessed)
                print("good guess: "+ guess_letter)
                print("Available letters: " + get_available_letter(letters_guessed))
                if guess_letter==secret_word:
                    break

        
            else:
                print("Oops!, That letter is not in word ________")
                print(IMAGES[8-remaining_lives])
                remaining_lives-=1
                print("Available letters: " + get_available_letter(letters_guessed))

    if secret_word==guess_letter:
        print("you win !!!!")
    else:
        print("you lose !!!!")

secret_word = choose_word()

hangman(secret_word)