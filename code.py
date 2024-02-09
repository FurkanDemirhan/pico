from gc import mem_free
freeramstart=mem_free()
import busio
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_text import label
import busio
import board
import digitalio
from time import sleep, monotonic
from random import randint,uniform
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
import analogio
import pulseio
WIDTH = 128
HEIGHT = 64
displayio.release_displays()
oled_reset=board.GP20
i2c=busio.I2C(board.GP19,board.GP18)
display_bus=displayio.I2CDisplay(i2c,device_address=0x3C,reset=oled_reset)
display=adafruit_displayio_ssd1306.SSD1306(display_bus,width=WIDTH,height=HEIGHT)
vrxjoy1=analogio.AnalogIn(board.GP26)
vryjoy1=analogio.AnalogIn(board.GP27)
pin0=digitalio.DigitalInOut(board.GP0)
pin0.switch_to_input(pull=digitalio.Pull.UP)
pin1=digitalio.DigitalInOut(board.GP1)
pin1.switch_to_input(pull=digitalio.Pull.UP)
pin2=digitalio.DigitalInOut(board.GP2)
pin2.switch_to_input(pull=digitalio.Pull.UP)
pin3=digitalio.DigitalInOut(board.GP3)
pin3.switch_to_input(pull=digitalio.Pull.UP)
pin4=digitalio.DigitalInOut(board.GP4)
pin4.switch_to_input(pull=digitalio.Pull.UP)
led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
extra3v3led=board.GP9
exled=digitalio.DigitalInOut(extra3v3led)
exled.direction=digitalio.Direction.OUTPUT
exled.value=False
buzzer_pin=board.GP5
buzzer = digitalio.DigitalInOut(buzzer_pin)
buzzer.direction = digitalio.Direction.OUTPUT
trg=digitalio.DigitalInOut(board.GP6)
trg.direction = digitalio.Direction.OUTPUT
echo=digitalio.DigitalInOut(board.GP7)
echo.direction = digitalio.Direction.INPUT
def read_j1_vrx():
    return vrxjoy1.value
def read_j1_vry():
    return vryjoy1.value
def play_tone(frequency, duration):
    # Calculate the time period for the given frequency
    period = 1 / frequency
    # Calculate half of the time period for toggling the buzzer
    half_period = period / 2
    # Calculate the number of cycles based on the duration
    cycles = int(duration * frequency)
    # Toggle the buzzer pin on and off for the specified duration
    for _ in range(cycles):
        buzzer.value = True
        sleep(half_period)
        buzzer.value = False # this code is not from me its from chat-gpt 3.5
        sleep(half_period)
def get_distance():
    trg.value = True
    sleep(0.00001)
    trg.value = False
    while echo.value == False:
        pulse_start=monotonic()
    while echo.value == True:
        pulse_end=monotonic()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 34300 / 2
    return distance
# Pong Merge Start
sc1=0
scai=0
pong_group = displayio.Group()
pad1=Rect(120,32,4,24,fill=0xFFFFFF,outline=0xFFFFFF)
padai=Rect(4,32,4,24,fill=0xFFFFFF,outline=0xFFFFFF)
ball=Rect(64,32,4,4,fill=0xFFFFFF,outline=0xFFFFFF)
score=label.Label(terminalio.FONT,text=f"{scai}-{sc1}",color=0xFFFFFF,x=56,y=15)
def plydw():
    pad1.y+=2
def plyup():
    pad1.y-=2
def aidwn():
    padai.y+=1
def aiup():
    padai.y-=1
