from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("H") == False
    assert is_valid("Hi") == True

def test_
