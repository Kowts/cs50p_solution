# Define the main function, which calculates the tip amount.
def main():
    # Prompt the user to input the meal cost and convert it to a float.
    dollars = dollars_to_float(input("How much was the meal? "))

    # Prompt the user to input the tip percentage and convert it to a float.
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate the tip amount by multiplying the meal cost and tip percentage.
    tip = dollars * percent

    # Print the calculated tip amount formatted with two decimal places.
    print(f"Leave ${tip:.2f}")

# Define a function to convert a string with a dollar sign to a float.
def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)

# Define a function to convert a string with a percentage to a float.
def percent_to_float(p):
    p_without_percent = p.replace("%", "")
    p_converted = float(p_without_percent) / 100
    return p_converted

# Call the main function to run the program.
main()
