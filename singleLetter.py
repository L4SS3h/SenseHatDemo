from sense_hat import SenseHat
from time import sleep
from random import randint
s = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def rndColour():
    rndRed = randint(0,255)
    rndGreen = randint(0,255)
    rndBlue = randint(0,255)
    return(rndRed, rndGreen, rndBlue)


s.show_letter("L", rndColour())
sleep(1)
s.show_letter("A", rndColour())
sleep(1)
s.show_letter("S", rndColour())
sleep(1)
s.show_letter("S", rndColour())
sleep(1)
s.show_letter("E", rndColour())
sleep(1)
s.clear()
