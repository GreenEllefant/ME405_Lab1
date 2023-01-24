"""! @encoder_class.py
This file contains code definitions for encoder behavior. 

@author Jack Ellsworth, Hannah Howe, Mathew Smith
@date   24-Jan-2023
@copyright (c) 2023 by Nobody and released under GNU Public License v3
"""
def constructor_init():
    pinB6= pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN_PP)            #set pinB6 to input
    pinB7= pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN_PP)            #set pinB7 to input
    pinC6= pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.IN_PP)            #set pinC6 to input
    pinC7= pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN_PP)            #set pinC7 to input   
    
    tim4 = pyb.Timer(prescaler=0, period=0xFFFF)             #set Timer to max period
    ch_1B = tim4.channel(1, pyb.Timer.ENC_AB, pin=pinB6) #export timer channel variable											      
    ch_2B = tim4.channel(2, pyb.Timer.ENC_AB, pin=pinB7) #export timer channel variable

    tim3 = pyb.Timer(prescaler=0, period=0xFFFF)             #set Timer to max period
    ch_1C = tim3.channel(1, pyb.Timer.ENC_AB, pin=pinC6) #export timer channel variable											      
    ch_2C = tim3.channel(2, pyb.Timer.ENC_AB, pin=pinC7) #export timer channel variable

    return ch_1B
    


def method_read():
    pass

def method_zero():
    pass

ch_1B = constructor_init()
out = ch_1B.counter()
print(out)