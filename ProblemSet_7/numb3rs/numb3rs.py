# Main function that prompts the user for an IPv4 address and prints whether it's valid or not.
def main():
    inp: str = input("IPv4 Address: ").strip()
    print(validate(inp))

# Validates if the given string is a valid IPv4 address.
def validate(ip: str) -> bool:
    """
    Args:
    - ip (str): The string to validate.

    Returns:
    - bool: True if valid IPv4, False otherwise.
    """
    try:
        # Split the IP address by periods
        splitIP: list[str] = ip.split(".")

        # Ensure there are exactly 4 parts in the IP address
        if len(splitIP) != 4:
            return False

        # Check each part to ensure it's within the valid range (0-255)
        for part in splitIP:
            if not 0 <= int(part) <= 255:
                return False
    except ValueError:  # If a part isn't an integer
        return False

    # All checks passed, IP is valid
    return True

if __name__ == "__main__":
    # Execute the main function
    main()
