import random
import requests

url_base = 'https://random-word-api.herokuapp.com/word'
dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'

def get_word_definition(word):
    response = requests.get(dictionary_url.format(word))
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            meanings = data[0].get("meanings", [])
            if meanings:
                for meaning in meanings:
                    definitions = meaning.get("definitions", [])
                    if definitions:
                        for definition in definitions:
                            print(f"Definition: {definition.get('definition')}")
        else:
            print(f'No definitions found for the word: {word}')
    else:
        print(f'Failed to fetch API response for word: {word}. Status code: {response.status_code}')

menu = [] 
count_points=count_guess = 0 
option='S'

while True:
    response = requests.get(url_base)
    if response.status_code == 200:
        word_data = response.json()
        if len(word_data) > 0:
            word = random.choice(word_data)
            print(f'The random word is: {word}')
            print(f'Here is the tips...')
            if len(word) <= 5:
                print('Hint: The word is short.')
            elif len(word) >= 6 and len(word) <= 10:
                print('Hint: The word is medium.')
            get_word_definition(word)

            menu = ['_'] * len(word)
            print(menu)

        else:
            print('No words found in the random word API response.')
    else:
        print('Failed to fetch random word API response. Status code:', response.status_code)
        break

    count_points = count_guess = 0

    while True: 
        guess = str(input('Type one letter: ')).lower()
        if len(guess) != 1: 
            print('You typed more than one letter!')
        else: 
            count_guess += 1 
            correct_guess = False
            for i in range(len(word)): 
                if word[i] == guess:
                    count_points += 1
                    menu[i] = guess
                    correct_guess = True

            print(menu)
            print('')
            if count_points == len(word):
                break

            if not correct_guess:
                print('Incorrect guess. Try again.')

    print(f'Congratulations \U0001F680! You got the word right in {count_guess} guesses! The word was: {word.upper()}')

    option = input('Do you want to play again [Y/N]?: ').upper()
    if option != 'Y':
        break