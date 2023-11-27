# Import the random module for generating random numbers
import random

# Main function to run the guessing game
def main():
    level = get_level()
    guess_number(level)

# Function to get the level of the guessing game from the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            break
        except ValueError:
            continue
    return level

# Function to play the guessing game
def guess_number(level):
    number = random.randint(1, level)
    guess = 0
    while guess != number:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Just Right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            continue

# Run the game when the script is executed
if __name__ == "__main__":
    main()
