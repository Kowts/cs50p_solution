# Prompt the user to input their answer to the Great Question of Life, the Universe, and Everything.
user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

# Define a list of possible correct answers.
answers = ["42", "forty two", "forty-two"]

# Check if the user's input matches any of the correct answers.
if user_input in answers:
    print("Yes")  # If the input is correct, print "Yes".
else:
    print("No")   # If the input is not correct, print "No".
