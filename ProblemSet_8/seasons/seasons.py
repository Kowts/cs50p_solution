from datetime import date
import inflect
import sys

p = inflect.engine()

# Main function to execute the program.
def main():
    birthday = input("Date of Birth (YYYY-MM-DD): ")
    minutes = calculate_minutes_since_birth(birthday)
    print(convert_minutes_to_text(minutes))

# Calculate the number of minutes since the given birthdate until today.
def calculate_minutes_since_birth(birth):
    """
    Args:
        birth (str): Birthdate in string format 'YYYY-MM-DD'.

    Returns:
        int: Number of minutes since birth.
    """
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date type")

    today = date.today()
    difference = today - birth_date
    total_minutes = round(difference.total_seconds() / 60)

    return total_minutes

# Convert the number of minutes to text representation.
def convert_minutes_to_text(num):
    """
    Args:
        num (int): Number of minutes.

    Returns:
        str: Minutes in words.
    """
    return f"{p.number_to_words(num, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()
