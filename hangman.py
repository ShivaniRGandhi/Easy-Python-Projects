import random
import string
from words import random_words

def get_valid_word(random_words): #pick a word without dashes or spaces
    word = random.choice(random_words)  #choose a random word from the words list
    while '-' in word or " " in word:
        word = random.choice(random_words)
    return word.lower()


def hangman():
    word = get_valid_word(random_words)
    word_letters = set(word)        # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()            #what the user has guessed

    #getting user input
    while len(word_letters) > 0:
        #letters used
        print('You have used these letters: ', ' '.join(used_letters))  

        #what is the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ' , " ".join(word_list))


        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used this character. Please try again.")
        else:
            print('Invalid Guess, please try again.')
    
    print("Good job you gussed it! ", word)

hangman()




