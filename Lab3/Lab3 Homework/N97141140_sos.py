import RPi.GPIO as GPIO
import time


PIN1 = 13
PIN2 = 11
freq = 550 #600-800
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)
voice = GPIO.PWM(PIN2,freq)

def led_Buzzer_on(on_time):
    GPIO.output(PIN1,True)
    voice.start(40) #占空比
    time.sleep(on_time)
    GPIO.output(PIN1,False)
    voice.stop()
    time.sleep(0.2)

try:
    #led_Buzzer_on(1.5)


    for i in range(3):
        led_Buzzer_on(0.15)

    time.sleep(0.2) 

    for i in range(3):
        led_Buzzer_on(0.3)

    time.sleep(0.2) 

    for i in range(3):
        led_Buzzer_on(0.15)


except KeyboardInterrupt:
    pass

finally:
    voice.stop()
    GPIO.cleanup()