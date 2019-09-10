import math

def foo(arg):
    x = 10

    def bar():
        x = 1
        return x

    def qqq():
        x = 2
        return x

    def www():
        x = 3
        return x

    def ggg():
        return pow(2,2)

    switcher = {      # <--- this is a python dictionary
        "bar": bar,
        "qqq": qqq,
        "www": www,
        "ggg": ggg,
    }

    r = switcher.get(arg, "nothing")
    try:
        print(r() * x)
    except:
        print("no way, Jose")

foo("bar")
foo("qqq")
foo("www")
foo("ppp")
foo("ggg")