import os
import sys
import csv


def main():
    """Pass the data in the sys.argv to tabulate."""

    # Check for insufficient arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    # Check for too many arguments
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    # Check if the input file exists
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    # Check if the input file is a CSV
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    else:
        # Process the CSV files
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(input_file, output_file):
    """Take the input file and write changes to an output file."""

    with open(input_file, "r") as csv_read_file:
        column_data = csv.DictReader(csv_read_file, delimiter=",")

        # Nested context
        with open(output_file, "w") as csv_write_file:
            fieldnames = ["first", "last", "house"]
            column_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)

            # Write the CSV header to the output file
            column_writer.writeheader()

            # Write the CSV source data to the output file
            for row in column_data:
                last, first = row["name"].split(",")
                house = row["house"]

                column_writer.writerow(
                    {"first": first.strip(), "last": last.strip(), "house": house.strip()}
                )


if __name__ == "__main__":
    main()
