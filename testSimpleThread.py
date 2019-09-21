import time
import sys
from simpleThread import Thread
import RPi.GPIO as GPIO

LedPin = 11    # pin11

i = 0
n = 0

def f(): 
	global i
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	i = 0
	try:
		while True:
			i += 1
			print "thread value of i: " + str(i)
			if i > 10:
				stopThread()
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(0.25)
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(0.25)
	finally:
		print "outta here"
		GPIO.output(LedPin, GPIO.LOW)   # led off
		GPIO.cleanup() 

def stopThread():
	global t
	t.terminate()
	t.join()
	t.isAlive()
	
def startThread():
	global t
	t = Thread(target = f)
	t.start()
	t.isAlive()
	
def gpioInit():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	
startThread()

while True:
	print "I am running in the main: " + str(n)
	n += 1
	time.sleep(2)
	if n >= 10:
		n = 0
		startThread()





