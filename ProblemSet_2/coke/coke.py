# Initialize the initial amount owed.
amount_owed: int = 50

# While there is still an amount owed.
while amount_owed > 0:
    # Print the current amount due.
    print(f"Amount Due: {amount_owed}")

    # Get the coin inserted by the user as an integer.
    coin_inserted: int = int(input("Insert Coin: "))

    # Check if the inserted coin is valid (50, 25, 10, or 5 cents).
    if coin_inserted in [50, 25, 10, 5]:
        # Subtract the value of the inserted coin from the amount owed.
        amount_owed -= coin_inserted

    # If the amount owed becomes negative (customer overpaid), convert it to a positive value and exit the loop.
    if amount_owed < 0:
        amount_owed *= -1
        break

# Print the final amount owed, which should be zero if the customer paid the correct amount.
print(f"Change Owed: {amount_owed}")
