
import singleton

s = singleton.Singleton.getInstance()


class TestingMain:

    def __init__(self):
        print("init TestingMain")

if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")
    s.foo = 'foo'