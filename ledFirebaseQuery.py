import RPi.GPIO as GPIO
from firebaseInit import FireBaseInit
from firebase_admin import db
import time
import ledJob

LedPin = 11
isRunning = False
led = ledJob.Job()

# init connection to firebase
def init():
	fbInit = FireBaseInit()
	fbReference = fbInit.init()
	return fbReference

def setup():
	# GPIO.setmode(GPIO.BOARD)
	# GPIO.setup(LedPin, GPIO.OUT)
	# GPIO.output(LedPin, GPIO.HIGH)
	bar = "bar"

def destroy():
	# GPIO.output(LedPin, GPIO.LOW)
	# GPIO.cleanup()
	foo = "foo"

def doFirebaseQuery(fbReference):
	while True:
		query = fbReference.order_by_key().equal_to('Mikey')
		result = query.get()
		username = result['Mikey']['full_name']
		checkFirebaseValue(username)
		time.sleep(5)

def checkFirebaseValue(username):
	global isRunning
	if username == "Michael D Corbridge":
		print username + ": Python programming GENIUS!"
		# GPIO.output(LedPin, GPIO.HIGH)
		if isRunning == False:
			led.run()
			isRunning = True
	else:
		print "This guy ain't no programming genius!"
		# GPIO.output(LedPin, GPIO.LOW)
		if isRunning == True:
			isRunning = False

def startedTimedQuery():
	fbReference = init()
	try:
		doFirebaseQuery(fbReference)
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


setup()
startedTimedQuery()