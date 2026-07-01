from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("Hi") == 20
    assert value("HI") == 20

def test_else():
    assert value("What are you doing?") == 100
    assert value("WHAT ARE YOU DOING?") == 100

