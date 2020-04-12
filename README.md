# Word Guessing Game

### Hangman-style word guessing game (python OOP)
#### Tom Keith - April 2020

Simply run word_guess.py to play the game. You have 6 'lives' to guess one of over 1000 words in word library.

This was a simple/fun coding exercise where I wanted to utilize OOP.

### Sample Win

```
You have 6 guesses left.
Used letters: 
Word: ------
Guess a letter: d
Sorry, no "d" in word.

You have 5 guesses left.
Used letters: d
Word: ------
Guess a letter: d
Invalid guess. 
Guess a letter: r
Yes, "r" is correct! There is 1 of them.

You have 5 guesses left.
Used letters: dr
Word: -----r
Guess a letter: e
Yes, "e" is correct! There are 2 of them.

You have 5 guesses left.
Used letters: dre
Word: -e--er
Guess a letter: l
Sorry, no "l" in word.

You have 4 guesses left.
Used letters: drel
Word: -e--er
Guess a letter: o
Sorry, no "o" in word.

You have 3 guesses left.
Used letters: drelo
Word: -e--er
Guess a letter: s
Sorry, no "s" in word.

You have 2 guesses left.
Used letters: drelos
Word: -e--er
Guess a letter: t
Sorry, no "t" in word.

You have 1 guess left.
Used letters: drelost
Word: -e--er
Guess a letter: m
Yes, "m" is correct! There are 2 of them.

You have 1 guess left.
Used letters: drelostm
Word: mem-er
Guess a letter: b
Yes, "b" is correct! There is 1 of them.

Congratulations! The word is "member". You guessed correctly using 9 letters.
```

### Sample Loss

```
You have 6 guesses left.
Used letters: 
Word: ------
Guess a letter: s
Sorry, no "s" in word.

You have 5 guesses left.
Used letters: s
Word: ------
Guess a letter: t
Sorry, no "t" in word.

You have 4 guesses left.
Used letters: st
Word: ------
Guess a letter: r
Sorry, no "r" in word.

You have 3 guesses left.
Used letters: str
Word: ------
Guess a letter: l
Sorry, no "l" in word.

You have 2 guesses left.
Used letters: strl
Word: ------
Guess a letter: n
Sorry, no "n" in word.

You have 1 guess left.
Used letters: strln
Word: ------
Guess a letter: e
Yes, "e" is correct! There is 1 of them.

You have 1 guess left.
Used letters: strlne
Word: -----e
Guess a letter: o
Sorry, no "o" in word.

GAME OVER! The word was "divide". You guessed 7 letters.
```
