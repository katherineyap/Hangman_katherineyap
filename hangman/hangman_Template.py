'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

hangman_display = [
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |                       
    |                           
    |                            
    |___                    
    HA _ _ _ _ _""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN _ _ _ _""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG _ _ _""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM _ _""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA _""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""

]


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5, display=0):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = []
        self.list_letter = []
        self.display = display

        for w in range(len(self.word)):
            self.word_guessed.append(' _ ')

        print (f"The mistery word has", {self.num_letters}, "characters")
        print (self.word_guessed)
                    
    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        if letter in self.word:
            self.num_letters -= 1
            for index,value in enumerate(self.word):
                if value == letter:
                    self.word_guessed[index] = letter
            print (f'Nice!', letter, 'is in the word!')
            print (self.word_guessed)
            if self.num_letters == 0:
                print ('Congratulations! You won! The word was',self.word)
            
        if letter not in self.word:
            self.num_lives -=1
            self.display +=1
            self.list_letter.append(letter)
            print (f'Sorry',letter,'is not in the word')
            print (f'You have', self.num_lives, 'lives left.',hangman_display[self.display] )
            if self.num_lives == 0:
                print (f'You lost! The word was', self.word)

        return self.ask_letter()
           
    def ask_letter(self, num_lives=5):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        while self.num_lives > 0:
            print ('please enter a letter')

            letter = input().lower()

            if len(letter) > 1:
                print ("Please, enter just one character")
            # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
            # TODO 3: If the letter is valid, call the check_letter method
            
            else:
                if letter in self.list_letter:
                    print (f"{letter},was already tried.")
                else:
                    self.check_letter(letter)
            


if __name__ == '__main__':

    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    test = Hangman(word_list, num_lives=5)
    test.ask_letter()


