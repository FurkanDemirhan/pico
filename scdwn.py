import usb_hid
from adafruit_hid.mouse import Mouse
mouse = Mouse(usb_hid.devices)
mouse.press(Mouse.LEFT_BUTTON)
for i in range(20):
    mouse.move(0,-10)
mouse.release(Mouse.LEFT_BUTTON)