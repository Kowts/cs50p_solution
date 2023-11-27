# Get the user input for the greeting and store it in the variable 's'.
text: str = input("Greeting: ")

# Convert the input to lowercase and remove leading/trailing whitespace.
text = text.lower().strip()

# Check what the input starts with.
if text.startswith("hello"):
    print("$0")    # If it starts with "hello," print "$0."
elif text.startswith("h"):
    print("$20")   # If it starts with "h" (but not "hello"), print "$20."
else:
    print("$100")  # If it doesn't match either condition, print "$100."