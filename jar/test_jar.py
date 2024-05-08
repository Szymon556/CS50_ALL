from jar import Jar
import pytest

def main():
   test_init()
   test_str()
   test_deposit()
   test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar.deposit(5)

    assert str(jar) == "🍪🍪🍪🍪🍪"

if __name__ == "__main__":
    main()