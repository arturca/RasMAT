import unittest
from data.clock_file import Clock


class TestClock(unittest.TestCase):
    def test_print_song_name(self):
        print(3)
        result = newClock.print_song_name('ab')
        AB = [[False,  True, False,  True,  True,  True],
         [ True, False,  True,  True, False,  True],
         [ True,  True,  True,  True,  True,  True],
         [ True, False,  True,  True, False,  True],
         [ True, False,  True,  True,  True,  True]]
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()