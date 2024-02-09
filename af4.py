import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices)
kbd.send(Keycode.ALT, Keycode.F4)