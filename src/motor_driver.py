class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        self.en_pin = en_pin
        self.in1pin = in1pin
        self.in2pin = in2pin
        self.timer = timer
        self.ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.in1pin)
        self.ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.in2pin)
        self.en_pin.high()
        ch1.pulse_width_percent(0)
        ch2.pulse_width_percent(0)
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        if(level > 0):
            self.ch1.pulse_width_percent(level)
            self.ch2.pulse_width_percent(0)
        elif(level < 0):
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(level)
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(0)
        print (f"Setting duty cycle to {level}")
    
if __name__ == "__main__":
    en_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    in1pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    in2pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    tim = pyb.Timer(3, prescalar = 0 , preiod = 0xFFFF)
    moe = MotorDriver(en_pin, in1pin, in2pin, tim)
    moe.set_duty_cycle(-42)
