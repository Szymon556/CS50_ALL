from um import count

def main():
    test_um()

def test_um():
    assert count("yum") == 0
    assert count(" um ") == 1
    assert count("um?") == 1
    assert count("Hello, um world") == 1
    assert count("Um, thanks, um...") == 2



if __name__=="__main__":
    main()
