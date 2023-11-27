class Jar:
    """
    Represents a cookie jar with a specified capacity.

    Attributes:
        capacity (int): The maximum number of cookies the jar can hold.
        size (int): The current number of cookies in the jar.

    Args:
        capacity (int, optional): The initial capacity of the jar (default is 12). Must be non-negative.

    Raises:
        ValueError: If the provided capacity is negative.
    """
    def __init__(self, capacity: int = 12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        Returns a string representation of the jar, using 🍪 to represent each cookie in the jar.
        """
        return "🍪" * self.size

    def deposit(self, amount: int):
        """
        Add cookies to the jar. If there are too many cookies to fit in the jar, raise a ValueError.

        Args:
            amount (int): The number of cookies to deposit.

        Raises:
            ValueError: If the jar cannot accommodate the specified number of cookies.
        """
        if amount > self.capacity or amount + self.size > self.capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        self._size += amount

    def withdraw(self, amount: int):
        """
        Remove cookies from the jar. If there are not enough cookies in the jar, raise a ValueError.

        Args:
            amount (int): The number of cookies to withdraw.

        Raises:
            ValueError: If there are insufficient cookies in the jar.
        """
        if amount > self.size:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._size -= amount

    @property
    def capacity(self):
        """
        The capacity property returns the maximum number of cookies the jar can hold.
        """
        return self._capacity

    @property
    def size(self):
        """
        The size property returns the number of cookies in the jar.
        """
        return self._size

# Testing the jar class
def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print("Jar Capacity:", jar.capacity)
    print("Current Jar Size:", jar.size)

if __name__ == "__main__":
    main()
