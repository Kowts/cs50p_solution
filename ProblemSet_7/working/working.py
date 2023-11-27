import re

# Main function that prompts the user for a time range in 12-hour format and prints the converted time range in 24-hour format.
def main():
    print(convert(input("Hours: ")))

# Converts a time range in 12-hour format to 24-hour format.
def convert(s):
    """
    Args:
    - time_range (str): Time range in 12-hour format (e.g. "1:30 AM to 2:45 PM").

    Returns:
    - str: Converted time range in 24-hour format.
    """
    if match := re.search(r"^(1?\d)(:[0-5]\d)? (AM|PM) to (1?\d)(:[0-5]\d)? (AM|PM)$", s):
        start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

        if start_period == "AM" and end_period == "PM":
            if 0 < int(start_hour) < 13 and 0 < int(end_hour) < 13:
                start_min = start_min if start_min else ":00"
                end_min = end_min if end_min else ":00"
                if (start_hour and end_hour) == "12":
                    return f"00{start_min} to {end_hour}{end_min}"
                return f"{start_hour.zfill(2)}{start_min} to {int(end_hour)+12}{end_min}"

        elif start_period == "PM" and end_period == "AM":
            if 0 < int(start_hour) < 13 and 0 < int(end_hour) < 13:
                start_min = start_min if start_min else ":00"
                end_min = end_min if end_min else ":00"
                return f"{int(start_hour)+12}{start_min} to {end_hour.zfill(2)}{end_min}"

        raise ValueError("Invalid time format provided.")
    else:
        raise ValueError("Invalid time format provided.")

if __name__ == "__main__":
    main()
