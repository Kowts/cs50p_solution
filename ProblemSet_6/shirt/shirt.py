import sys
from os.path import splitext, isfile
from PIL import Image, ImageOps

def main():
    # Validate command-line arguments and proceed if valid
    if is_valid_command_line_argument(sys.argv):
        overlay_images(sys.argv[1], sys.argv[2])

def is_valid_command_line_argument(argv):
    """Validates the command-line arguments provided by the user."""

    # Check for the number of command-line arguments
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    # Supported file extensions
    supported_files = [".jpeg", ".jpg", ".png"]

    input_extension = splitext(argv[1])[1].lower()
    output_extension = splitext(argv[2])[1].lower()

    # Check if the extensions of the provided files are supported
    if input_extension not in supported_files:
        sys.exit("Invalid input file extension.")
    if output_extension not in supported_files:
        sys.exit("Invalid output file extension.")

    # Check if the input and output files have the same extension
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions.")

    # Check if the input file exists
    if not isfile(argv[1]):
        sys.exit("Input file does not exist.")

    return True

def overlay_images(input_image, output_image):
    """Overlays a shirt image onto a base image and saves the result."""
    try:
        # Open the shirt image and the input image
        with Image.open("shirt.png") as shirt:
            with Image.open(input_image) as base_image:
                # Resize and crop the base image to match the shirt size
                base_image = ImageOps.fit(base_image, shirt.size)

                # Overlay the shirt image on the base image
                base_image.paste(shirt, (0, 0), shirt)  # Use shirt as mask for transparency

                # Save the result to the specified output file
                base_image.save(output_image)

    # Handle file not found error
    except FileNotFoundError:
        sys.exit(f"{input_image} does not exist.")
    # Handle other potential errors (like corrupted images)
    except OSError:
        sys.exit(f"Cannot process {input_image}.")

if __name__ == "__main__":
    main()
