import os

class TestOsListing:

    def __init__(self):
        print("init TestOsListing")

    def printDirectoryContents(self,sPath):

        for sChild in os.listdir(sPath):
            sChildPath = os.path.join(sPath, sChild)
            if os.path.isdir(sChildPath):
                self.printDirectoryContents(sChildPath)
            else:
                print(sChildPath)


testOsListing = TestOsListing()
testOsListing.printDirectoryContents("C:/Users/m_cor/PycharmProjects/")