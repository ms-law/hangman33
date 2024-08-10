import random
word_list = ['apple', 'pear', 'cherry', 'watermelon', 'strawberry']
#print(word_list)
choice = random.choice
word = choice(word_list)
#print(word)

#while True:
#    guess = input("Please enter a letter.")
#    if len(guess) == 1 and guess.isalpha() == True:
#        break
#    else:
#        print("Invalid letter. Please enter a single alphabetical character.")

#if guess in word:
#    print("Good guess!", guess, "is in the word")
#else:
#    print("Sorry,", guess, "is not in the word. Try again.")

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess!", guess, "is in the word")
    else:
        print("Sorry,", guess, "is not in the word. Try again.")   

def ask_for_input():
    while True:
        guess = input("Please enter a letter.")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()            