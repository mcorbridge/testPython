import sys
import builtins

class TestingSys:

    def __init__(self):
        print('looking at some sys functions')
        print(sys.api_version)
        print(sys.argv)
        print(sys.base_exec_prefix)
        print(sys.base_prefix)
        print(sys.builtin_module_names)
        print(sys.byteorder)
        print(sys.copyright)
        print(sys.dllhandle)
        print(sys.exc_info())
        # print(sys.exc_traceback)
        print(sys.executable)
        print(sys.path)
        print(sys.maxsize)
        print(sys.platform)
        print(sys.flags)
        print(sys.float_info)
        print(sys.float_repr_style)
        print(sys._framework)
        print(sys.getdefaultencoding())
        print(sys.getwindowsversion())
        print(sys.getallocatedblocks())
        print(sys.getfilesystemencodeerrors())
        # print(sys.getcheckinterval())
        print(sys.getprofile())
        print(sys.getrecursionlimit())
        print(sys.getswitchinterval())
        print(sys.gettrace())
        print(sys._git)
        print('\n')
        print(sys.getsizeof(self))

testingSys = TestingSys()

class TestingBuiltins:
    def __init__(self):
        print("!!!!!!!!!!! testing builtins !!!!!!!!!")
        print(builtins.copyright())

    def open(path):
        f = builtins.open(path, 'r')
        return UpperCaser(f)

    @staticmethod
    def foo():
        print("this static method does not have any default arguments like 'self' or 'cls'")

class UpperCaser:
    '''Wrapper around a file that converts output to upper-case.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()

testingBuiltins = TestingBuiltins()
# print(testingBuiltins.open(sys.path))
testingBuiltins.foo()