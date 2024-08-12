import random
choice = random.choice

# The name of the class has to be UpperCamelCase or PascalCase.
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = choice(self.word_list)
        self.word_guessed = []
        for letter in self.word:
            self.word_guessed.append('_')
        #print(self.word_guessed)
        self.num_lives = num_lives
        self.num_letters = int(len(set(self.word_guessed)))
        # self.word_list = ['apple', 'pear', 'cherry', 'watermelon', 'strawberry']
        self.list_of_guesses = []
        #while self.guess not in self.list_of_guesses:
        #   self.list_of_guesses.append()

    '''Create the class Hangman for the game objects.
    Pass in word_list and num_lives as parameters.
    The default number of lives is 5.
    Initialse the following attributes:
        word: The word to be guessed, picked randomly from the word_list.
        word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        num_lives: int - The number of lives the player has at the start of the game.
        word_list: list - A list of words, to be passed in as the argument.
        list_of_guesses: list - A list of the guesses that have already been tried.'''
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(letter)] = guess
            self.num_letters -=1
            print("Good guess!", guess, "is in the word.")
        else:
            self.num_lives -=1
            print("Sorry,", guess, "is not in the word. Try again.")
            print("You have", self.num_lives, "lives left.")  
    
    '''Define the method check_guess.
    Pass guess to the method as a parameter.
    The function will convert the guessed letter into lowercase.
    If the letter is in the randomly picked word, replace the corresponding _ with the letter in the word_guessed list, and reduce num_letters by 1.
    If not in, reduce num_lives by 1 and print a message to annouce the new num_lives to the user.'''

    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter.")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")        
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)     
    
    '''Define the method ask_for_input.
    Pass self in, which means the function will take the hangman object - an instance of the Hangman class.
    Create a while loop and set the condition to True.
    Ask the user to input a letter and assign it to the variable guess.
    If the guess does not meet the requirement: a single aphabetical letter, print a message to ask for a valid input.
    If the guess is valid, but has been tried before, print a message to notify the user.
    If the guess is valid and has not been tried before, run the check_guess function and append this guess to the list_of_guesses.'''

my_hangman = Hangman(['apple', 'pear', 'cherry', 'watermelon', 'strawberry'], 3)

Hangman.ask_for_input(my_hangman)