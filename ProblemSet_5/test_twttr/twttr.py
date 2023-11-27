# Main function
def main():
    user_input = input("Enter a string: ")
    print(shorten(user_input))

# Shorten the provided word function
def shorten(user_input):
    # Iterate over the characters in the inputted string
    for index in range(len(user_input)):
        # Check if the character is a vowel (case insensitive)
        if user_input[index].lower() in ["a", "e", "i", "o", "u"]:
            # Replace the vowel with 'u'
            user_input = user_input[:index] + "u" + user_input[index + 1:]

    # Remove all occurrences of 'u' from the string
    return user_input.replace("u", "")

# Run the main function
if __name__ == "__main__":
    main()
