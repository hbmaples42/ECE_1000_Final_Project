import time
import board
from rainbowio import colorwheel
import neopixel
from random import choice, uniform
from digitalio import DigitalInOut, Direction, Pull

#NeoPixel setup
pixel_pin = board.GP28
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
#Button Setup
red = DigitalInOut(board.GP27)
red.direction = Direction.INPUT
red.pull = Pull.UP

green = DigitalInOut(board.GP26)
green.direction = Direction.INPUT
green.pull = Pull.UP

blue = DigitalInOut(board.GP22)
blue.direction = Direction.INPUT
blue.pull = Pull.UP

yellow = DigitalInOut(board.GP21)
yellow.direction = Direction.INPUT
yellow.pull = Pull.UP

# RGB Color Codes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 150, 0)
OFF = (0, 0, 0)

#Rainbow Animation
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
#List of colors
colors = [RED, GREEN, BLUE, YELLOW]
#The "attract sequence to entice people to play
for i in range(10):
    rainbow_cycle(0)

while True:
    pixels.fill(OFF)
    pixels.show()
    rnd_colors = []
    player = []
#Wait for the green button start the game
    if green.value == False:
        delay = round(uniform(0.3,1.0),1)
        print(delay)
        for i in range(4):
            rnd_colors.append(choice(colors))
            print(rnd_colors)
        for color in rnd_colors:
            print(color)
            pixels.fill(color)
            pixels.show()
            time.sleep(delay)
            pixels.fill(OFF)
            pixels.show()
            time.sleep(delay)
#Player has four guesses, each guess saves the color choice to player list
        while len(player) <4:
            time.sleep(0.3)
            if red.value == False:
                player.append((255,0,0))
                print(player)
                pixels.fill(RED)
                pixels.show()
                time.sleep(0.1)
                pixels.fill(OFF)
                pixels.show()
            elif green.value == False:
                player.append((0,255,0))
                print(player)
                pixels.fill(GREEN)
                pixels.show()
                time.sleep(0.1)
                pixels.fill(OFF)
                pixels.show()
            elif blue.value == False:
                player.append((0,0,255))
                print(player)
                pixels.fill(BLUE)
                pixels.show()
                time.sleep(0.1)
                pixels.fill(OFF)
                pixels.show()
            elif yellow.value == False:
                player.append((255, 150, 0))
                print(player)
                pixels.fill(YELLOW)
                pixels.show()
                time.sleep(0.1)
                pixels.fill(OFF)
                pixels.show()
#If the player guesses correctly they get a nice rainbow
        if player == rnd_colors:
            for i in range(10):
                rainbow_cycle(0)
#If you lose, you see red!
        else:
            for i in range(3):
                pixels.fill(RED)
                pixels.show()
                time.sleep(0.2)
                pixels.fill(OFF)
                pixels.show()
                time.sleep(0.1)