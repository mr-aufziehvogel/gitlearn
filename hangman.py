import random
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def randomword():
    lines = open('words2.txt').read().splitlines()
    myline = random.choice(lines)
    return myline

def win():
    while True:
        to_continue = input("Gewonnen! Neues Spiel? ")
        if to_continue == "j" or to_continue == "J":
            newgame()
            break
        elif to_continue == "n" or to_continue == "N":
            exit()

def lose():
    while True:
        to_continue = input("Verloren :( Neues Spiel? ")
        if to_continue == "j" or to_continue == "J":
            newgame()
            break
        elif to_continue == "n" or to_continue == "N":
            exit()

def richtig(j):
    solved[j] = word[j]
    if solved == list(word):
        global mistakes
        mistakes = 0
        win()

def check_correctness(guess,word):
#    print(str(word) + "\n")
    i = -1
    w = 0
    for letter in word:
        i += 1
        if letter == guess:
            richtig(i)
        else:
            w += 1
    if w == len(word):
        global mistakes
        mistakes = mistakes + 1
    
    if mistakes == 5:
        clear()
        print("FEHLVERSUCHE: " + str(mistakes) + "/5\n")
        mistakes = 0
        lose()
    else:
        clear()
        print("FEHLVERSUCHE: " + str(mistakes) + "/5\n")



def play():
    while True:
        buchstabe = input("Gib einen Buchstaben ein: ")
        if len(buchstabe) == 1 and buchstabe.isalpha() == True:
            check_correctness(buchstabe.upper(),letters)
            print(*solved)

      
def newgame():
    global word
    global letters
    global solved
    word = randomword()
    letters = list(word)
    solved = []
    for i in range(len(word)):
        solved.append("_")
    clear()
    print("FEHLVERSUCHE: " + str(mistakes) + "/5\n")
    print(*solved)
    play()

global solved
global word
global letters
global mistakes
mistakes = 0

clear()
print("----- HANGMAN -----\n")
x = input("Enter drücken")
newgame()
while True:
    play()