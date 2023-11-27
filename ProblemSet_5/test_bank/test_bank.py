from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

# Test return 0
def test_return_zero():
    assert value('hello Heilly') == 0
    assert value('Hello') == 0
    assert value('Hello Gi') == 0

# Test return 20
def test_return_20():
    assert value('How are you doing?') == 20
    assert value('Hi') == 20
    assert value('hey') == 20

# Test return 100
def test_return_100():
    assert value ("What's up?") == 100
    assert value ("What's happening??") == 100
    assert value ('good day') == 100

if __name__ == "__main__":
    main()
