# Dictionary to store the count of each grocery item input by the user
grocery_counts: dict[str, int] = {}

# Continuously prompt the user for grocery items
while True:
    try:
        # Read the user input for a grocery item
        item_name: str = input()

        # Check if the item is not already in the dictionary, and initialize its count to 0
        if item_name not in grocery_counts:
            grocery_counts[item_name] = 0

        # Increment the count of the grocery item
        grocery_counts[item_name] += 1
    except EOFError:
        # Exit the loop when an EOF (End of File) is encountered
        break

# Convert the dictionary keys (item names) to a sorted list
sorted_items: list[str] = sorted(grocery_counts.keys())

# Iterate over the sorted grocery items and print the count and item name in uppercase
for item in sorted_items:
    print(f"{grocery_counts[item]} {item.upper()}")
