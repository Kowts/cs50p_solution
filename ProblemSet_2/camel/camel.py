# Get user input in camelCase format.
camelCase = input("camelCase: ")

# Initialize an empty list to store the snake_case parts.
snake_case_parts = []

# Loop through every letter in camelCase.
for letter in camelCase:
    # Check if the letter is uppercase.
    if letter.isupper():
        # Add an underscore followed by the lowercase letter to the list.
        snake_case_parts.append("_" + letter.lower())
    else:
        # If the letter is not uppercase, add it as is to the list.
        snake_case_parts.append(letter)

# Join the list of parts into a single string with underscores.
snake_case = ''.join(snake_case_parts)

# Print the result in snake_case.
print("snake_case:", snake_case)
