import logging
import threading
import time

def worker():
    logging.debug('Starting')
    time.sleep(1)
    k = 0
    while k < 99:
        print("blink Red [" + str(k) + "]")
        time.sleep(0.1)
        k = k + 1
    logging.debug('Exiting')


def my_service():
    logging.debug('Starting')
    time.sleep(1)
    k = 0
    while k < 99:
        print("blink Blue [" + str(k) + "]")
        time.sleep(0.1)
        k = k + 1
    logging.debug('Exiting')



logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()