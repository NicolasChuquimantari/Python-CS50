from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("Good morning") == False
    assert is_valid("Hi") == True

def test_starts_alpha():
    assert is_valid("Good") == True
    assert is_valid("12Hello") == False

def test_alphanumeric():
    assert is_valid("Bye") == True
    assert is_valid("Hi-men") == False


def test_numbers():
    assert is_valid("Bye00") == True
    assert is_valid("G00dbye") == False
