# !/usr/bin/env python
# -*- coding: utf-8 -*-

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
        # print(self.queue)
        while len(self.queue[0]) > 10:
            colorWipe(self.strip, Color(0, 0, 0), 0)
            self.strip.show()
            for i in range(6):
                for j in range(10):
                    if self.queue[i][j]:
                        self.strip.setPixelColor(helper_list[i+2][j], Color(255, 0, 0))
            self.strip.show()
            self.queue = self.queue[:, 1:]
            time.sleep(0.15)
        self.previous_time = 'x'

    def get_rid_of_polish_sign(self, title):
        # new_title = list(titlee)
        polskie = {"\xc4\x84": "A", "\xc4\x86": "C",
                   "\xc4\x98": "E", "\xc5\x81": "L", "\xc5\x83": "N", "\xc3\x93": "O",
                   "\xc5\x9a": "S", "\xc5\xb9": "Z", "\xc5\xbb": "Z", "\xc4\x85": "a",
                   "\xc4\x87": "c", "\xc4\x99": "e", "\xc5\x82": "l", "\xc5\x84": "n",
                   "\xc3\xB3": "o", "\xc5\x9b": "s", "\xc5\xba": "z", "\xc5\xbc": "z"}

        for x in polskie.keys():
            title = str.replace(title, x, polskie[x])
        return title
        # for i in range(len(u'new_title')):
        #     print(i)
        #     if new_title[i] == 'Ą':
        #         new_title[i] = 'A'
        #     elif new_title[i] == 'Ę':
        #         new_title[i] = 'E'
        #     elif new_title[i] == 'Ć' or new_title[i] == 'ć':
        #         print("jesst Ć")
        #         new_title[i] = 'C'
        #     elif new_title[i] == 'Ł' or new_title[i] == 'ł':
        #         new_title[i] = 'L'
        #     elif new_title[i] == 'Ń' or new_title[i] == 'ń':
        #         new_title[i] = 'N'
        #     elif new_title[i] == 'Ó' or new_title[i] == 'ó':
        #         print("jesst ó")
        #         new_title[i] = 'O'
        #     elif new_title[i] == 'Ś':
        #         new_title[i] = 'S'
        #     elif new_title[i] == 'Ź' or new_title[i] == 'Ż':
        #         new_title[i] = 'Z'
        # print('STOP'.join(new_title) + '--1')
        # return ''.join(new_title)

    def print_song_name(self, name):
        colorWipe(self.strip, Color(0, 0, 0), 0)
        i = 0
        name_2 = self.get_rid_of_polish_sign(name)
        print(name_2)
        name_2 = str.upper(name_2)
        self.queue = np.array(6*[10*[False]])
        for letter in name_2:
                if letter == ' ':
                    self.queue = np.column_stack((self.queue, np.array(6*[2*[False]])))
                if 0 <= ord(letter) - 65 < len(digits_and_letters.letters_list):
                    self.queue = np.column_stack((self.queue, np.array(digits_and_letters.letters_list[ord(letter) - 65])))
                    if letter != 'I' and letter != 'Y' and letter != 'L' and letter != 'E' and letter != 'T' \
                            and letter != 'F':
                        self.queue = np.column_stack((self.queue,
                                                      np.array(6*[[False]])))
        self.queue = np.column_stack((self.queue, np.array(6*[10*[False]])))
        self.queue = np.column_stack((self.queue, self.queue))
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
