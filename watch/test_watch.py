from watch import parse

def main():
    test_parse()

def test_parse():

    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None

    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

    assert parse('https://www.youtube.com/embed/xvFZjo5PgG0') == None

if __name__ == "__main__":
    main()