# firebase json result transformed into a python dict
# then the dict is iterated

from firebaseInit import FireBaseInit
from firebase_admin import db

# place all functions at top of module
def doAction(action):
	if action == "Michael D Corbridge":
		print "!!!!!!!!!!!!!!!!!!!!"

# init connection to firebase
fbInit = FireBaseInit()
fbReference = fbInit.init()
result = fbReference.get()

# print type(result)
# print result

print

# iterate through a python dict
for k0 in result:
	print k0
	if k0 == "Jan":
		print "********************"
	for k1 in result[k0]:
		print result[k0][k1]
		doAction(result[k0][k1])
	print "------------"


