# Hangman game steps:
# 1. Randomly select a word
# 2. create the same word with all underscores instead of letters
# 3. Display - word with underscores and pos - 0 of HANGMANPICS
# 4. ask for user to guess a Letter
# 5. check if the letter is in the word.
# 6. no - update display with HANGMANPICS postion incremented by 1
# 7. yes - update display with letter showing at correct position instead of underscore
# 8. Game over if
# 9. a. - HANGMANPICS reaches last pic OR b. all the underscores are gone.

import string
import random


class GameOver(Exception):
    pass


print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                   
""")

print("Welcome to the game of hangman..")
print("=================================")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
position = 0
word = list((random.choice(words)))


def create_hidden_word(word):
    new_word = []
    for w in word:
        new_word.append("_")
    return new_word


h_word = create_hidden_word(word)


choice_list = []


def display(h_word, HANGMANPICS):
    for w in h_word:
        print(w, end=" ")
    print()

    print(HANGMANPICS[position])


def is_letter_present(l, word, h_word):
    global position
    if l in word:
        x = 0
        for w in word:
            if l == w:
                h_word[x] = w
            x += 1
    else:
        position += 1

    if "_" not in h_word:
        print("======================")
        print("You Won. Game Over....")
        raise GameOver
    elif position == 6:
        print("======================")
        print("You Lost. Game Over")
        raise GameOver


try:
    while True:
        display(h_word, HANGMANPICS)

        l = input("please enter a letter: ")
        choice_list.append(l)

        is_letter_present(l, word, h_word)
except GameOver:
    pass

display(h_word, HANGMANPICS)
print(f"result --- {word}")
