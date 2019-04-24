from sense_hat import SenseHat
import time
s = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
while True:
    s.show_message("Hello World!", text_colour=red)
