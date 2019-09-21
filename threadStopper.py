import time
import threading
import signal
import RPi.GPIO as GPIO

LedPin = 11    # pin11
 
 
class Job(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

		# The shutdown_flag is a threading.Event object that
		# indicates whether the thread should be terminated.
		self.shutdown_flag = threading.Event()

		GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
		GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
		GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

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
 
 
class ServiceExit(Exception):
	"""
	Custom exception which is used to trigger the clean exit
	of all running threads and the main program.
	"""
	pass
 
 
def service_shutdown(signum, frame):
	print('Caught signal %d' % signum)
	raise ServiceExit
	
def exit():
	raise ServiceExit
 
def main():

	# Register the signal handlers
	signal.signal(signal.SIGTERM, service_shutdown)
	signal.signal(signal.SIGINT, service_shutdown)
	
	i = 0

	print('Starting main program')

	# Start the job threads
	try:
		j1 = Job()
		# j2 = Job()
		j1.start()
		# j2.start()

		# Keep the main thread running, otherwise signals are ignored.
		while True:
			# print "main thread"
			# i += 1
			# if i > 1000:
			#	raise ServiceExit
			#else:
				time.sleep(0.5)

	except ServiceExit:
		# Terminate the running threads.
		# Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
		j1.shutdown_flag.set()
		# j2.shutdown_flag.set()
		# Wait for the threads to close...
		j1.join()
		# j2.join()
		print('Exiting main program')

 
# main()




	
