# Define the main function to calculate and display the fuel gauge status.
def main():
    # Prompt the user for input.
    fraction_input: str = input("Enter the fuel fraction (e.g., '3/4'): ")

    try:
        # Split the inputted fraction by "/" and convert to integers.
        numerator, denominator = map(int, fraction_input.split("/"))

        # Check if the numerator is greater than the denominator or the denominator is zero.
        if numerator > denominator or denominator == 0:
            raise ValueError("Invalid numerator or denominator values")

        # Calculate the fuel percentage.
        fuel_percent: int = int(round((numerator / denominator) * 100))

        # Determine the fuel gauge status.
        if fuel_percent <= 1:
            # Fuel gauge is empty.
            print("E")
        elif fuel_percent >= 99:
            # Fuel gauge is full.
            print("F")
        else:
            # Fuel gauge is partially filled.
            print(f"{fuel_percent}%")

    except ValueError:
        # Handle invalid input by restarting the main function.
        main()

# Run the main function to start the program.
if __name__ == "__main__":
    main()