from bank import value

def main():
    test_0()
    test_20()
    test_100()

def test_0():
    assert value("Hello") == "$0"
    assert value("hello, Newman") == "$0"
    assert value("Hello Newman") == "$0"

def test_20():
    assert value("hi") == "$20"
    assert value("How you doing?") == "$20"

def test_100():
    assert value("XYZ") == "$100"
    assert value("Good Morning, America") == "$100"


if __name__ == "__main__":
    main()