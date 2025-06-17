import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")

    # User sets the range
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))

        if lower >= upper:
            print("Invalid range. Lower bound must be less than upper bound.")
            return

        # Generate the random number
        number_to_guess = random.randint(lower, upper)
        attempts = 0

        print(f"I'm thinking of a number between {lower} and {upper}. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < lower or guess > upper:
                    print(f"Your guess is out of range! Please guess between {lower} and {upper}.")
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Correct! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")

    except ValueError:
        print("Invalid input. Please enter integers for the range.")

# Run the game*
number_guesser()
