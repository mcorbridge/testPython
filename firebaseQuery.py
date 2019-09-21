from firebaseInit import FireBaseInit
from firebase_admin import db
import time

# init connection to firebase
fbInit = FireBaseInit()
fbReference = fbInit.init()

doQuery = True
currentDob = None
 # query for a single value
while doQuery:
	query = fbReference.order_by_key().limit_to_first(1)
	result = query.get()
	dob = result.items()[0][1]['date_of_birth']
	if currentDob == None:
		currentDob = dob
	elif currentDob != dob:
		doQuery = False # comment this line out to keep script running
		currentDob = dob
		print "the value has changed!!!"
	else:
		print "sleep for 60 seconds"
		time.sleep(60)


