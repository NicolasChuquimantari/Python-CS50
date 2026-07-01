from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("Goodmorning") == False

def test_starts_alpha():
    assert is_valid("Hi") == True
    assert is_valid("H145") == False
    assert is_valid("H1") == False

def test_alphanumeric():
    assert is_valid("Bye") == True
    assert is_valid("Hi-men") == False

def test_numbers():
    assert is_valid("G0od") == False
    assert is_valid("Hell0") == False
