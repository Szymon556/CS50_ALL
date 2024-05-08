from twttr import shorten

def main():
    test_vovels()
    test_VOVELS()
    test_mix_VOVELS()
    test_is_alpha()
    test_punct()

def test_vovels():
    assert shorten("twitter") == "twttr"

def test_VOVELS():
    assert shorten("TWITTER") == "TWTTR"

def test_mix_VOVELS():
    assert shorten("Twitter") == "Twttr"

def test_is_alpha():
    assert shorten("123") == "123"

def test_punct():
    assert shorten("!.?") == "!.?"


if __name__ == "__main__":
    main()