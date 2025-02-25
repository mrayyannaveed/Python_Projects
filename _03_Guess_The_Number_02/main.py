# Guess The Number __ Number Guess By Computer

import random


index = 1

while index <= 5:
    random_number = int(input("Enter random number between 1 to 10 which is guessed by computer: "))
    guess_number = random.randint(1, 10)
    if guess_number == random_number:
        print("Computer guessed the number correctly")
        break
    else:
        print("Tryagain")
    
    print("Computer Guess Number",guess_number,", You have", 5-index, "chances left")
    index += 1