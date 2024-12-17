from  time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

a1=hello()
a2=hi()
a1.start()
sleep(0.2)
a2.start()
a1.join()
a2.join()           


