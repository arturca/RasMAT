import time
from time import gmtime, strftime
from random import randint

from default_function_and_settings import *

class Clock:
    def __init__(self, previosus_time, previous_line):
        self.previous_time = previosus_time
        self.previous_line = previous_line
        self.queue = []

    def clock(self, strip):
        current_time = strftime("%H:%M", time.localtime())
        position = 0
        if current_time != self.previous_time:
            self.previous_time = current_time
            how_to_wipe = randint(0, 2)

            if how_to_wipe == 0:
                color_wipe_bar(strip, Color(randint(0, 255), randint(0, 255), randint(0, 255)))
            else:
                colorWipe(strip, Color(0, 0, 0), 0)
            for char in current_time:
                if char != ':':
                    set_number(strip, position, int(char))
                    position += 1

    def print_song_name(self, name):
        colorWipe(strip, Color(150, 150, 150), 0)

        self.previous_time = 'x'
        time.sleep(1)
        return
        for letter in name:
            self.queue.append(digits_and_letters.letters_list[ord(letter) - 65])


    def check_logs_file(self, filename):
        logs_file = open(filename)
        lines_of_file = logs_file.readlines()
        logs_file.close()
        if ("loaded" in lines_of_file[len(lines_of_file) - 1]) \
                and (lines_of_file[len(lines_of_file) - 1] != self.previous_line):
            name_of_song = re.search(r"<(.*)\>", lines_of_file[len(lines_of_file) - 1]).group(1)
            self.print_song_name(name_of_song)
            # self.previous_line = lines_of_file[len(lines_of_file) - 1]
            # colorWipe(strip, Color(150, 150, 150), 0)
            # time.sleep(1)
            # self.previous_time = 'x'
        return