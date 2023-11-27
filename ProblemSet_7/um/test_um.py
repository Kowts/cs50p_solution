from um import count

# Test case-insensitive counting of the word 'um'.
def test_um_case_variation():
    assert count("Hello, UM, my name is human.") == 1
    assert count("Hello, Um, my name is human.") == 1
    assert count("Hello, Um... um... um... my name is human.") == 3
    assert count("Hello, uM, my name is human.") == 1
    assert count("Hello, um, my name is human.") == 1
    assert count("Hello, uhm, my name is human.") == 0

# Test counting 'um' in various positions.
def test_um_positions():
    assert count("um, Hello, my name is human.") == 1
    assert count("Um my name is human?") == 1
    assert count("my name is human Um") == 1
    assert count("my name is human Um?") == 1
    assert count("UM ...my name is human.") == 1
    assert count("UMM ...my name is human.") == 0

# Test edge cases for counting 'um'.
def test_um_edge_cases():
    assert count("Um? Hello, um, my name is human.") == 2
    assert count("UM!, um, my name is human?") == 2
    assert count("Hello! my name is human? Um?") == 1
    assert count("Hello! my name is human? U.m?") == 0
    assert count("Hello! my name is human? U m!") == 0