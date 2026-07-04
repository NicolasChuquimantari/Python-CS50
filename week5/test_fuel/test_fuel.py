from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("5/5") == 100

    with pytest.raises(ValueError):
        convert("-10/5")

    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"



