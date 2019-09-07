

class TestString:

    def __init__(self):
        print("TestString Constructor")

    @staticmethod
    def stringOperations():

        foo = "foo is foo"

        print(foo + " !!!!!")

        print(foo.encode())

        print(foo.capitalize())

        print("ThE Rain In SPAin FAllS Mainly on the PLaIn".casefold())

        print("Now is our winter of discontent".count(" is "))

        print("Now is our winter of discontent".endswith("discontent"))

        # unicode string
        string = 'pythön!'
        # print string
        print('The string is:', string)
        # default encoding to utf-8
        string_utf = string.encode()
        # print result
        print('The encoded version is:', string_utf)

        print("mikeCorbridge@gmail.com".encode())

        print("mikeCorbridge@gmail.com".find("com"))

        sentence = 'Python programming is fun.'

        result = sentence.index('is fun')
        print("Substring 'is fun':", result)

        try:
            result = sentence.index('Java')
            print("Substring 'Java':", result)
        except:
            print("there is no fucking substring 'Java'")

        name = "M234onica"
        print(name.isalnum())

        # contains whitespace
        name = "M3onica Gell22er "
        print(name.isalnum())

        name = "Mo3nicaGell22er"
        print(name.isalnum())

        name = "133"
        print(name.isalnum())

        email = "mikecorbridge@gmail.com"

        print(email + " length = " + str(len(email)))

        for i in range(0,len(email)):
            print(email[i])
            if(email[19]) == '.':
                email = "mikecorbridge@gmail*com"

        print(email)

        loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
                 "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea " \
                 "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
                 "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa " \
                 "qui officia deserunt mollit anim id est laborum."

        loremIpsumArr = loremIpsum.split()

        for word in loremIpsumArr:
                print(word)

        print(loremIpsumArr[19])

        loremIpsumArr[19] = "*FooFoo*"

        print(loremIpsumArr)

        str1 = ' '.join(loremIpsumArr)

        print(str1)

        loremIpsum = str1

        print(loremIpsum)


print("=======================================================================")

TestString.stringOperations()