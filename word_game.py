from helper_functions import *
import time
from computer_player import *



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
    
    while gameHandle != 'e':
        if gameHandle == 'r':
            print("You have not played a hand yet. Please play a new hand first!")
            gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            
        while gameHandle == 'n':
            gamerHandle = input("Enter u to have yourself play, c to have the computer play: ")
            
            if gamerHandle == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                
            elif gamerHandle == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
                gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                
            if gamerHandle not in ['c','u']:
                print ("Invalid command.")
                print()
                gamerHandle = input("Enter u to have yourself play, c to have the computer play: ")
            
            while gameHandle == 'r':
                gamerHandle = input("Enter u to have yourself play, c to have the computer play: ")
            
                if gamerHandle == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                    
                elif gamerHandle == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                if gamerHandle not in ['c','u']:
                    print ("Invalid command.")
                    print()
                    gamerHandle = input("Enter u to have yourself play, c to have the computer play: ")
            
                
        if gameHandle not in ['n','r','e']:
            print ("Invalid command.")
            gameHandle = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")



        

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

