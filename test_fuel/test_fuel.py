from fuel import convert, gauge
import pytest

def test_Value():
    with pytest.raises(ValueError):
        convert("cat/5") == "Only Integers"
def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0") == "Cant Devide by Zero"
def test_input():
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("1/4") == 25 and gauge(25) == "25%"

def main():
    test_Value()
    test_devide_by_zero()

if __name__ == "__main__":
    main()