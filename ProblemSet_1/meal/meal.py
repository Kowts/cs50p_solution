# Define the main function.
def main():
    # Prompt the user to input the current time in the format "HH:MM".
    time = input("What time is it? ")

    # Call the 'convert' function to convert the input time to decimal hours.
    hours = convert(time)

    # Check the converted hours to determine the mealtime.
    if hours >= 7 and hours <= 8:
        print("Breakfast time")
    elif hours >= 12 and hours <= 13:
        print("Lunch time")
    elif hours >= 18 and hours <= 19:
        print("Dinner time")

# Define a function to convert time in "HH:MM" format to decimal hours.
def convert(time):
    time = time.split(":")
    minutes = float(time[1]) / 60
    return float(time[0]) + minutes

# Check if the script is being run as the main program.
if __name__ == "__main__":
    main()
