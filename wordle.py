from os import system
from colorama import Fore, Style
from random import choice

WORD_LIST_DIR = "words_mit"

def censor(goal_word: str, guessed_word: str) -> str:
    out = ""
    for letter_index in range(len(guessed_word)):
        if goal_word[letter_index] == guessed_word[letter_index]:
            out += Fore.GREEN + guessed_word[letter_index] + Style.RESET_ALL
        elif guessed_word[letter_index] in goal_word:
            out += Fore.YELLOW + guessed_word[letter_index] + Style.RESET_ALL
        else:
            out += Fore.RED + guessed_word[letter_index] + Style.RESET_ALL
    return out

def valid_word(word: str, word_length: int,
        valid_chars: str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm",
    ) -> bool:
    for letter in word:
        if letter not in valid_chars:
            return False
        
    with open(f".\{WORD_LIST_DIR}\words len_{word_length}.txt", "r") as file:
        words = file.read().split("\n")
        if word in words:
            return True
    return False

guessed_words = []

word_select = input("[R]andom word \n[C]hoose word \n> ")

if word_select.lower() == "r":
    word_length = 0
    while word_length < 1 or word_length > 20:
        system("cls")
        word_length = int(input("Word length: "))

    with open(f".\{WORD_LIST_DIR}\words len_{word_length}.txt", "r") as file:
        words = file.read().split("\n")
        word_to_guess = choice(words)
else:
    good_word = False
    while not good_word:
        word_to_guess = input("> ")
        good_word = valid_word(word_to_guess)

    word_length = len(word_to_guess)

system("cls")

word_to_guess = word_to_guess.lower()
guesses = int(input("Guesses: "))

invalid_word_reason = ""
for x in range(guesses+1):
    system("cls")

    for index, word in enumerate(guessed_words): 
        print(f"{index+1} - {censor(word_to_guess, word)}")
    print()

    if x == guesses:
        break

    print(invalid_word_reason)
    word = input("> ") 
    
    if word == word_to_guess:
        guessed_words.append(word)
        break

    good_length = len(word) == len(word_to_guess)
    valid       = valid_word(word, word_length)
    
    if good_length and valid:
        guessed_words.append(word)
        invalid_word_reason = ""
    elif not good_length:
        invalid_word_reason = "Word isnt correct length"
    else:
        invalid_word_reason = "Word isnt valid"

system("cls")

for index, word in enumerate(guessed_words): 
    print(f"{index+1} - {censor(word_to_guess, word)}")

if x >= guesses:
    print(f"\nCorrect word is: \n{word_to_guess}")
else:
    print("Correct!")
