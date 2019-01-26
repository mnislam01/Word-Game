# The 6.00 Word Game

import random
import string
from helper_functions import *

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
    
    while gameHandle != 'e':
        if gameHandle == 'r':
            print("You have not played a hand yet. Please play a new hand first!")
            gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        while gameHandle == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            
            while gameHandle == 'r':
                playHand(hand, wordList, HAND_SIZE)
                gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                
        if gameHandle not in ['n','r','e']:
            print ("Invalid command.")
            gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        



#Play the game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
