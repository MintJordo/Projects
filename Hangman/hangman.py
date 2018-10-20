import random
import os
import sys

# Display the board
def board(name, y):
    numSpaces = len(word)
    print('------------------------------')
    if(name == 'Original Board'):
        print(name)
    else:
        print(f'Player: {name} - Lives: {y}')
    print('\n')
    for char in word:
            if char in lettersGuessed:
                print(char, sep=" ", end=" ", flush=True)
                numSpaces -= 1
            else:
                print('_', sep=" ", end=" ", flush=True)
    print('\n')
    if not gameOver:
        print('Letters used:', sep=" ", end=" ", flush=True)
        for char in lettersGuessed:
            print(char, sep=" ", end=" ", flush=True)
        print('\n')
    print('------------------------------')
    return numSpaces

# Clears the screen after the user enters something
def clearScreen():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

# Picks a random line from my text file for the word
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "hangman_words.txt")
select_word = open(path).read().splitlines()
word = random.choice(select_word)

# Initialization of variables
MAX_PLAYERS = 5
playerInfo = {'d1':{},
             'd2':{}}
lettersGuessed = ""          
gameOver = False
totalLives = 0

# Input validation for entering the number of users
while True:
    try:
        j = int(input("How many players (5 max): "))
    except ValueError:
        print("Not valid input. How many players (5 max): ")
        continue
    else:  
        while j > MAX_PLAYERS or j < 1:
            j = int(input("Not a valid integer. How many players (5 max): "))
        break

for i in range(1, j+1):
    name = input("Name: ")
    print(f"Welcome {name}!")
    playerInfo['d1'][i] = name
    playerInfo['d2'][i] = 3
    totalLives += playerInfo['d2'][i]
print(word)
board("Original Board", playerInfo['d2'][1])

# The gameplay code
while not gameOver:
    if totalLives == 0:
        gameOver = True
        print(f"The game is over. No one guessed the correct word, {word}")
    else:
        for i in playerInfo['d1']:
            if playerInfo['d2'][i] == 0:
                print(f"Sorry, {playerInfo['d1'][i]}, you are out of lives and cannot play anymore.")
            else:
                guess = input(f"{playerInfo['d1'][i]}, guess a letter/word: ").lower()
                if guess not in lettersGuessed and guess.isalpha():
                    clearScreen()

                while not guess.isalpha():
                    guess = input(f"Input can only be letters. {playerInfo['d1'][i]}, guess again: ").lower()
                if guess not in lettersGuessed and guess.isalpha():
                    clearScreen()

                if len(guess) != 1:
                    if(guess == word):
                        gameOver = True
                        lettersGuessed += guess
                        board(playerInfo['d1'][i], playerInfo['d2'][i])
                        print(f"Congrats, {playerInfo['d1'][i]}, you won the game!")
                        sys.exit()
                    else:
                        playerInfo['d2'][i] -= 1
                        totalLives -= 1
                        board(playerInfo['d1'][i], playerInfo['d2'][i])
                else:
                    if guess not in lettersGuessed:
                        if guess not in word:
                            playerInfo['d2'][i] -= 1
                            totalLives -= 1
                        lettersGuessed += guess
                        numSpaces = board(playerInfo['d1'][i], playerInfo['d2'][i])
                        if numSpaces == 0:
                            gameOver = True
                            print(f"Congrats, {playerInfo['d1'][i]}, you won the game!")
                            sys.exit()
                    else:
                        while guess in lettersGuessed:
                            guess = input(f"Letter already used. {playerInfo['d1'][i]}, guess again: ").lower()
                        if guess not in lettersGuessed and guess.isalpha():
                            clearScreen()
                        if len(guess) != 1:
                            if(guess == word):
                                gameOver = True
                                lettersGuessed += guess
                                board(playerInfo['d1'][i], playerInfo['d2'][i])
                                print(f"Congrats, {playerInfo['d1'][i]}, you won the game!")
                                sys.exit()
                            else:
                                playerInfo['d2'][i] -= 1
                                totalLives -= 1
                                board(playerInfo['d1'][i], playerInfo['d2'][i])
                        else:
                            if guess not in lettersGuessed:
                                if guess not in word:
                                    playerInfo['d2'][i] -= 1
                                    totalLives -= 1
                            lettersGuessed += guess
                            numSpaces = board(playerInfo['d1'][i], playerInfo['d2'][i])
                            if numSpaces == 0:
                                gameOver = True
                                print(f"Congrats, {playerInfo['d1'][i]}, you won the game!")
                                sys.exit()
                        