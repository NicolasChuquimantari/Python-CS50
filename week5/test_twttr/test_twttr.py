from twttr import shorten

def test_capital():
    assert shorten("NICOLAS") == "NCLS"
    assert shorten(")

