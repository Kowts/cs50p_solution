# Import necessary modules
import sys
import random
from pyfiglet import Figlet

# Initialize a Figlet object for text rendering
figlet = Figlet()

# Define the main function to handle command-line arguments and rendering
def main(argv):
    # Check if the font is set successfully, otherwise exit with an error message
    if set_figlet_font(argv):
        render_message()
    else:
        sys.exit("Invalid usage")

# Function to set the Figlet font based on command-line arguments
def set_figlet_font(argv):
    # Get the list of available fonts
    font_list = figlet.getFonts()
    is_font_set = False

    # If no command-line arguments provided, select a random font
    if len(argv) == 1:
        random_font = random.choice(font_list)
        figlet.setFont(font=random_font)
        is_font_set = True

    # If command-line arguments provided, check if they specify a valid font
    elif len(argv) == 3:
        if argv[1] == "-f" or argv[1] == "--font":
            if argv[2] in font_list:
                figlet.setFont(font=argv[2])
                is_font_set = True

    return is_font_set

# Function to render and display the input message with the selected font
def render_message():
    message = input("Input: ")
    print("Output:")
    print(figlet.renderText(message))

# Check if the script is run as the main program
if __name__ == "__main__":
    main(sys.argv)
