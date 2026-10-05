from time import sleep, localtime
import RPi.GPIO as GPIO
from tm1637 import TM1637
import time


DIO = 24
CLK = 23


class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False

    def run(self):
       while True:
            t = localtime()
            self.show_colon = not self.show_colon
            tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
            time.sleep(0.5)


if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(1)    #亮度 0 - 7
    clock = Clock(tm)
    clock.run()
