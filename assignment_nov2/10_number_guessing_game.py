import random

secret_number = random.randint(1, 50)
attempts = 0

print("I have chosen a number between 1 and 50.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < 1 or guess > 50:
        print("Please guess a number between 1 and 50.")
    elif guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct! You guessed the number in", attempts, "attempts.")
        break
