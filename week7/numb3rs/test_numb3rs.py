from numb3rs import validate

def test_ip_format():
    assert validate("210.34.4.32") == True
    assert validate("10.20.30") == False
    assert validate("44.90.30.hello") == False

def test_number():
    assert validate("100.0.50.25") == True
    assert validate("159.23.0.280") == False

