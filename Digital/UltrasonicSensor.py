from machine import Pin
import utime

TIMEOUT1 = 1000
TIMEOUT2 = 1000

class UltrasonicSensor():

    def __init__(self, pin):
        self.sensor = pin
        self.TIMEOUT1 = 1000
        self.TIMEOUT2 = 1000


    def GetDistance(self) -> str:
        
        self.sensor.init(Pin.OUT)


        self.sensor.low()
        utime.sleep_us(2)
        self.sensor.high()
        utime.sleep_us(10)
        self.sensor.low()

        self.sensor.init(Pin.IN)

        while not self.sensor.value():
            signaloff = utime.ticks_us()
            if (utime.ticks_us() - signaloff) > TIMEOUT1:
                return None
        
        while self.sensor.value():
            signalon = utime.ticks_us()
            if (utime.ticks_us() - signalon) > TIMEOUT2:
                return None

        # Compute the difference between the two recorded times (in microseconds)
        timepassed = signalon - signaloff

        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s

        distance = (timepassed * 0.0343) / 2
        return distance

