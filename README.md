# Word Guessing Game
This is a simple word guessing game written in Python. The game fetches a random word from an API and gives you hints about the word. Your task is to guess the word one letter at a time.

## Requirements
- Python 3.6 or higher
- requests library

## Installation
1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

## How to Run
1. Navigate to the directory where you cloned the repository.
2. Run the main.py file using Python:

```
pip install -r requirements.txt
```

## How to Play
1. The game will fetch a random word from an API and give you a hint about the length of the word.
2. You will be prompted to guess a letter of the word.
3. If your guess is correct, the letter will be revealed in the word.
4. If your guess is incorrect, you will be prompted to try again.
5. The game continues until you have guessed all the letters in the word.
6. At the end of the game, you will be asked if you want to play again.

## Note
* This game relies on two external APIs to fetch random words and their definitions. If these APIs are down or unavailable, the game will not function correctly.