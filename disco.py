from sense_hat import SenseHat
from time import sleep
from random import randint
s = SenseHat()
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

def rndColour():
    rndRed = randint(0,255)
    rndGreen = randint(0,255)
    rndBlue = randint(0,255)
    return(rndRed, rndGreen, rndBlue)
# solid color for all pixels
# s.clear(r)
sleeptime = 10 

while True:
  s.clear(rndColour())
  sleep(sleeptime)
  
  if sleeptime > 0:
    sleeptime -= 2
  if sleeptime < 0:
    sleeptime = 0
        
