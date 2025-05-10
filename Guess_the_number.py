import random
number = random.randint(1,100)
attempts = 0
while 1:
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit():
        print("Please Enter valid number between 1 and 100")
        continue
    guess = int(guess)
    attempts =attempts + 1
    if guess < number:
        print("Your number is Less than the Original Number.")
    elif guess > number:
        print("Your number is More than the Original Number..")
    else:
        print(f"Correct! You guessed it in {attempts} Attempts.")
        break