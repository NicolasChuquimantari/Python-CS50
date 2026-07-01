from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("H") == False
    assert is_valid("Hi") == True

def test_starts_alpha():
    assert is_valid("Good") == True
    assert is_valid("G1ood") == False

def test_alphanumeric():
    assert is_valid("Python") == True
    assert is_valid("Py.thon") == False


def test_numbers():
    assert is_valid("Bye00") == True
    assert is_valid("G00dbye") == False
