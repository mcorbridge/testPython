import ledModule
from firebaseInit import FireBaseInit
from firebase_admin import db

# init connection to firebase
fbInit = FireBaseInit()
fbReference = fbInit.init()

query = fbReference.order_by_key().equal_to('Mikey')
result = query.get()

username = result['Mikey']['full_name']

if username == "Michael D Corbridge":
	print username + ": Python programming GENIUS!"
	ledModule.startBlink()
else:
	print "This guy ain't no programming genius!"
	


