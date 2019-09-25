

class TestFstring:

    def __init__(self):
        print (f"init TestFstring")


    def showVarInPrint(self):
        foo = "foo"
        status = "fucked"
        party = "GOP"

        print(f"Hello, {foo}. You are {status}.")

        message = ( f"Hi {foo}. "
                    f"You are {status}. "
                    f"You were in the {party}.")

        print(message)


testFstring = TestFstring()
testFstring.showVarInPrint()