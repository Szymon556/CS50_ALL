from numb3rs import validate

def main():
    test_valid_ip()
    test_invalid_ip()
    test_oher()

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_ip():
    assert validate("256.0.1.2") == False
    assert validate("1.1,1.1") == False
    assert validate("1") == False
    assert validate("255.") == False
    assert validate("255.345.1.5") == False

def test_other():
    assert validate("cat") == False
    assert validate("255.2.Dog.2") == False

if __name__ == "__main__":
    main()
