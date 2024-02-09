import usb_hid
from time import sleep
from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)
cl = not cl
while cl and pin2.value and pin4.value:
    if not pin2.value or not pin4.value:
        cl = not cl
    elif cl == True:
        mouse.click(Mouse.LEFT_BUTTON)
        sleep(CS)