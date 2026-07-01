from plates import is_valid

def test_length():
    assert is_valid("Hello") == True
    assert is_valid("H") == False
    assert is_valid("Hi") == True

def test_starts_alpha():
    assert is_valid("Good") == True
    assert is_valid("G1ood") == False



def test_numbers():
    assert is_valid("Harvard50") == True
    assert is valid("Harv50ard") == False
