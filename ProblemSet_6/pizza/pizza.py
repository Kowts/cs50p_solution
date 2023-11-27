import sys
import csv
from tabulate import tabulate

# Generate and print a table using the tabulate package from a given CSV file.
def generate_table_from_csv(file_path):
    """
    :param file_path: Path to the CSV file.
    """
    try:
        # Read CSV data
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

            # Print the table using tabulate
            print(tabulate(data, headers='firstrow', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    # Check if the file has a .csv extension
    if file_path.endswith('.csv'):
        generate_table_from_csv(file_path)
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
