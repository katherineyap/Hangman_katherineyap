# Hangman_katherineyap
AiCore Hangman assignment 1

**Introduction**

A popular word guessing game that brings together most of the Python's fundamental concepts. 


**Step 1**

Import the Random module 
  - A built-in function that allows the random choice of word from the list 
 
**Step 2**

Initialise Class and attributes that will be used later 

  -the use of len() function for the number of characters 
	
  -assigning underscores according to the number of characters 
	
  -assigning an empty list for 'list letter' variable to store letter that has been guessed 
	
  -use of f'string
 
 **Step 3**
 Ask for letter
 
  -while True for looping 
	
  -the use of input() method to ask user for input, at the same time, the use of lower() method 
	
   to make sure all inputs are in lower format 
	 
  -the use of 'if' and 'else' statements to stipulate two possible outcomes
	
  -call for check_letter method if the input complies with the 'if' conditions 
	
  
  **Step 4**
	
Check if the input letter is within the randomly generated word 
	
-the use of 'in' and 'not in' operators 
		
-the use of enumerate to get the index of the correct letter in the word, and assigning the correct letter to the word_guessed list with the index enumerated 
		 
-for every correct guess of letter, the num_letter is deducted by 1. When the num_letter reaches 0, it means the user has guessed correctly
		 
 -for every wrong guess of letter, the num_lives is deducted by 1, and the display is added by 1. When the num_lives reaches 0, it means the user losses the game. 
		 
 -for each wrong guess, the hangman_display list is printed, indexed according to the display number
   
   
  
  
  
  
