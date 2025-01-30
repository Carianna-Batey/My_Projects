"""
Carianna Batey
Program Description:
This program is a guessing game, where the user inputs a random number in attempt to match the random 
number generated in the program.
"""
import random
print("I have generated a random number netween 1 and 100. You will have 10 attempts to guess that number.")
number= random.randint(1,100)
i=1
while i<=10:
    guess=int(input(f"Guess {i}: "))
    i+=1
    if guess > number:
        print("Your guess is greater than my random number. Try Again.")
    elif guess < number:
        print("Your guess is less than my random number. Try Again.")
    else:
        print("You correctly guessed my random number!")
        break
else:
    print("You've run out of chances. Game Failed.")