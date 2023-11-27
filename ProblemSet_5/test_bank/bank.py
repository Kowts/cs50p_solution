import string

def main():
    # Get the user input for the greeting and store it in the variable 's'.
    text: str = input("Greeting: ")
    print(value(text))

def value(greeting):
    # Convert the input to lowercase and remove leading/trailing whitespace.
    greeting = greeting.lower().strip()

    # Check what the input starts with.
    if greeting.startswith("hello"):
        penalty = 0    # If it starts with "hello," print 0."
    elif greeting.startswith("h"):
        penalty = 20   # If it starts with "h" (but not "hello"), print 20."
    else:
        penalty = 100  # If it doesn't match either condition, print 100."
    return penalty

if __name__ == "__main__":
    main()
