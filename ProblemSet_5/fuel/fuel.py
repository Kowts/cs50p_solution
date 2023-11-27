# Main function to interact with the user
def main():
    while True:
        try:
            fraction = input("Fraction (X/Y format): ").strip()
            print(gauge(convert(fraction)))
            break
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Denominator cannot be zero.")

# Function to convert a string to a X/Y fraction and calculate its percentage
def convert(fraction: str) -> float:
    if "/" not in fraction:
        raise ValueError("Not a valid fraction format.")

    x, y = fraction.split("/", 1)

    if not x.isdigit() or not y.isdigit():
        raise ValueError("X or Y is not an integer.")

    x, y = int(x), int(y)

    if x > y:
        raise ValueError("Numerator cannot be larger than denominator.")

    if y == 0:
        raise ZeroDivisionError()

    return (x / y) * 100

# Function to gauge the fuel reserve based on a percentage
def gauge(percentage: float) -> str:
    if percentage >= 99:
        return "F"
    elif 1 <= percentage < 99:
        return f"{percentage:.0f}%"
    else:
        return "E"

# Entry point of the script
if __name__ == "__main__":
    main()