paidw=0
paiup=0
bally="up"
ballx="right"
poncedid = False
# Pong Merge End
# Main Start
main_group=displayio.Group()
HY=25
CS=0.0035
Htext=label.Label(terminalio.FONT, text="Dil Sec\nChoose Language",scale=1, x=0, y=HY)
line=Rect(0, 15, 128, 1, fill=0xFFFFFF, outline=0xFFFFFF)
line2=Rect(0, 48, 128, 1, fill=0xFFFFFF, outline=0xFFFFFF)
key1t=label.Label(terminalio.FONT, text="Turkish",scale=1, x=0, y=5)
key2t=label.Label(terminalio.FONT, text="English",scale=1, x=0, y=55)
Fram=label.Label(terminalio.FONT, text="",x=20,y=40)
arrow2=Polygon(
    points=[
        (110, 55),
        (120, 50),
        (115, 60)
    ],
    outline=0xFFFFFF
)
arrow1=Polygon(
    points=[
        (111, 10),
        (119, 12),
        (117, 0)
    ],
    outline=0xFFFFFF
)
distance= get_distance()
CSUI=label.Label(terminalio.FONT, text=f"{CS}",x=20,y=40)
Fram=label.Label(terminalio.FONT, text="",x=20,y=40)
distui=label.Label(terminalio.FONT, text=f"{distance}",x=20,y=40)
main_group.append(line)
main_group.append(line2)
main_group.append(key1t)
main_group.append(key2t)
#main_group.append(arrow2)
#main_group.append(arrow1)
main_group.append(Htext)
select=1
fp=True
cl=False
ls=False
iss17 = False
lang=0#0=eng 1=TR
lsbug=False
wne = False
# Main End
Mode="Main"
while True:
    j1x = read_j1_vry()
    j1y = read_j1_vrx()
    distance= get_distance()
    display.refresh()
    if Mode == "Main":
        freerammain=mem_free()
        usedram=freeramstart-freerammain
        if select == 17:
            distui.text=f"{distance} cm"
            try:
                main_group.append(distui)
            except Exception as e:
                pass
            else:
                pass
        if ls == False:
            key1t.text="			Turkce"
            key2t.text="		   English"
            if not pin2.value or j1y > 50000:
                lang=0
                ls=True
                key1t.text="			 Next"
                key2t.text="		  Confirm"
                Htext.text="Hello World"
                display.show(main_group)
                display.refresh()
            elif not pin3.value or j1y < 10000:
                lang=1
                ls=True
                key1t.text="			Sonraki"
                key2t.text="			Onayla"
                Htext.text="Merhaba Dunya"
                display.show(main_group)
                display.refresh()
        if ls == True:
            if not pin3.value or j1x < 10000 or j1x > 50000:
                try:
                    main_group.remove(Htext)
                except Exception as e:
                    pass
                else:
                    pass
                try:
                    main_group.remove(CSUI)
                except Exception as e:
                    pass
                else:
                    pass
                try:
                    main_group.remove(Fram)
                except Exception as e:
                    pass
                else:
                    pass
                try:
                    main_group.remove(distui)
                except Exception as e:
                    pass
                else:
                    pass
                if fp == True:
                    select=1
                    fp=False
                else:
                    if j1x > 50000:
                        select-=1
                    if j1x < 10000:
                        select+=1
                    if select > 20:
                        select=1
                    if select < 1:
                        select=20
                display.refresh()
                sleep(0.1)
                if select == 1:
                    if lang == 0:
                        Htext.text="1:Toggle OnBoard LED"
                    if lang == 1:
                        Htext.text="1:LED i Ac/Kapat"
                    main_group.append(Htext)
                if select == 2:
                    if lang == 0:
                        Htext.text="2:Toggle RGB LED"
                    if lang == 1:
                        Htext.text="2:RGB LED i Ac/Kapat"
                    main_group.append(Htext)
                if select == 3:
                    if lang == 0:
                        Htext.text="3:Send Alt-Tab Input"
                    if lang == 1:
                        Htext.text="3:Alt-Tab Gonder"
                    main_group.append(Htext)
                if select == 4:
                    if lang == 0:
                        Htext.text="4:Send Alt-F4 Input"
                    if lang == 1:
                        Htext.text="4:Alt-F4 Gonder"
                    main_group.append(Htext)
                if select == 5:
                    if lang == 0:
                        Htext.text="5:Send Ctrl-Alt-Del"
                    if lang == 1:
                        Htext.text="5:Ctrl-Alt-Del Gonder"
                    main_group.append(Htext)
                if select == 6:
                    if lang == 0:
                        Htext.text="6:Auto Clicker"
                    if lang == 1:
                        Htext.text="6:Otomatik TIklama"
                    main_group.append(Htext)
                if select == 7:
                    if lang == 0:
                        Htext.text="7:Shutdown Windows PC"
                    if lang == 1:
                        Htext.text="7:Windows PC Kapat"
                    main_group.append(Htext)
                if select == 8:
                    if lang == 0:
                        Htext.text="8:Open Explorer"
                    if lang == 1:
                        Htext.text="8:Open Explorer"
                    main_group.append(Htext)
                if select == 9:
                    if lang == 0:
                        Htext.text="9:Lock Pc"
                    if lang == 1:
                        Htext.text="9:BilgisiyarI Kilitle"
                    main_group.append(Htext)
                if select == 10:
                    if lang == 0:
                        Htext.text="10:Scroll Down\nFor Shorts And TikTok"
                    if lang == 1:
                        Htext.text="10:Asagaya kaydIr\nShorts Ve TikTok Icin"
                    main_group.append(Htext)
                if select == 11:
                    if lang == 0:
                        Htext.text="11:Scroll Up\nFor Shorts And TikTok"
                    if lang == 1:
                        Htext.text="11:YukarIya kaydIr\nShorts Ve TikTok Icin"
                    main_group.append(Htext)
                if select == 12:
                    if lang == 0:
                        Htext.text="12:Click Speed +"
                    if lang == 1:
                        Htext.text="12:TIklama HIzI +"
                    main_group.append(Htext)
                    main_group.append(CSUI)
                if select == 13:
                    if lang == 0:
                        Htext.text="13:Click Speed -"
                    if lang == 1:
                        Htext.text="13:TIklama HIzI -"
                    main_group.append(Htext)
                    main_group.append(CSUI)
                if select == 14:
                    if lang == 0:
                        Htext.text="14:Play Pong"
                    if lang == 1:
                        Htext.text="14:Pong Oyna"
                    main_group.append(Htext)
                if select == 15:
                    if lang == 0:
                        Htext.text="15:Free RAM"
                    if lang== 1:
                        Htext.text="15:Bos RAM"
                    main_group.append(Htext)
                    Fram.text=f"{freerammain} KB"
                    main_group.append(Fram)
                if select == 16:
                    if lang == 0:
                        Htext.text="16:Random Sound"
                    if lang == 1:
                        Htext.text="16:Rastgele Ses"
                    main_group.append(Htext)
                if select == 17:
                    if lang == 0:
                        Htext.text="17:Distance:"
                    if lang == 1:
                        Htext.text="17:UzaklIk:"
                    main_group.append(Htext)
                if select == 18:
                    if lang == 0:
                        Htext.text="18:Mouse Mode\nPress Joy1 To Exit"
                    if lang == 1:
                        Htext.text="18:Fare Modu\nCIkmak icin Joy1 E Bas"
                    main_group.append(Htext)
                if select == 19:
                    if lang == 0:
                        Htext.text="19:Mouse Mode\nWith No Exit"
                    if lang == 1:
                        Htext.text="19:Fare Modu\nCIkIs yok"
                    main_group.append(Htext)
                if select == 20:
                    if lang == 0:
                        Htext.text="20:Send Windows-Tab"
                    if lang == 1:
                        Htext.text="20:Windows-Tab Gonder"
                    main_group.append(Htext)
            if not pin2.value or not pin4.value:
                if fp == True:
                    pass
                else:
                    sleep(0.4)
                    if select == 1:
                        led.value=not led.value
                    if select == 2:
                        exled.value=not exled.value
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
                    if select == 8:
                        exec(open("exp.py").read())
                    if select == 9:
                        exec(open("lockpc.py").read())
                    if select == 10:
                        exec(open("scdwn.py").read())
                    if select == 11:
                        exec(open("scup.py").read())
                    if select == 12:
                        CS-=0.0001
                        if CS < 0.000000000:
                            CS=0.0035
                        CSUI.text=f"{CS:.4f}"
                    if select==13:
                        CS+=0.0001
                        if CS < 0.000000000:
                            CS=0.0035
                        CSUI.text=f"{CS:.4f}"
                    if select == 14:
                        Mode="Pong"
                    if select == 15:
                        main_group.remove(Fram)
                        Fram.text=f"{freerammain} KB"
                        main_group.append(Fram)
                    if select == 16:
                        for i in range(10):
                            randsond = randint(1,50)
                            randlong = uniform(1, 3.9)
                            print(f"freq:{randsond}\nlong:{randlong}")
                            play_tone(randsond, randlong)
                    if select == 18:
                        wne = False
                        exec(open("mousemode.py").read(), globals())
                    if select == 19:
                        wne = True
                        exec(open("mousemode.py").read(), globals())
                        wne = False
                    if select == 20:
                        exec(open("wintab.py").read())
        display.refresh()
        display.show(main_group)
    if Mode == "Pong":
        freerammain=mem_free()
        usedram=freeramstart-freerammain
        if poncedid == False:
            pong_group.append(score)
            pong_group.append(pad1)
            pong_group.append(padai)
            pong_group.append(ball)
            poncedid = True
        sleep(0.075)
        if not pin2.value or j1y > 50000:
            if pad1.y > 38:
                pass
            else:
                paidw=monotonic()
                plydw()
        if not pin3.value or j1y < 10000:
            if pad1.y < 4:
                pass
            else:
                paiup=monotonic()
                plyup()
        if paidw > 1 or ball.y > padai.y:
            if padai.y > 38:
                pass
            else:
                aidwn()
            paidw=0
        if paiup > 1 or ball.y < padai.y:
            if padai.y < 4:
                pass
            else:
                aiup()
            paiup=0
        if ball.x >= 130:
            play_tone(2,0.5)
            scai+=1
            score.text=f"{scai}-{sc1}"
            ball.x=64
            ball.y=32
        if ball.x <= -10:
            play_tone(2,0.5)
            sc1+=1
            score.text=f"{scai}-{sc1}"
            ball.x=64
            ball.y=32
        if ball.y <= 1:
            bally="down"
        if ball.y >= 54:
            bally="up"
        if pad1.y - 3 <= ball.y <= pad1.y + 24 and pad1.x - 9 <= ball.x <= pad1.x + 1:
            ballx="left"
        if pad1.y == ball.y and pad1.x == ball.x:
            ballx="left"
        if padai.y - 3 <= ball.y <= padai.y + 24 and padai.x - 1 <= ball.x <= padai.x + 9:
            ballx="right"
        if padai.y == ball.y and padai.x == ball.x:
            ballx="right"
        if ballx=="right":
            ball.x+=4
        if ballx=="left":
            ball.x-=4        
        if bally=="up":
            ball.y-=4
        if bally=="down":
            ball.y+=4
        if not pin2.value and not pin3.value or not pin4.value:
            Mode="Main"
            sleep(1)
        display.refresh()
        display.show(pong_group)