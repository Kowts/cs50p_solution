# Define the main function.
def main():
    # Prompt the user to enter a vanity plate.
    plate = input("Plate: ")

    # Check if the entered vanity plate is valid and print the result.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define a function to check the validity of a vanity plate.
def is_valid(plate):
    # Check if the plate length is between 2 and 6 characters (inclusive).
    if not (2 <= len(plate) <= 6):
        return False

    # Check if the first two characters are letters.
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # Store whether a digit has been found.
    found_digit = False
    first_digit = True

    # Iterate through each character in the plate.
    for char in plate:
        if char.isdigit():
            found_digit = True
            # Check if it's the first digit, and if it's '0'.
            if first_digit and char == "0":
                return False
            first_digit = False
        elif char.isalpha():
            # If a letter comes after a digit, return False.
            if found_digit:
                return False
        else:
            # If the character is neither a digit nor a letter, return False.
            return False

    return True

# Check if the script is being run as the main program.
if __name__ == "__main__":
    main()
