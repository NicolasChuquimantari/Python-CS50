from twttr import shorten

def test_capital():
    assert shorten("NICOLAS") == "NCLS"

def test_lower():
    assert shorten("nicolas") == "ncls"

def test_number()
