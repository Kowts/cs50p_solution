# Prompt the user to input a text and store it in the 'text' variable.
text = input("Enter text: ")

# Replace all spaces in the input text with three dots '...' using the 'replace()' method.
# This replaces spaces with a specific character sequence.
new_text = text.replace(" ", "...")

# Print the modified text with spaces replaced by '...'.
print(new_text)
