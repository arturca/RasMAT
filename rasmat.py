

import numpy as np
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
import argparse
from copy import deepcopy

import data.numbers_and_letters as digits_and_letters
import time
from time import gmtime, strftime
from data.clock_file import *
# for watching
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# get track title
import re
from data import *
# for observer
import os
#import time



# previous_name = 'rmsd'

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
    newClock = Clock('x', 'empty', strip)

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    # try:
        while True:
            newClock.clock()
            newClock.check_logs_file('/var/log/librespot.log')

        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
    observer.join()

    # class MyHandler(FileSystemEventHandler):
    #     def __init__(self, strip):
    #         self.strip = strip
    #
    #     def get_title(self, last_line):
    #         title = re.search('"(.*)"', last_line)
    #         return title.group(1)
    #
    #     def displayScrollLeft(self, current_frame_array):
    #         colorWipe(self.strip, Color(0, 0, 0))
    #         for i in range(len(current_frame_array[0])):
    #             for j in range(5):
    #                 if current_frame_array[j][i]:
    #                     strip.setPixelColor(helper_list[9 - i][j + 3], Color(255, 223, 0))
    #
    #     def nextFrame(self, current_frame, queue):
    #
    #         if len(current_frame[0]) <= 10:
    #             current_frame = np.c_[current_frame[:, :], queue[:, 0]]
    #         else:
    #             current_frame = np.c_[current_frame[:, 1:], queue[:, 0]]
    #
    #         queue = queue[:, 1:]
    #
    #         return current_frame, queue
    #
    #     def paint_name_running_left(self):
    #         last_line = ''
    #         with open('/var/log/helper/librespot.log', 'r') as f:
    #             lines = f.read().splitlines()
    #             last_line = lines[-1]
    #         if 'Track' in last_line:
    #             title = self.get_title(last_line)
    #         else:
    #             return
    #         helper_queue = []
    #         queue = []
    #
    #         title = str.upper(title)
    #         print('Song title: ', title)
    #
    #         for letter in title:
    #             if letter == " ":
    #                 pass
    #             else:
    #                 helper_queue.append(digits_and_letters.letters_list[ord(letter) - 65])
    #
    #         current_frame = []
    #         for i in range(5):
    #             queue.append([])
    #             current_frame.append([])
    #
    #         for s in range(len(helper_queue)):
    #             for i in range(5):
    #                 for j in range(3):
    #                     queue[i].append(helper_queue[s][i][j])
    #
    #         queue_array = np.array(queue)
    #
    #         current_frame_array = np.array(current_frame)
    #
    #         while len(queue[0]):
    #             self.displayScrollLeft(current_frame_array)
    #             current_frame_array, queue_array = self.nextFrame(current_frame_array, queue_array)
    #             time.sleep(0.4)
    #
    #     def on_modified(self, event):
    #         self.paint_name_running_left()
    #
