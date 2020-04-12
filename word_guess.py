# Word Guessing Game (hangman-style)
# Tom Keith - April 2020

import random
import csv

def randomWord():
    '''
    Returns a random word from the word.csv which contatins
    ~1000 words of length 5 or greater.
    '''
    with open('words.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    word_list = data[0]
    word_list_len = len(word_list)
    return word_list[random.randint(0,word_list_len)]

class WordGuesser:
    '''
    Game is played by instantiating this class.
    Default setting is 6 wrong guesses before game over.
    '''
    def __init__(self):
        self.word = randomWord().strip()
        self.word_length = len(self.word)
        self.target = list('-'*self.word_length)
        self.max_guesses = 6
        self.wrong_guesses = 0
        self.guesses = 0
        self.used_letters = ''
        self.display_board()
        self.take_guess()
    
    def display_board(self):
        print('')
        print(f'You have {self.max_guesses - self.wrong_guesses} guess{"es" if (self.max_guesses - self.wrong_guesses) != 1 else ""} left.')
        print(f'Used letters: {self.used_letters}')
        print(f'Word: {"".join(self.target)}')
        return
    
    def take_guess(self):
        '''
        Takes guess from user. Verifies given input is a single non-numeric character.
        '''
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        guess = input('Guess a letter: ')
        if (len(guess) == 1) and (guess.lower() in alpha) and (guess.lower() not in self.used_letters):
            return self.check_guess(guess.lower())
        else:
            print('Invalid guess. ', end="")
            return self.take_guess()
    
    def check_guess(self, guess):
        '''
        Checks input from the user to updates clue, guess number, and displays the game board
        before asking user for another input
        '''
        # Count how many times the letter shows up
        correct_num = 0
        if guess in self.word:
            for i,x in enumerate(self.word):
                if guess == x:
                    self.target[i] = self.word[i]  # Reveal the 
                    correct_num+=1
        if correct_num > 0:
            print(f'Yes, "{guess}" is correct! There {"are" if (correct_num>1) else "is"} {correct_num} of them.')
        else:
            print(f'Sorry, no "{guess}" in word.')
            self.wrong_guesses+=1
        self.used_letters += guess
        self.guesses+=1
        
        # Check if game is done by: 1. word has been fully guessed, or 2. if player is out of guesses
        if ('-' not in self.target):
            print('')
            print(f'Congratulations! The word is "{self.word}". You guessed correctly using {self.guesses} letters.')
            return
        if (self.max_guesses - self.wrong_guesses == 0):
            print('')
            print(f'GAME OVER! The word was "{self.word}". You guessed {self.guesses} letters.')
            return
        self.display_board()
        return self.take_guess()
        
game = WordGuesser()