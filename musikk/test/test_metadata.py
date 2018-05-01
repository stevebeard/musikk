import unittest
import test_utils

from musikk import metadata

class TestMetadata(unittest.TestCase):
    
    def test_get_track_metadata(self):
        filepath = test_utils.get_test_filepath('test.mp3')
        track = metadata.get_track_metadata(filepath)
        # print(track)
        self.assertEquals(track.title, 'Me, Myself & I')
        self.assertEquals(track.artist, 'G-Eazy x Bebe Rexha')
        self.assertEquals(track.album, "When It's Dark Out")

    def test_get_track_metadata_no_data(self):
        filepath = test_utils.get_test_filepath('test_no_metadata.mp3')
        track = metadata.get_track_metadata(filepath)
        # print(track)
        self.assertEquals(track.title, '')
        self.assertEquals(track.artist, '')
        self.assertEquals(track.album, '')
