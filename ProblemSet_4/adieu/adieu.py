# Import necessary modules
import sys
import inflect

# Create an inflect engine to handle pluralization
p = inflect.engine()

# Initialize an empty list to store names
names = []

# Infinite loop until manually terminated
while True:
    try:
        # Get the inputted name and capitalize it
        _names = input("Name: ").title()

        # If no name is provided, exit the program
        if len(_names) < 1:
            sys.exit(0)

        # Append the new name to the global names list
        names.append(_names)

    # Handle the case when Control+D (EOF) is pressed
    except EOFError:
        # Print a farewell message with the joined names
        print(f"\nAdieu, adieu, to {p.join(names)}")
        break
