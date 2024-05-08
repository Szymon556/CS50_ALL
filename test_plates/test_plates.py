from plates import is_valid

def test_letters():
    assert is_valid("C50S") == False
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("5") == False
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("55") == False
    assert is_valid("6666") == False

def test_length():
    assert is_valid("OUTTAME") == False
    assert is_valid("H") == False
    assert is_valid("KP45") == True

def test_order():
    assert is_valid("50CS") == False
    assert is_valid("CS05") == False
    assert is_valid("CS5K") == False
    assert is_valid("CS05") == False


def test_interpuction():
    assert is_valid("KP.56") == False
    assert is_valid("CS50?") == False


def main():
    test_letter()
    test_length()
    test_order()

if __name__ == "__main__":
    main()