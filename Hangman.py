import random
def hangman():
    list_of_words = ["eduyear","hangman","india","laptop"]
    word=random.choice(list_of_words)
    turns=10
    guessmade = ' '
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word =""

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word==word:
            print(main_word)
            print("you won the Game!!!!")
            break
        print("guess the word",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter the valid character")
            guess=input()
        if guess not in word:
            turns=turns-1     
            if turns==9:
                print("9 turns is left")
                print("-------------------")
            if turns==8:
                print("8 turns is left!!!!" )
                print("-------------------")
                print("       O       ")
            if turns==7:
                print("7 turns is left!!!!" )
                print("-------------------")
                print("       O       ")
                print("       |       ")
            if turns==6:
                print("6 turns is left!!!!" )
                print("-------------------")
                print("       O       ")
                print("       |       ")
                print("       /       ")
            if turns==5:
                print("5 turns is left!!!!" )
                print("-------------------")
                print("       O        ")
                print("       |        ")
                print("      / \       ")
            if turns==4:
                print("4 turns is left!!!!" )
                print("-------------------")
                print("       \O        ")
                print("        |        ")
                print("       / \       ")
            if turns==3:
                print("3 turns is left!!!!" )
                print("-------------------")
                print("       \O/       ")
                print("        |        ")
                print("       / \       ")
            if turns==2:
                print("2 turns is left!!!!" )
                print("-------------------")
                print("       \O/ |      ")
                print("        |        ")
                print("       / \       ")
            if turns==1:
                print("1 only one turns is left!!!! hangman on his last breath" )
                print("-------------------")
                print("       \O/_|      ")
                print("        |        ")
                print("       / \       ")
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print("this was the word:",word)
                print("-------------------")
                print("        O_|      ")
                print("       /|\       ")
                print("       / \       ")
                break
            
          

            


name=input("ENTER A NAME =")
print("welcome",name,"=.....")
print("--------------------"
)
print("try to guess the word  you have a 10 chance")
hangman()