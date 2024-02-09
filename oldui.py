import board
import digitalio
import time
#from audiocore import WaveFile
#from audiopwmio import PWMAudioOut as AudioOut
#import audiocore
import os
import busio
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_text import label
import busio
WIDTH = 128
HEIGHT = 64
BORDER = 5
try:
    displayio.release_displays()
    oled_reset = board.GP20
    i2c = busio.I2C(board.GP19, board.GP18)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=oled_reset)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
except Exception as e:
    pass
else:
    pass


pin0 = digitalio.DigitalInOut(board.GP0)
pin0.switch_to_input(pull=digitalio.Pull.UP)
pin1 = digitalio.DigitalInOut(board.GP1)
pin1.switch_to_input(pull=digitalio.Pull.UP)
pin2 = digitalio.DigitalInOut(board.GP2)
pin2.switch_to_input(pull=digitalio.Pull.UP)
pin3 = digitalio.DigitalInOut(board.GP3)
pin3.switch_to_input(pull=digitalio.Pull.UP)
pin4 = digitalio.DigitalInOut(board.GP4)
pin4.switch_to_input(pull=digitalio.Pull.UP)
pin5 = digitalio.DigitalInOut(board.GP5)
pin5.switch_to_input(pull=digitalio.Pull.UP)
pin6 = digitalio.DigitalInOut(board.GP6)
pin6.switch_to_input(pull=digitalio.Pull.UP)
pin7 = digitalio.DigitalInOut(board.GP7)
pin7.switch_to_input(pull=digitalio.Pull.UP)


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
extra3v3led = board.GP9
exled = digitalio.DigitalInOut(extra3v3led)
exled.direction = digitalio.Direction.OUTPUT
exled.value = True



#wavf = open("virus.wav", "rb")
#wave = WaveFile(wavf)
#audio = AudioOut(board.GP20)

def clearss():
    print("\n" * 4)

print("Hello World!\nMerhaba Dunya!")
select = 1
fp = False
cl = False
while True:
    if not pin3.value:
        time.sleep(0.5)
        clearss()
        if fp == False:
            select = 1
            fp = True
        else:
            select+=1
            if select > 7:
                select = 1
            if select < 1:
                select = 7
        if select == 1:
            print("1: Toggle OnBoard LED\n1: LED i Ac/Kapat")
        if select == 2:
            print("2: Toggle RGB LED\n2: RGB LED i Ac/Kapat" )
        if select == 3:
            print("3: Send Alt-Tab Input\n3: Alt-Tab Gonder")
        if select == 4:
            print("4: Send Alt-F4 Input\n4: Alt-F4 Gonder")
        if select == 5:
            print("5:Send Ctrl-Alt-Del\n5:Ctrl-Alt-Del Gonder")
        if select == 6:
            print("6: Auto Clicker\n6: Otomatik Tiklama")
        if select == 7:
            print("7:Shutdown Windows PC\n7:Windows PC Kapat")
    if not pin2.value:
        time.sleep(0.5)
        if select == 1:
            led.value = not led.value
        if select == 2:
            exled.value = not exled.value
        if select == 3:
            exec(open("atab.py").read())
        if select == 4:
            exec(open("af4.py").read())
        if select == 5:
            exec(open("cadel.py").read())
        if select == 6:
            exec(open("autoclick.py").read(), globals())
        if select == 7:
            exec(open("shut.py").read())