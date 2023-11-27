import sys

# Count the number of lines of code in the given file. Excludes blank lines and comment lines.
def count_lines_of_code(filename):
    """
    :param filename: Path to the Python file.
    :return: Number of lines of code.
    """
    total_lines = 0

    with open(filename, "r") as file:
        for line in file:
            stripped_line = line.strip()

            # Skip blank lines
            if not stripped_line:
                continue

            # Skip lines that start with a comment
            if stripped_line.startswith("#"):
                continue

            total_lines += 1

    return total_lines

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # Check if the provided filename has a .py extension
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        lines_of_code = count_lines_of_code(sys.argv[1])
        print(lines_of_code)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
