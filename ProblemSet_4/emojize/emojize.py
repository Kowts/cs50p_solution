import emoji

def emojize_input(user_input: str) -> str:
    """
    Emojizes the user input using emoji aliases.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: The emojized result.
    """
    emojized_input = emoji.emojize(user_input, language='alias')
    return emojized_input

# Get the user input
user_input = input("Input: ")

# Emojize the input
emojized_result = emojize_input(user_input)

# Print the emojized result
print(emojized_result)
