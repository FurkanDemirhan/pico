import board
import analogio
vrxjoy1=analogio.AnalogIn(board.GP26)
vryjoy1=analogio.AnalogIn(board.GP27)
def read_j1_vrx():
    return vrxjoy1.value
def read_j1_vry():
    return vryjoy1.value
while True:
    j1x = read_j1_vry()
    j1y = read_j1_vrx()
    print(f"x:{j1x} 		y:{j1y}")