# ####################################################################
class Country:
    def __init__(self):
        print("Calling COUNTRY constructor")

        def setAttr(self, attr):
            Country.name = attr

        def getAttr(self):
            print("Country name:", Country.name)

        country = property(setAttr, getAttr)

# ####################################################################
class State:
    def __init__(self):
        print("Calling STATE constructor")

        def setAttr(self, attr):
            State.name = attr

        def getAttr(self):
            print("State name:", State.name)

        state = property(setAttr, getAttr)

# ####################################################################
class County:
    def __init__(self):
        print("Calling COUNTY constructor")

        def setAttr(self, attr):
            County.name = attr

        def getAttr(self):
            print("County name:", County.name)

        county = property(setAttr, getAttr)

# ####################################################################
class City:
    def __init__(self):
        print("Calling CITY constructor")

        def setAttr(self, attr):
            City.name = attr

        def getAttr(self):
            print("City name:", City.name)

        city = property(setAttr, getAttr)

# ####################################################################
class StreetName:
    def __init__(self):
        print("Calling STREET constructor")

        def setAttr(self, attr):
            StreetName.name = attr

        def getAttr(self):
            print("Street name:", StreetName.name)

        streetName = property(setAttr, getAttr)

# ####################################################################
class StreetNum:
    def __init__(self):
        print("Calling NUMBER constructor")

        def setAttr(self, attr):
            streetNum.value = attr

        def getAttr(self):
            print("Street Number:", streetNum.value)

        streetNum = property(setAttr, getAttr)

# ####################################################################
class POBox:
    def __init__(self):
        print("Calling POBOX constructor")

        def setAttr(self, attr):
            POBox.number = attr

        def getAttr(self):
            print("POBox number:", POBox.number)

        poBox = property(setAttr, getAttr)

# ####################################################################
class ZipCode:
    def __init__(self):
        print("Calling ZIPCODE constructor")

        def setAttr(self, attr):
            ZipCode.code = attr

        def getAttr(self):
            return ZipCode.code

        zipCode = property(setAttr, getAttr)

# ####################################################################
class Type:
    def __init__(self):
        print("Calling TYPE constructor")

        def setAttr(self, attr):
            Type.name = attr

        def getAttr(self):
            return Type.name

        type = property(setAttr, getAttr)

# ####################################################################
class Address(ZipCode, POBox, StreetName, StreetNum, City, County, State, Country, Type):
    def __init__(self,address=None):
        if address != None:
          print("an address was provided!")
        else:
            print("no address was provided")

# ####################################################################
class Person():
    def __init__(self):
        self._age = 0
        self._fname = ''
        self._mname = ''
        self._lname = ''
        self._addresses = object

    listOfAddresses = list()

    @property
    def get_age(self):
        return self._age
    def set_age(self, a):
        if a <= 0:
          print("age must be a non-zero positive integer")
        else:
            self._age = a
    def del_age(self):
        del self._age
    def doc_age(self):
        print("this is the age function")

    @property
    def get_fname(self):
        return self._fname
    def set_fname(self, a):
        self._fname = a
    def del_fname(self):
        del self._fname

    @property
    def get_mname(self):
        return self._mname
    def set_mname(self, a):
        self._mname = a
    def del_mname(self):
        del self._mname

    @property
    def get_lname(self):
        return self._lname
    def set_lname(self, a):
        print("new last name: " + a)
        self._lname = a
    def del_lname(self):
        del self._lname

    @property
    def get_addresses(self):
        return self._addresses
    def _addresses(self, a):
        print("new address: " + a)
        global listOfAddresses
        listOfAddresses.append(a)
        self._addresses = listOfAddresses
    def _addresses(self):
        del self._addresses





homeAddress = Address()
homeAddress.zipCode = '02635'
homeAddress.poBox = '2109'
homeAddress.streetNum = '321'
homeAddress.streetName = 'School St.'
homeAddress.city = 'Cotuit'
homeAddress.county = 'Barnstable'
homeAddress.state = 'Massachusetts'
homeAddress.country = 'United States'
homeAddress.type = 'home address'

workAddress = Address()
workAddress.zipCode = '02190'
workAddress.poBox = '45'
workAddress.streetNum = '197'
workAddress.streetName = '8th St.'
workAddress.city = 'Charlestown'
workAddress.county = 'Sussex'
workAddress.state = 'Massachusetts'
workAddress.country = 'United States'
workAddress.type = 'work address'

michael = Person()
michael.fname = 'Michael'
michael.mname = 'Douglas'
michael.lname = 'Corbridge'
michael.age = -9

# #################################################################
class ArrayOfObjects(Address):

    def __init__(self):
        pass

    listAddresses = list()

    def makeArrayOfObjects(self):

        global listAddresses

        homeAddress = Address()
        homeAddress.zipCode = '02635'
        homeAddress.poBox = '2109'
        homeAddress.streetNum = '321'
        homeAddress.streetName = 'School St.'
        homeAddress.city = 'Cotuit'
        homeAddress.county = 'Barnstable'
        homeAddress.state = 'Massachusetts'
        homeAddress.country = 'United States'
        homeAddress.type = 'home address'

        workAddress = Address()
        workAddress.zipCode = '02190'
        workAddress.poBox = '45'
        workAddress.streetNum = '197'
        workAddress.streetName = '8th St.'
        workAddress.city = 'Charlestown'
        workAddress.county = 'Sussex'
        workAddress.state = 'Massachusetts'
        workAddress.country = 'United States'
        workAddress.type = 'work address'

        capeAddress = Address()
        capeAddress.zipCode = "02635"
        capeAddress.poBox = '45'
        capeAddress.streetNum = '197'
        capeAddress.streetName = '8th St.'
        capeAddress.city = 'Charlestown'
        capeAddress.county = 'Sussex'
        capeAddress.state = 'Massachusetts'
        capeAddress.country = 'United States'
        capeAddress.type = 'Cape Cod address'

        listAddresses = [homeAddress, workAddress, capeAddress]

    def showAddresses(self):
        for i in listAddresses:
            print(i.type)

# #######################################################
class P:

    def __init__(self):
        self._addresses = list()

    @property
    def addresses(self):
        print("P._addresses getter")
        return self._addresses

    @addresses.setter
    def addresses(self, address):
        print("P._addresses setter")
        self._addresses.append(address)

    @property
    def x(self):
        print("P.x getter")
        return self._x

    @x.setter
    def x(self, x):
        print("P.x setter")
        self._x = x

    @property
    def y(self):
        print("P.y getter")
        return self._y

    @y.setter
    def y(self, y):
        print("P.y setter")
        self._y = y

p = P()
p.x = 100
p.y = 100
print( p.x * p.y )

p.addresses = homeAddress
p.addresses = workAddress


print(len(p.addresses))
print(type(p.addresses[0]))
print(p.addresses[0].zipCode + " " + p.addresses[1].zipCode)

if(type(p.addresses[0]) != Address):
    print('this is NOT an address!')
else:
    print('this is an address!')
