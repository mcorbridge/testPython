import RPi.GPIO as GPIO
import time
LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led
	
def blink():
	while True:
		GPIO.output(LedPin, GPIO.HIGH)  # led on
		time.sleep(1)
		GPIO.output(LedPin, GPIO.LOW) # led off
		time.sleep(1)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)   # led off
	GPIO.cleanup()    
             
def startBlink():
	setup()
	try:
		blink()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
		
def altBlink():
	i = 0
	try:
		while i < 2:
			i += 1
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(1)
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(1)
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(0.1)
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
		
def main():
	setup()
	altBlink()
	destroy()
		
if __name__ == '__main__':
    main()