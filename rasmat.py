# import numpy as np
# import data.numbers_and_letters as NaL
#
# import argparse     # work in terminal
#
# # from neopixel import *
# from copy import deepcopy
# import time
#
# # LED strip configuration:
# LED_COUNT = 100  # Number of LED pixels.
# ROWS = 10
# COLS = 10
# LED_PIN = 10  # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0 (must be in directory!!! find it)).
# LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA = 10  # DMA channel to use for generating signal (try 10)
# LED_BRIGHTNESS = 20  # Set to 0 for darkest and 255 for brightest
# LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
# LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
# #LED_STRIP = ws.WS2811_STRIP_BRG	# if colors of your leds are swaped (lire red for gren and vice versa. You nead to change it to BRG/RGB/GBR)
# #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#

# class Clock:
#     def __init__(self):
#         self.time_str ="21:37"
#
#     def tick(self):
#         if time_str != time.strftime("%H:M"):
#             time_str = time.strftime("%H:M")
#             return True
#         return False
#
#
# class RasMat(Clock):
#     def __init__(self, strip):
#         self.helper_list = []
#         k = 0
#         k_2 =0
#         for i in range(0, 10):
#             helper_list.append([])
#             k_2 = 0
#             for j in range(0, 10):
#                 if i % 2 == 0:
#                     helper_list[i].append(k)
#                     k = k + 1
#                 else:
#                     helper_list[i].append(k + 9 - k_2)
#                     k += 1
#                     k_2 += 2
#         self._strip = strip
#         self.matrix =[]
#         for i in range(ROWS):
#             self.matrix.append([False for i in range(COLS)])
#
#     def setColor(self, i, j, color):
#         strip.setPixelColor(helper_list[i][j], color)
#
#     def color_wipe_matrix_fast(self, color):
#         for i in range(ROWS):
#             for j in range(COLS):
#                 matrix[i][j].setColor(color)
#
#     def display_clock(self):
#         if Clock.tick():
#             for i in range(5):
#                 for j in range(2, 5):
#                     if NaL.digits_list[int(Clock.time_str[0])][i][j-2]:
#                         self.setColor(i, j, Corol(250, 30, 0))
#             for i in range(5):
#                 for j in range(6, 9):
#                     if NaL.digits_list[int(Clock.time_str[1])][i][j-6]:
#                         self.setColor(i, j, Corol(250, 30, 0))
#             for i in range(5, 10):
#                 for j in range(2, 5):
#                     if NaL.digits_list[int(Clock.time_str[3])][i-5][j-2]:
#                         self.setColor(i, j, Corol(0, 30, 250))
#             for i in range(5, 10):
#                 for j in range(6, 9):
#                     if NaL.digits_list[int(Clock.time_str[4])][i-5][j-6]:
#                         self.setColor(i, j, Corol(0, 30, 250))

#strip.begin()
# for i in range(LED_COUNT):
#     strip.setPixelColor(i, Color(255, 0, 0))
#     time.sleep(1)
#     strip.show()
#     print(i)


import numpy as np
from neopixel import *
import argparse
from copy import deepcopy

import data.numbers_and_letters as digits_and_letters
import time
from time import gmtime, strftime

# for watching
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from random import randint
# get track title
import re

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
    for i in range(ROWS_NUM):
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


class Clock:
    def __init__(self, previosus_time):
        self.previous_time = previosus_time

    def clock(self, strip):
        current_time = strftime("%H:%M", time.localtime())
        position = 0
        if current_time != self.previous_time:
            self.previous_time = current_time
            how_to_wipe = randint(0, 2)
            print(how_to_wipe)
            if how_to_wipe == 0:
                color_wipe_bar(strip, Color(randint(0, 255), randint(0, 255), randint(0, 255)))
            else:
                colorWipe(strip, Color(0, 0, 0), 0)
            for char in current_time:
                if char != ':':
                    set_number(strip, position, int(char))
                    position += 1


class MyHandler(FileSystemEventHandler):
    def __init__(self, strip):
        self.strip = strip

    def get_title(self, last_line):
        title = re.search('"(.*)"', last_line)
        return title.group(1)

    def displayScrollLeft(self, current_frame_array):
        colorWipe(self.strip, Color(0, 0, 0))
        for i in range(len(current_frame_array[0])):
            for j in range(5):
                if current_frame_array[j][i]:
                    strip.setPixelColor(helper_list[9 - i][j + 3], Color(255, 223, 0))

    def nextFrame(self, current_frame, queue):

        if len(current_frame[0]) <= 10:
            current_frame = np.c_[current_frame[:, :], queue[:, 0]]
        else:
            current_frame = np.c_[current_frame[:, 1:], queue[:, 0]]

        queue = queue[:, 1:]

        return current_frame, queue

    def paint_name_running_left(self):
        last_line = ''
        with open('/var/log/helper/librespot.log', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
        if 'Track' in last_line:
            title = self.get_title(last_line)
        else:
            return
        helper_queue = []
        queue = []

        title = str.upper(title)
        print('Song title: ', title)

        for letter in title:
            if letter == " ":
                pass
            else:
                helper_queue.append(digits_and_letters.letters_list[ord(letter) - 65])

        current_frame = []
        for i in range(5):
            queue.append([])
            current_frame.append([])

        for s in range(len(helper_queue)):
            for i in range(5):
                for j in range(3):
                    queue[i].append(helper_queue[s][i][j])

        queue_array = np.array(queue)

        current_frame_array = np.array(current_frame)

        while len(queue[0]):
            self.displayScrollLeft(current_frame_array)
            current_frame_array, queue_array = self.nextFrame(current_frame_array, queue_array)
            time.sleep(0.4)

    def on_modified(self, event):
        self.paint_name_running_left()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # Intialize the library (must be called once before other functions).
    strip.begin()

    # checker
    # event_handler = MyHandler(strip)
    # file_observer = Observer()
    # file_observer.schedule(event_handler, path='/var/log/helper', recursive=False)
    # file_observer.start()

    newClock = Clock('x')

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    # try:
        while True:
            newClock.clock(strip)
            strip.setBrightness(255)
    # except KeyboardInterrupt:
    #     observer.stop()

        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
    observer.join()