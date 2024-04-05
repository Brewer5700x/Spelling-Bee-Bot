from tqdm import tqdm
import os
from time import sleep

#Get words
f = open('words_alpha.txt', 'r')
data = f.read()
allWords = data.splitlines()
f.close()

#Prep bad letters
allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
goodLetters = []
while True:
    letter = input("Good Letter:")
    if letter == "done":
        break
    else:
        goodLetters.append(letter)
for letter in goodLetters:
    if letter in allLetters:
        allLetters.remove(letter)
badLetters = allLetters

#Remove words with bad letters
goodWords = []
for word in tqdm(allWords, desc="Loading"):
    badWord = False
    for letter in badLetters:
        if letter in word:
            badWord = True
    if not badWord:
        goodWords.append(word)
        goodWords.append("\n")

#Remove words without required letter and short words
reqdLetter = "a"
dummy = goodWords
goodWords = []
for word in tqdm(dummy, desc="Loading"):
    if reqdLetter in word and len(word) > 3:
        goodWords.append(word)
        goodWords.append("\n")

#Copy from goodWords list to solved_words.txt
os.remove("solved_words.txt")
f = open("solved_words.txt", "a")
for word in tqdm(goodWords, desc="Loading"):
    f.write(word)
f.close()