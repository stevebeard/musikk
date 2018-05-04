import unittest
import test_utils

from musikk import metadata

class TestMetadata(unittest.TestCase):
    
    def test_get_track_metadata(self):
        filepath = test_utils.get_test_filepath('test.mp3')
        track = metadata.get_track_metadata(filepath)
        # print(track)
        self.assertEqual(track.title, 'Me, Myself & I')
        self.assertEqual(track.artist, 'G-Eazy x Bebe Rexha')
        self.assertEqual(track.album, "When It's Dark Out")

    def test_get_track_metadata_no_data(self):
        filepath = test_utils.get_test_filepath('test_no_metadata.mp3')
        track = metadata.get_track_metadata(filepath)
        # print(track)
        self.assertEqual(track.title, '')
        self.assertEqual(track.artist, '')
        self.assertEqual(track.album, '')
