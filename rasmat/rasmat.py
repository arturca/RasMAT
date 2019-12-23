import numpy as np
#import data.numbers_and_letters

import argparse     # work in terminal

from neopixel import *
from copy import deepcopy
import time

# LED strip configuration:
LED_COUNT = 100  # Number of LED pixels.
LED_PIN = 10  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0 (must be in directory!!! find it)).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_BRG	# if colors of your leds are swaped (lire red for gren and vice versa. You nead to change it to BRG/RGB/GBR)
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

strip.begin()
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(255,0,0))
    time.sleep(1)
    strip.show()
    print(i)
