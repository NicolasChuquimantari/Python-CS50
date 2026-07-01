from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("Goodmorning") == False
    assert is_valid("Hi") == True

def test_starts_alpha():
    assert is_valid("Good") == True
    assert is_valid("1Hello") == False

def test_alphanumeric():
    assert is_valid("Bye") == True
    assert is_valid("Hi-men") == False


def test_numbers():
    assert is_valid("Bye00") == False
    assert is_valid("G00d") == False
    assert is_valid("Bye10") == True
