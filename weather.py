from sense_hat import SenseHat
from time import sleep
s = SenseHat()

red = (255,0,0)
green = (0,255,0)
while True:
    temp = s.get_temperature()
    pres = s.get_pressure()
    humi = s.get_humidity()

    temp = round(temp, 1)
    pres = round(pres, 1)
    humi = round(humi, 1)

    messege = "Temp: " + str(temp) + "| Pres: " + str(pres) + "| Humi: " + str(humi)

    if temp > 18.3 and temp < 26.7:
        bg = green
    else:
        bg = red
    
    s.show_message(messege, scroll_speed=0.5, back_colour=bg)
