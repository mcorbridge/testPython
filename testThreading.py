
import RPi.GPIO as GPIO
import thread
import time

class Foo:

	def __init__(self):
		GPIO.setmode(GPIO.BOARD) 
		GPIO.setup(11, GPIO.OUT) 

	def print_time(self, threadName):
		# ... Job code here ...
		print ("LED on")
		GPIO.output(11, GPIO.HIGH)  # led on
		time.sleep(2)
		print ("LED off")
		GPIO.output(11, GPIO.LOW) # led off
		time.sleep(2)

	def start(self):
		try:
			thread_1 = thread.start_new_thread( self.print_time, ("blink") )
		except:
			print ("Error: unable to start thread")


fooLight = Foo()
fooLight.start()