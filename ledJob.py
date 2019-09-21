import time
import threading
import signal
import RPi.GPIO as GPIO

LedPin = 11    # pin11


class Job(threading.Thread):

	def __init__(self):
		print "Job constructor"
		threading.Thread.__init__(self)

		# The shutdown_flag is a threading.Event object that
		# indicates whether the thread should be terminated.
		self.shutdown_flag = threading.Event()

		GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
		GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
		# GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

	def run(self):
		print('Thread #%s started' % self.ident)

		while not self.shutdown_flag.is_set():
			# ... Job code here ...
			print "LED on"
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(2)
			print "LED off"
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(2)

		# ... Clean shutdown code here ...
		GPIO.output(LedPin, GPIO.LOW)   # led off
		GPIO.cleanup()
		print('Thread #%s stopped' % self.ident)
		
if __name__ == "__main__":
	job = Job()
	job.run()