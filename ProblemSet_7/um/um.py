import re

# Prompt the user for a text and print the count of the filler word 'um'.
def main():
    input_text = input("Text: ")
    um_count = count(input_text)
    print(um_count)

# Count the occurrence of the filler word 'um' in the given text.
def count(text: str) -> int:
    """
    Args:
    - text (str): The text in which to count the occurrences.

    Returns:
    - int: Number of occurrences of the word 'um'.
    """
    return len(re.findall(r"\bum\b", text, re.IGNORECASE))

if __name__ == "__main__":
    main()
y
