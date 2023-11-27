# Main function to calculate the total cost of items from a taco menu
def main():
    calculate_total_cost()

# Function to calculate the total cost of selected items from the taco menu
def calculate_total_cost():
    total_cost = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        try:
            # Prompt the user for the item they want
            selected_item = input("Enter the item you want: ").title()

            if selected_item in menu:
                # Add the cost of the selected item to the total
                total_cost += menu[selected_item]
                print(f"Total Cost: ${total_cost:.2f}")
            else:
                print("Item not found in the menu. Please enter a valid item.")
        except EOFError:
            # Exit the loop when an EOF (End of File) is encountered
            break

if __name__ == "__main__":
    # Start the program by calling the main function
    main()
