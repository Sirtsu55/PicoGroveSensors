from machine import Pin, PWM

class ServoController():
    
    def __init__(self, pin, min_pulse_width_ms, max_pulse_width_ms, max_angle):
        self.pin = PWM(Pin(pin))
        self.min_pulse_width = min_pulse_width_ms
        self.max_pulse_width = max_pulse_width_ms
        self.max_angle = max_angle
        self.pin.freq(50)
        self.pin.duty_u16(0)


    def SetAngle(self, angle):
        pulse_width = self.min_pulse_width + (self.max_pulse_width - self.min_pulse_width) * (angle / self.max_angle)
        print(int(pulse_width * 65535 / 20))
        self.pin.duty_u16(int(pulse_width * 65535 / 20))

    def Relax(self):
        self.pin.duty_u16(0)
    
    def ContinuousRotate(self):
        self.pin.duty_u16(32768)
