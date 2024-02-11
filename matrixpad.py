import board
import digitalio
from time import sleep
import adafruit_matrixkeypad

row_pins = [board.GP14, board.GP15, board.GP16, board.GP17]
col_pins = [board.GP10, board.GP11, board.GP12, board.GP13]

row_pins = [digitalio.DigitalInOut(pin) for pin in row_pins]
for pin in row_pins:
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = True
    
col_pins = [digitalio.DigitalInOut(pin) for pin in col_pins]
for pin in col_pins:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    
keypad_layout = [
    ['S13', 'S9', 'S5', 'S1'],
    ['S14', 'S10', 'S6', 'S2'],
    ['S15', 'S11', 'S7', 'S3'],
    ['S16', 'S12', 'S8', 'S4']
]

def scan_keypad():
    pressed_key = None
    for row_num, row_pin in enumerate(row_pins):
        row_pin.value = False
        for col_num, col_pin in enumerate(col_pins):
            if not col_pin.value:
                pressed_key = keypad_layout[row_num][col_num]
        row_pin.value = True
    return pressed_key

while True:
    a = scan_keypad()
    if a:
        print(a)
    sleep(0.1)
            