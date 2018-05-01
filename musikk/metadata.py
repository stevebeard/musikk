import collections
import tagpy

class Track(collections.namedtuple('Track', ['title', 'artist', 'album'])):
    """A representation of track metadata"""

def get_track_metadata(filepath):
    f = tagpy.FileRef(filepath)
    tag = f.tag()
    return Track(tag.title, tag.artist, tag.album)