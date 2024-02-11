import busio
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_text import label
import busio
import board
import digitalio
from time import sleep
from random import randint,choice
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
import board
import analogio
import pulseio
buzzer_pin=board.GP5
buzzer = digitalio.DigitalInOut(buzzer_pin)
buzzer.direction = digitalio.Direction.OUTPUT
vrxjoy1=analogio.AnalogIn(board.GP26)
vryjoy1=analogio.AnalogIn(board.GP27)
pin4=digitalio.DigitalInOut(board.GP4)
pin4.switch_to_input(pull=digitalio.Pull.UP)
WIDTH = 128
HEIGHT = 64
displayio.release_displays()
oled_reset = board.GP20
i2c = busio.I2C(board.GP19, board.GP18)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=oled_reset)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

dino_group = displayio.Group()
dinoplayer1 = Rect(64,46,8,16, fill=0xFFFFFF,outline=0xFFFFFF)
ground = Rect(0,63,128,2, fill=0xFFFFFF,outline=0xFFFFFF)
block = Rect(-10,54,8,8, fill=0xFFFFFF,outline=0xFFFFFF)
pplayer1score = 0
player1score = label.Label(terminalio.FONT, text=f"score: {pplayer1score}", x=5,y=10)
def read_j1_vrx():
    return vrxjoy1.value
def read_j1_vry():
    return vryjoy1.value
def ply1R():
    dinoplayer1.x+=3
def ply1L():
    dinoplayer1.x-=3
def play_tone(frequency, duration):
    period = 1 / frequency
    half_period = period / 2
    cycles = int(duration * frequency)
    for _ in range(cycles):
        buzzer.value = True
        sleep(half_period)
        buzzer.value = False
        sleep(half_period)
dino_group.append(dinoplayer1)
dino_group.append(ground)
dino_group.append(block)
dino_group.append(player1score)
onground = True
jumping = False
jumpicol = 0
blockdir = "right"
while True:
    if dinoplayer1.y > 46:
        dinoplayer1.y=46
    sleep(0.05)
    j1x = read_j1_vry()
    j1y = read_j1_vrx()
    if block.y - 8 <= dinoplayer1.y <= block.y + 8 and block.x - 8 <= dinoplayer1.x <= block.x + 8:
        play_tone(2,0.5)
        dinoplayer1.y=16
        pplayer1score=0
        player1score.text = f"score: {pplayer1score}"
    if blockdir == "right":
        block.x+=3
    if blockdir == "left":
        block.x-=3
    if block.x > 132:
        blockdir = "left"
        pplayer1score+=1
        player1score.text = f"score: {pplayer1score}"
    if block.x < -13:
        blockdir = "right"
        pplayer1score+=1
        player1score.text = f"score: {pplayer1score}"
    if jumpicol == 0:
        jumping = False
    if not pin4.value and onground == True:
        if dinoplayer1.y <= 16:
            pass
        else:
            jumping=True
            onground = False
    if dinoplayer1.y < 46 and jumping == False:
        dinoplayer1.y+=3
    if jumping == True:
        if jumpicol < 24 and onground == False:
            dinoplayer1.y-=3
            jumpicol+=2
        if onground == True:
            jumping=True
            jumpicol=0
        if jumpicol == 24:
            jumpicol=0
            jumping=False
    if dinoplayer1.y == 46:
        onground = True
        jumping = False
    if j1x < 5000:
        if dinoplayer1.x > 118:
            pass
        else:
            ply1R()
    if j1x > 55000:
        if dinoplayer1.x < 1:
            pass
        else:
            ply1L()
    display.show(dino_group)