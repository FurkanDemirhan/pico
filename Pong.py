import busio
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_text import label
import busio
import board
import digitalio
import time
from random import randint,choice
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
WIDTH = 128
HEIGHT = 64
displayio.release_displays()
oled_reset = board.GP20
try:
    i2c = busio.I2C(board.GP19, board.GP18)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=oled_reset)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
except Exception as e:
    pass
else:
    pass
try:
    pin2 = digitalio.DigitalInOut(board.GP2)
    pin2.switch_to_input(pull=digitalio.Pull.UP)
    pin3 = digitalio.DigitalInOut(board.GP3)
    pin3.switch_to_input(pull=digitalio.Pull.UP)
except Exception as e:
    pass
else:
    pass

sc1= 0
scai= 0
pong_group = displayio.Group()
pad1 = Rect(120,32,3,24, fill= 0xFFFFFF, outline=0xFFFFFF)
padai = Rect(4,32,3,24, fill= 0xFFFFFF, outline=0xFFFFFF)
ball = Rect(64,32,4,4, fill=0xFFFFFF, outline=0xFFFFFF)
score = label.Label(terminalio.FONT, text=f"{scai}-{sc1}", color = 0xFFFFFF, x=58,y=15)
pong_group.append(score)
pong_group.append(pad1)
pong_group.append(padai)
pong_group.append(ball)
def plydw():
    pad1.y+=4
def plyup():
    pad1.y-=4
def aidwn():
    padai.y+=randint(0,1)
def aiup():
    padai.y-=randint(0,1)

paidw = 0
paiup = 0
display.refresh()
bally="up"
ballx="right"

while True:

    time.sleep(0.05)
    if not pin2.value:
        if pad1.y > 38:
            pass
        else:
            paidw = time.monotonic()
            plydw()
    if not pin3.value:
        if pad1.y < 4:
            pass
        else:
            paiup = time.monotonic()
            plyup()
            
    if paidw > 1 or ball.y > padai.y:
        if padai.y > 38:
            pass
        else:
            aidwn()
        paidw = 0
    if paiup > 1 or ball.y < padai.y:
        if padai.y < 4:
            pass
        else:
            aiup()
        paiup = 0
    if ball.x >= 130:
        scai+=1
        score.text = f"{scai}-{sc1}"
        ball.x = 64
        ball.y = 32
    if ball.x <= -10:
        sc1+=1
        score.text = f"{scai}-{sc1}"
        ball.x = 64
        ball.y = 32
    if ball.y <= 1:
        bally="down"
    if ball.y >= 54:
        bally = "up"
    if pad1.y - 3 <= ball.y <= pad1.y + 28 and pad1.x - 9 <= ball.x <= pad1.x + 1:
        ballx = "left"
    if pad1.y == ball.y and pad1.x == ball.x:
        ballx = "left"
    if padai.y - 3 <= ball.y <= padai.y + 28 and padai.x - 1 <= ball.x <= padai.x + 9:
        ballx = "right"
    if padai.y == ball.y and padai.x == ball.x:
        ballx= "right"
    if ballx == "right":
        ball.x+=1
    if ballx == "left":
        ball.x-=1        
    if bally == "up":
        ball.y-=1
    if bally == "down":
        ball.y+=1        
    
    

    display.show(pong_group)