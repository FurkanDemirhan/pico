import analogio
import busio
import board
import digitalio
import usb_hid
from time import sleep
from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)
mouse_mode = True
def read_j1_vrx():
    return vrxjoy1.value
def read_j1_vry():
    return vryjoy1.value
x=0
y=0
while mouse_mode:
    vrx = read_j1_vry()
    vry = read_j1_vrx()
    #print(f"{vrx}		{vry}")
    if not pin4.value:
        if wne == False:
            mouse_mode=False
        if wne == True:
            sleep(0.035)
            mouse.click(Mouse.LEFT_BUTTON)
                
    
    if vry < 5000:
        sleep(0.00000000000001)
        y-=5
        mouse.move(x,y)
        y=0
    if vry > 55000:
        sleep(0.00000000000001)
        y+=5
        mouse.move(x,y)
        y=0
    if vrx < 5000:
        sleep(0.00000000000001)
        x+=5
        mouse.move(x,y)
        x=0
    if vrx > 55000:
        sleep(0.00000000000001)
        x-=5
        mouse.move(x,y)
        x=0