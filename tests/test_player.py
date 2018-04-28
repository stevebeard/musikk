import unittest

import time
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import pathlib

import player

def get_test_file_uri(filename):
    filepath = os.path.join(dir_path, filename)
    return pathlib.Path(filepath).as_uri()

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.instance = player.Player()

    def tearDown(self):
        self.instance.close()

    def test_play_uri(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        # time.sleep(5)

    def test_play_uri_when_playing(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(2)
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(6)

    def test_play_uri_then_stop(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(5)
        self.instance.stop()

    def test_play_uri_then_stop_then_play(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(5)
        self.instance.stop()
        self.instance.play()
        # uncomment to hear audio output
        time.sleep(5)

    def test_play_uri_then_pause(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(5)
        self.instance.pause()

    def test_play_uri_then_pause_then_play(self):
        self.instance.play_uri(get_test_file_uri('test.mp3'))
        # uncomment to hear audio output
        time.sleep(5)
        self.instance.pause()
        # uncomment to hear audio output
        time.sleep(1)
        self.instance.play()
        # uncomment to hear audio output
        time.sleep(5)

    def test_set_next_uri(self):
        self.instance.play_uri(get_test_file_uri('short.mp3'))
        self.instance.set_next_uri(get_test_file_uri('short.mp3'))
        # uncomment to hear audio output
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()