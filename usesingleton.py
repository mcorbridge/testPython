from singleton import Singleton


class UseSingleton:
    def __init__(self):
        print("UseSingleton constructor")
        singleton = Singleton.getInstance()
        singleton.foo = 'foo'