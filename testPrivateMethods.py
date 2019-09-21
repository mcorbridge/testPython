
# base class
class Vehicle:
	__type = ""
	__weight = 0
	__color = ""
	__numWheels = 0
	__length = 0
	__height = 0
	__foo = "foo"
	
	def __init__(self):
		print "class Vehicle constructor"
		
	def getFoo(self):
		print self.__foo
		
# class Car inherits from class Vehicle
class Car(Vehicle):
 
	__maxspeed = 0
	__name = ""
	__weight = 0
	__weightUnit = ""

	def __init__(self,supercarType,vehicleWeight,weightUnit):
		Vehicle.__init__(self) # subclasses Vehicle
		self.__type = supercarType
		self.__weight = vehicleWeight
		self.__weightUnit = weightUnit

	def drive(self):
		print self.__type + " maxspeed: " + self.__getMaxSpeed()

	def setMaxSpeed(self,speed,unit="mph"):
		try:
			assert unit == "mph" or unit == "kph"
		except:
			print "ARGUMENT INPUT EXCEPTION: unit of speed can only be 'mph' or 'kph'"
		if unit == "mph":
			self.__maxspeed = str(speed) + " " + unit
		elif unit == "kph":
			self.__maxspeed = str(speed) + " kph"
		
	def __getMaxSpeed(self):
		return self.__maxspeed

	def getWeight(self,unit=""):
		try:
			assert unit == "lbs" or unit == "kg" or unit == ""
		except:
			print "ARGUMENT INPUT EXCEPTION: unit of weight can only be empty, 'lbs' or 'kg'"
		if unit == "" and self.__weightUnit == "lbs":
			print str(self.__weight) + " lbs"
		elif unit == "" and self.__weightUnit == "kg":
			print str(self.__weight) + " kg"
		elif unit == "lbs" and self.__weightUnit == "lbs":
			print str(self.__weight) + " lbs"
		elif unit == "kg" and self.__weightUnit == "lbs":
			wtKg = "{:.0f}".format(self.__weight * 0.453592)
			print str(wtKg) + " kg"
		elif unit == "kg" and self.__weightUnit == "kg":
			print str(self.__weight) + " kg"
		elif unit == "lbs" and self.__weightUnit == "kg":
			wtLbs = "{:.0f}".format(self.__weight * 2.20462)
			print str(wtLbs) + " lbs"
			
	def test_var_args(f_arg, *argv): # accepts a list as an argument
		print "first normal arg:", f_arg
		for arg in argv:
			print "another arg through *argv :", arg
			
	def greet_me(self,**kwargs): # accepts key/value pairs
		if kwargs is not None:
			for key, value in kwargs.iteritems():
				print "%s == %s" %(key,value)
				
class Obu:
	__a = ""
	__b = ""
	__c = ""
	
	def __init__(self,a,b,c):
		print "class Obu constructor"
		self.__a = a
		self.__b = b
		self.__c = c
		
	def getA(self):
		return self.__a
		
	def getB(self):
		return self.__b
		
	def getC(self):
		return self.__c
				
def objectView(obu):
	print obu.getA()
	print obu.getB()
	print obu.getC()
	print obu.a
 
lamborgini = Car("Lamborgini",1000,"kg")
lamborgini.setMaxSpeed(320,"kph")
lamborgini.drive()
lamborgini.getWeight()
lamborgini.getWeight("lbs")
lamborgini.getFoo()
print type(lamborgini)
lamborgini.test_var_args('yasoob','python','eggs','test','alpha','beta','gamma', 'delta')
lamborgini.greet_me(firstName="Jabba", lastName="Hutt")

obj = Obu("a","b","c")
obj.a = "aa"
obj.b = "bb"
obj.c = "cc"
obj.d = "dd"
objectView(obj)

