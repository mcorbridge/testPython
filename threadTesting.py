import time
import threading


class Job(threading.Thread):

	def __init__(self):
		print "Job constructor"
		threading.Thread.__init__(self)

		# The shutdown_flag is a threading.Event object that
		# indicates whether the thread should be terminated.
		self.shutdown_flag = threading.Event()

	def run(self):
		print('Thread #%s started' % self.ident)

		while not self.shutdown_flag.is_set():
			# ... Job code here ...
			print "threading..."

		# ... Clean shutdown code here ...
		print('Thread #%s stopped' % self.ident)
		
		
job = Job()
job.run()