import random
word_list = ['apple', 'pear', 'cherry', 'watermelon', 'strawberry']
print(word_list)
choice = random.choice
word = choice(word_list)
print(word)
guess = input("Please enter a single letter.")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")