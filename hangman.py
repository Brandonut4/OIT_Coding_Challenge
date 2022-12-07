#Brandon Jacobs
#This program is designed to choose a word from a predfined list. Then using that word, the user can play a hangman style game.

import random
#Predefined global variables
HANGMAN_IMAGES = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''
]
WORD_LIST = ['stephcurry', 'lebronjames', 'nikolajokic', 'russellwilson', 'russellnelson', 'patsurtain', 'aarongordon', 'calemakar', 'timtebow', 'troytulowitzki']

class Person():
    def __init__(self, name):
        self.__name__ = name
    
    def GetName(self):
        return self.__name__
    def SetName(self, newName):
        self.__name__ = newName

def InputName():
    name = input(f"Enter the player's first name: ")
    Person(name)
    return name
    

def ChooseWord():
    
    wordString = random.choice(WORD_LIST)
    wordAsList = list(wordString)
    
    for letter in range(0, len(wordAsList)):
       wordAsList[letter] = '_'
    return wordAsList, wordString
      

def PlayGame(blankList, answer, name):
    #initialize variables
    dictAlphabet={ 'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0, 'j':0,'k':0,'l':0,
    'm':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0 }
    count = 0
    gameList = blankList
    answerList = list(answer)
    incorrectGuesses = []
    correctGuesses = []
    numIncorrect = 0
    
    #iterate game
    while ('_' in gameList):
        userGuess = input(f"{name} enter guess #{count}: ")
        userGuess = userGuess.lower()
        if ValidateGuess(userGuess, dictAlphabet): #Validate if guess is single letter
            if dictAlphabet[userGuess] == 0:    #Check if guess has been made
                dictAlphabet[userGuess] = 1
                count = count + 1               #increment counter
            else:                               #Prompt "redo guess"
                print(f"You already guessed letter {userGuess}.")
                continue

        else:
            print(f"Guess not valid. Please choose one letter of the alphabet")
            continue
        
        #make list of incorrect guesses
        if userGuess not in answerList:
            incorrectGuesses.append(userGuess)
            guess = False
            numIncorrect = numIncorrect + 1
        else:
            correctGuesses.append(userGuess)
            guess = True

        #Make updated sting based on guess
        for letter in range(0, len(gameList)):
            if answerList[letter] == userGuess : #find and replace
                gameList[letter] = userGuess
                
            else:
                continue
        #print according to correctness of guess
        if guess:
            print(f'\nCorrect!\n{"".join(gameList)}')
            
        else:
            print(f'\n{userGuess} is not in the word.\nIncorrect guesses: {", ".join(incorrectGuesses)}')
            

        print(f'\nCorrect guesses: {len(correctGuesses)}\nIncorrect guesses: {len(incorrectGuesses)}')
       
        if numIncorrect < 6:
            print(HANGMAN_IMAGES[numIncorrect])
        else:
            print(HANGMAN_IMAGES[6])

    if '_' not in gameList: #Check if whole word has been guessed
        print(f'\nYou guessed the word! You used {count} guesses.\nThe word was {"".join(gameList)}')
    else:
        print(f"\nYou took too many guesses!")
   
    #Prompt play again
    playAgain = input(f"Would you like to play again? (Y/N): ")
    
    return playAgain

def ValidateGuess(letter, dict): #Validate guess if single letter
    if letter in dict.keys():
        return True
    else:
        False

def Execute():
    playerName = InputName()
    #start game
    playAgain = 'Y'
    while playAgain.upper() == 'Y': 
        blankWord, answerWord = ChooseWord() #randomize word
        playAgain = PlayGame(blankWord, answerWord, playerName) 
    print('Thanks for playing!')




