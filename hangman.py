"""
@filename: hangman.py
@author: Ben Ries-Roncalli And Matt Baysa
@@date_created:10-24-2020
@python_version: python 3.7.0
   

"""

from graphics import HANGMANPICS
import random
import more_itertools as mit #adds some iteration fxns



def game_start(word):
  '''
  fxn to start game, print welcome and initial gallow and blanks for word
  '''
  print('*'*15, '\n') #line 17-20 prints intro
  print('H A N G M A N\n')
  print('welcome to the gallows\n')
  print('*'*15, '\n') 
    
  print(HANGMANPICS[0]) #prints gallows
    
  blanks = ['_' for i in range(len(word))] #line 24-26 prints blanks of word
  for i in range(len(blanks)):
    print(blanks[i], end = ' ')
  print()
  return blanks
    
    
def pullwords(filename):
  """
  fxn to pull wordbank from file
  """
  with open(filename, 'r') as file: #opens file
    wordstring = file.read() #copies wordbank from file to string wordstring
  return wordstring.split("\n") #splits string wordstring into list over new lines


def getword(bank):
  """
  fxn to pick random word from list bank
  """
  length = len(bank)
  num = random.randrange(0, length) #generates random number in length of wordbank list
  return bank[num] #returns word at random position in wordbank list


def callgraphics(num):
  """
  this fxn calls the correct picture to be printed based on number of wrong guesses
  """
  print(HANGMANPICS[num]) #prints hangman pic


def letter_guess(word, blanks):
  """
  this fxn runs the games
  """
  wrong_guesses = 0 #initialize variable to count wrong guesses
  wrong_letters = [] #initialize list for wrong letters
  
  while wrong_guesses < 7: #while loop for when there have not been too many wrong guesses
    letter = input('Guess a letter: ') #ask user to guess a letter
    callgraphics(wrong_guesses) #prints hangman pic based on number of wrong guesses
    print('Wrong guesses:', end = ' ') #lines 66-68 prints wrong letters guessed
    for i in range(len(wrong_letters)):
        print(wrong_letters[i], end = '   ')
    print()



    if letter in word: #triggered if user guesses correctly
      print('Correct! The letter ', letter, ' is in the word!')
      positions = list(mit.locate(word, lambda x: x == letter))
      for n in positions: #finds position of all ocurrences of letter guessed correctly
        blanks[n] = letter #replaces blanks at those positions with letter
      for i in range(len(blanks)): #prints blanks and letters guessed correctly
        print(blanks[i], end = ' ')
      print()

      
    else: #triggered if letter guessed incorrect
      print('Wrong! The letter ', letter, ' is not in the word!')
      wrong_guesses += 1 #increments wrong_guesses
      for i in range(len(blanks)): #line 86-87 prints blanks (and any other letters previously guessed correctly)
        print(blanks[i], end = ' ')
      wrong_letters.append(letter) #adds incorrect letter guessed to list wrong_guesses
      print()

      
    if '_' not in blanks: #triggered if no more blanks in list (all letters guessed)
      print()
      print('Congratulations! You guessed the word! You win!')
      print()
      break #breaks while loop since user won
  
  else: #triggered if user used all guesses and lost
    print()
    print('You lost!')
    print('The word was ', word)
    print()



# this is the main part and the above functions are called here.
if __name__ == '__main__':
  userinput = input("Do you want to play hangman? y/n: ") #ask user if wants to play
  while userinput == 'y': #while loop allowing user to replay game
    word = getword(pullwords('./wordbank/bank2.txt')) #gets random word using getword() and pullwords() fxns defined earlier
    blanks = game_start(word) #game_start fxn does game setup
    letter_guess(word, blanks) #letter_guess fxn is gameplay
    userinput = input("Do you want to play again? y/n: ") #asks user if wants to replay after game ends