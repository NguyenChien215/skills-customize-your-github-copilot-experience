# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python where the player guesses letters to reveal a hidden word, practicing strings, loops, conditionals, and basic game logic.

## 📝 Tasks

### 🛠️	Hangman Core Game Loop

#### Description
Create the basic Hangman game that runs in the terminal. The game should randomly pick a word, ask the player to guess letters, and show progress until the player either wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of at least 5 words
- Show the current word progress using underscores for unknown letters (for example: `_ p p l e`)
- Accept a single-letter guess from the user each turn
- Track and display the number of remaining incorrect attempts
- End the game when the word is fully guessed or attempts reach 0, then display a clear win/lose message

Example interaction:

```python
Word: _ _ _ _ _
Guesses left: 6
Enter a letter: a
Good guess!

Word: a _ _ a _
Guesses left: 6
Enter a letter:
```

### 🛠️	Enhance the Player Experience

#### Description
Improve your Hangman game to be more user-friendly and fun. Add features that help the player understand what is happening and keep track of their guesses.

#### Requirements
Completed program should:

- Show all letters that have already been guessed (both correct and incorrect)
- Prevent the player from guessing the same letter twice (and show a helpful message if they do)
- Handle invalid input (such as more than one character, numbers, or symbols) with a clear error message and no penalty
- Allow the player to play multiple rounds without restarting the program and show how many games they have won and lost
