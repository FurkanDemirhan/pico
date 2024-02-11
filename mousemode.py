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
mspeed=5
while mouse_mode:
    kys = keypad.pressed_keys
    vrx = read_j1_vry()
    vry = read_j1_vrx()
    #print(f"{vrx}		{vry}")
    if not pin4.value:
        try:
            mouse.press(Mouse.LEFT_BUTTON)
        except Exception as e:
            pass
        else:
            pass

    if kys:
        if "S16" in kys:
            mouse.press(Mouse.RIGHT_BUTTON)
        if "S15" in kys:
            mouse_mode=False
        if "S14" in kys:
            sleep(0.5)
            mspeed+=1
        if "S13" in kys:
            sleep(0.5)
            mspeed-=1
    
    
    if pin4.value:
         try:
            mouse.release(Mouse.LEFT_BUTTON)
         except Exception as e:
             pass
         else:
            pass
    if kys:
        mouse.release(Mouse.RIGHT_BUTTON)
    
    if vry < 5000:
        sleep(0.00000000000001)
        y-=mspeed
        mouse.move(x,y)
        y=0
    if vry > 55000:
        sleep(0.00000000000001)
        y+=mspeed
        mouse.move(x,y)
        y=0
    if vrx < 5000:
        sleep(0.00000000000001)
        x+=mspeed
        mouse.move(x,y)
        x=0
    if vrx > 55000:
        sleep(0.00000000000001)
        x-=mspeed
        mouse.move(x,y)
        x=0