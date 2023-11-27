import pytest
from jar import Jar

def test_jar_initialization():
    """
    Test the initialization of the Jar class.
    """
    Jar()

def test_string_representation():
    """
    Test the string representation of the Jar class.
    """
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit_and_size_property():
    """
    Test the deposit function and size property of the Jar class.
    """
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(89)

def test_withdraw():
    """
    Test the withdraw function of the Jar class.
    """
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(64)
