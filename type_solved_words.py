import pyautogui as gui
from time import sleep
from tqdm import tqdm

f = open("solved_words.txt", "r")
data = f.read()
words = data.splitlines()
f.close

sleep(5)

for word in tqdm(words):
    gui.write(word, 0.05)
    gui.press('enter')
    sleep(0.5)

# gui.write(words[0], 0.05)
# gui.press("enter")