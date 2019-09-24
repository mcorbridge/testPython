"""
Using docstring as a comment.
"""

import array
import numbers
import calendar
import datetime
# import jsonschema
# import audioop
# import abc
# import aifc
# import antigravity
# import argparse
# import ast
# import asynchat
# import asyncio
# import asyncore
# import atexit
# import lzma
# import apitools.base.py.exceptions
# import random
# import jsonschema.validators
# import cmath
# import copyreg
import hashlib

class TestingPythonArrays:

    """
    docs for TestingPythonArrays
    as if it really needs any explanation
    """

    def __init__(self):
        print("init TestingPythonArrays")
        # help(hashlib)


    def makeArray(self):
        intArr = array.array('i', [0,1,2,3,4,5,6,7,8,9,])
        charArr = array.array('u',['f','b','q'])
        print(intArr)
        print(charArr)
        # help('array')

    def testNumbersModule(self):
        n = numbers.Number()
        # c = numbers.Complex()
        print(n)

    def testCalendar(self):
        m = calendar.month
        c = calendar.Calendar
        fwd = c.firstweekday
        # help(calendar)
        now = datetime.datetime.now()
        print(now.month)
        # print(c.monthdatescalendar(2019,now.month))

    def testingHashlib(self):
        password = b'wally'
        hash = hashlib.sha224(password)
        d = hash.digest()
        hd = hashlib.sha224(password).hexdigest()
        print(hashlib.md5(password).hexdigest())

        if (hashlib.sha224(password).hexdigest()) == '7def3ae0c8ad8a3fd6040b3b379b902750fe787ad7a360392c2876de':
            print("valid password")
        else:
            print("invalid password")

        h = 'wally'.encode().hex()

        for n in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            a = n.encode().hex()
            print(a)








testingPythonArrays  = TestingPythonArrays()
testingPythonArrays.makeArray()
testingPythonArrays.testNumbersModule()
testingPythonArrays.testCalendar()
testingPythonArrays.testingHashlib()
