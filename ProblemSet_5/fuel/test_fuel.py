import pytest
from fuel import convert, gauge

def main():
    test_convert_valid_fraction()
    test_convert_invalid_fraction()
    test_gauge_fuel_reserve()

# Test valid fractions
def test_convert_valid_fraction():
    assert convert("0/1") == 0
    assert convert("3/4") == 75
    assert convert("5/5") == 100
    assert convert("1/2") == 50
    assert convert("1/100") == 1.0

# Test various invalid fractions
def test_convert_invalid_fraction():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("x/y")

# Test fuel reserve gauge
def test_gauge_fuel_reserve():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

if __name__ == "__main__":
    main()
