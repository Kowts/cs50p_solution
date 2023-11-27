from validator_collection import validators, checkers

def main():
    # Prompt the user to enter an email address
    email = input("Enter an email address: ").strip()

    # Check if the email address is syntactically valid and not empty
    if checkers.is_email(email) and validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
