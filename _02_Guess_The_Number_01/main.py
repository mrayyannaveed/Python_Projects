# Guess The Number __ User Guess The Number 
import random

index = 1
print("You have 10 turns to guess the number")
while index <=10:
    random_guess = random.randint(1, 15)
    guess = int(input("Guess a number between 1 and 15: "))
    if guess == random_guess:
        print("You guessed correctly!")
        break
    else:
        print("Try again!")
    print("Number is", random_guess ,"You have", 10-index, "turns left")
    index += 1