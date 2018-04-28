import unittest

import time
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import pathlib

import player

test_filepath = os.path.join(dir_path, 'test.mp3')
test_file_uri = pathlib.Path(test_filepath).as_uri()

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.instance = player.Player()

    def tearDown(self):
        self.instance.close()

    def testPlay(self):
        self.instance.play_uri(test_file_uri)
        # uncomment to hear audio output
        # time.sleep(5)

if __name__ == '__main__':
    unittest.main()