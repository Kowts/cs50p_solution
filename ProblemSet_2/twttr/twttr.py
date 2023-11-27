# Get user input as a string
user_input: str = input("Enter a string: ")

# Iterate over the characters in the inputted string
for index in range(len(user_input)):
    # Check if the character is a vowel (case insensitive)
    if user_input[index].lower() in ["a", "e", "i", "o", "u"]:
        # Replace the vowel with 'u'
        user_input = user_input[:index] + "u" + user_input[index + 1:]

# Remove all occurrences of 'u' from the string
user_input = user_input.replace("u", "")

# Print the modified string
print(user_input)
