import unittest
from data.clock_file import Clock


class TestClock(unittest.TestCase):
    def test_print_song_name(self):
        print(3)
        newClock = Clock('x', 'x')
        result = newClock.print_song_name("Should print this name")
        self.assertEqual(result, "Should print this name")


if __name__ == '__main__':
    unittest.main()