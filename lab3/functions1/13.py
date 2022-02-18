import random
name = input("Hello! What is your name?\n")
print("Well, KBTU, I am thinking of a number between 1 and 20.\nTake a guess.")
def guess_num(x,num,guess):
    if x==num: print("Good job, {name}! You guessed my number in {guess} guesses!")
    else:
        guess += 1
        if num > x: 
            print("Your guess is too high.\nTake a guess.")
            num = int(input())
            guess_num(x,num,guess)
        else:
            print("Your guess is too low.\nTake a guess.")
            num=int(input())
            guess_num(x,num,guess)
x = random.randrange(1,20)
num = int(input())
guess = 1
guess_num(x,num,guess)