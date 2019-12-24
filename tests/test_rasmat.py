import unittest
from rasmat import Clock
clock = Clock()
clock.tick()


class ClockTEST(unittest.TestCase):
    def test(self):
        self.assertEqual(clock.time_str, time.strftime("%H:M"))
