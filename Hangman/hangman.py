import random
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from our list
    
    # this will not choose one of the words with either a - or a space
    # the while loop is used to say, while the word has either a - or a space, it will continuously randomize it
    # until there is none

    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # initialized for the number of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a, 'b', 'cd']) --> 'a b cd' 
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie. for word: W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        # this group is used to check whether or not the letter is in the used letters already
        # if it isn't, it will add it to the list of used letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            # this first if/else statement is used for a correct guess of letter
            # it checks if the input letter is inside the word
            if user_letter in word_letters:
                # then it takes the word letters and removes the users input as that letter is now taken off the list
                word_letters.remove(user_letter)
                print('')

            # this else is for a wrong guess of letter
            else:
                lives = lives - 1 # take away a life for a wrong guess
                print('\nYour letter, ', user_letter, ' is not in the word.')
            
        elif (user_letter in used_letters):
            print('\nYou have already used that letter. Guess again.')
        
        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives are at 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Yay! You guess the word', word, '!')

hangman()