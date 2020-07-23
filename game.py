#Easy game made by kezim

import random
print("Welcome to the game, it is here for you to guess the drawn number as soon as possible | PRESS ENTER TO NEXT |")
next = input()

print("Okay! let's go")
random = random.randint(1,100)
print("I generated a number in the range 0 100")

tries = 0

x = input()
x = int()

while random != x:
    if x < random:
        tries += 1
        print("Your number is too small")
        print(" ")
        print("Pls next number")
        x = input()
        x = int(x)
        print(" ")
    else:
        tries += 1
        print("Your number is too big")
        print(" ")
        print("Pls next number")
        x = input()
        x = int(x)
        print(" ")
if random == x:
    print("You win!")
    print(" ")
    print("Tries:")
    print(tries)