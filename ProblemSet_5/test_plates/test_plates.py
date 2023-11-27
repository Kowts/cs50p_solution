from plates import is_valid  # Replace 'your_script_file' with the actual filename

def main():
    test_start_with_letters()
    test_length_constraints()
    test_number_placement()
    test_blocked_symbols()

# Vanity plates must start with at least two letters.
def test_start_with_letters():
    assert is_valid("AB12") == True
    assert is_valid("1") == False
    assert is_valid("22") == False
    assert is_valid("AA") == True

# Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters.
def test_length_constraints():
    assert is_valid("A") == False
    assert is_valid("ABCDEF12") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True

# Numbers cannot be used in the middle of a plate; they must come at the end.
def test_number_placement():
    assert is_valid("ABC12") == True
    assert is_valid("A12B") == False
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("XYZ012") == False
    assert is_valid("AB12") == True
    assert is_valid("AB12CA") == False
    assert is_valid("ABC123") == True
    assert is_valid("AB1234") == True

# No periods, spaces, or punctuation marks are allowed.
def test_blocked_symbols():
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^D3*") == False

if __name__ == "__main__":
    main()
