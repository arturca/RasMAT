
import numpy as np
# from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import argparse
from copy import deepcopy
from random import randint

import data.numbers_and_letters as digits_and_letters
import time
from time import gmtime, strftime

# LED strip configuration:
LED_COUNT = 100  # Number of LED pixels.
LED_PIN = 10  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0 (must be in directory!!! find it)).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
ROWS_NUM = 10
COLS_NUM = 10
# this one create a table that have specific order of elements
helper_list = []
k = 0
k_2 = 0

for i in range(0, 10):
    helper_list.append([])
    k_2 = 0
    for j in range(0, 10):
        if i % 2 == 0:
            helper_list[i].append(k)
            k = k + 1
        else:
            helper_list[i].append(k + 9 - k_2)
            k += 1
            k_2 += 2


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=1):
    """Wipe color across displayScrollLeft a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
        # time.sleep(wait_ms/1000.0)
def color_wipe_bar(strip, color):
    if randint(0,1):
        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                strip.setPixelColor(i*10+j, color)
            strip.show()
            time.sleep(0.1)
            for j in range(COLS_NUM):
                strip.setPixelColor(i * 10 + j, Color(0, 0, 0))
            strip.show()
    else:
        for i in range(ROWS_NUM, -1, -1):
            for j in range(COLS_NUM):
                strip.setPixelColor(i*10+j, color)
            strip.show()
            time.sleep(0.1)
            for j in range(COLS_NUM):
                strip.setPixelColor(i * 10 + j, Color(0, 0, 0))
            strip.show()
    strip.show()

def set_number(strip, position, number):
    if position == 0:
        for i_0 in range(0, 5):
            for j_0 in range(2, 5):
                if digits_and_letters.digits_list[number][i_0][j_0 - 2]:
                    strip.setPixelColor(helper_list[i_0][j_0], Color(255, 0, 0))
    elif position == 1:
        for i_1 in range(0, 5):
            for j_1 in range(6, 9):
                if digits_and_letters.digits_list[number][i_1][j_1 - 6]:
                    strip.setPixelColor(helper_list[i_1][j_1], Color(255, 0, 0))
    elif position == 2:
        for i_2 in range(5, 10):
            for j_2 in range(2, 5):
                if digits_and_letters.digits_list[number][i_2 - 5][j_2 - 2]:
                    strip.setPixelColor(helper_list[i_2][j_2], Color(0, 255, 0))

    elif position == 3:
        for i_3 in range(5, 10):
            for j_3 in range(6, 9):
                if digits_and_letters.digits_list[number][i_3 - 5][j_3 - 6]:
                    strip.setPixelColor(helper_list[i_3][j_3], Color(0, 255, 0))
    strip.show()

