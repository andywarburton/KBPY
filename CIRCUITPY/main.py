"""CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

switch = DigitalInOut(board.D1)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


led = neopixel.NeoPixel(board.NEOPIXEL, 1) 
led.brightness = 0.3
led[0] = (255, 0, 0)

print("ok")

while True:

	if switch.value:
		led[0] = (255, 0, 0)
	else:
		led[0] = (0, 255, 0)

	time.sleep(0.01)  # debounce delay
