import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from time import sleep
kbd = Keyboard(usb_hid.devices)
shutcmdt = [Keycode.S, Keycode.H, Keycode.U, Keycode.T, Keycode.D, Keycode.O, Keycode.W, Keycode.N, Keycode.SPACE, Keycode.KEYPAD_MINUS, Keycode.S, Keycode.SPACE, Keycode.KEYPAD_MINUS, Keycode.T, Keycode.SPACE, Keycode.ZERO]
kbd.send(Keycode.WINDOWS, Keycode.R)
sleep(0.4)
for keycode in shutcmdt:
    kbd.send(keycode)
    sleep(0.1)
kbd.send(Keycode.RETURN)