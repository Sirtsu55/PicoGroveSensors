import lcd1602
from machine import I2C,Pin
from time import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = lcd1602.Display(i2c, 2, 16)
d.set_rgb(255, 0, 0)
sleep(1)
d.home()
d.print('Hello ')
d.set_rgb(0, 255, 0)
sleep(1)
d.setCursor(0, 1)
d.print('word ')
d.set_rgb(0, 0, 255)