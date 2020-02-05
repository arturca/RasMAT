import time
from time import gmtime, strftime
import re
from data.default_function_and_settings import *
import numpy as np
class Clock:
    def __init__(self, previosus_time, previous_line, strip):
        self.previous_time = previosus_time
        self.previous_line = previous_line
        self.strip = strip
        self.queue = np.array([])

    def clock(self):
        current_time = strftime("%H:%M", time.localtime())
        position = 0
        if current_time != self.previous_time:
            self.previous_time = current_time
            how_to_wipe = randint(0, 2)

            if how_to_wipe == 0:
                color_wipe_bar(self.strip, Color(randint(0, 255), randint(0, 255), randint(0, 255)))
            else:
                colorWipe(self.strip, Color(0, 0, 0), 0)
            for char in current_time:
                if char != ':':
                    set_number(self.strip, position, int(char))
                    position += 1

    def paint_scrolling_name(self):
        print(self.queue)
        while len(self.queue) > 10:
            colorWipe(self.strip, Color(0, 0, 0), 0)
            self.strip.show()
            for i in range(10):
                for j in range(10):
                    if self.queue[i][j]:
                        self.strip.setPixelColor(helper_list[i][j], Color(255, 0, 0))
            self.strip.show()
            self.queue = self.queue[:, 1:]
            time.sleep(1)


    def print_song_name(self, name):
        colorWipe(self.strip, Color(150, 150, 150), 0)
        #time.sleep(1)
        #return
        i = 0
        name = str.upper(name)
        for letter in name:
            if i == 0:
                self.queue = np.array(digits_and_letters.letters_list[ord(letter) - 65])
                i += 1
            else:
                self.queue = np.column_stack((self.queue, np.array(digits_and_letters.letters_list[2])))     # digits_and_letters.letters_list[ord(letter) - 65]

        self.paint_scrolling_name()


    def check_logs_file(self, filename):
        logs_file = open(filename)
        lines_of_file = logs_file.readlines()
        logs_file.close()
        if ("loaded" in lines_of_file[len(lines_of_file) - 1]) \
                and (lines_of_file[len(lines_of_file) - 1] != self.previous_line):
            name_of_song = re.search(r"<(.*)\>", lines_of_file[len(lines_of_file) - 1]).group(1)
            self.previous_line = lines_of_file[len(lines_of_file) - 1]
            self.print_song_name(name_of_song)
            # colorWipe(self.strip, Color(150, 150, 150), 0)
            # time.sleep(1)
            # self.previous_time = 'x'
        return
