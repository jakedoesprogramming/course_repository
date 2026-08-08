import random

# Generate a random number
number = random.randint(1, 30)

# Track guesses
guess_attempts = 0
amount_attempts = 5

# Keep asking until the guess is correct
while True:

    

    # Ask the user for a guess
    question = int(input("Guess the number: "))

    # Count this guess
    guess_attempts += 1


    # Check the guess
    if question > number:
        print("Too high!")
        if guess_attempts >= amount_attempts:
             print(f"game over! your number was {number}")
             break

    elif question < number:
        print("Too low!")
        if guess_attempts >= amount_attempts:
            print(f"game over! your number was {number}")
            break

    else:
        print("Correct!")
        print(f"You got it in {guess_attempts} guesses!")
        break