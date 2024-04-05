from tqdm import tqdm
import pyautogui as gui
from time import sleep

# Get words
f = open('words_alpha.txt', 'r')
data = f.read()
allWords = data.splitlines()
f.close()

# Prep bad letters
allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
goodLetters = []
while True:
    letter = input("Good Letter:")
    if letter == "done":
        break
    else:
        goodLetters.append(letter)
reqdLetter = input("Required Letter:")
for letter in goodLetters:
    if letter in allLetters:
        allLetters.remove(letter)
badLetters = allLetters

# Remove words with bad letters
goodWords = []
for word in tqdm(allWords, desc="Loading"):
    badWord = False
    for letter in badLetters:
        if letter in word:
            badWord = True
    if not badWord:
        goodWords.append(word)

# Remove words without required letter and short words
dummy = goodWords
goodWords = []
for word in tqdm(dummy, desc="Loading"):
    if reqdLetter in word and len(word) > 3:
        goodWords.append(word)

sleep(5)

# Type solved words
for word in goodWords:
    gui.write(word, 0.05)
    gui.press('enter')
    sleep(0.5)