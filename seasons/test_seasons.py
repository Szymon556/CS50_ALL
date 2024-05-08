from seasons import validate_time
import pytest
def main():
    test_validate_time()

def test_validate_time():
    assert validate_time("February 6th, 1998") == None
    assert validate_time("2002-10-09") == ["2002","10","09"]


if __name__ == "__main__":
    main()