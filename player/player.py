import gi
gi.require_version('Gst','1.0')
from gi.repository import GLib, Gst

class Player():

    def __init__(self):
        # init gobject threads
        # GObject.threads_init() # no longer required
        # init gstreamer
        Gst.init(None)
        # create gstreamer playbin
        self.playbin = Gst.ElementFactory.make('playbin', None)
        if self.playbin is None:
            raise RuntimeError('failed to create gstreamer playbin')
        # TODO: create gstreamer event loop
        # self.loop = GLib.MainLoop()

    def play(self, uri):
        self.playbin.set_property('uri', uri)
        self.playbin.set_state(Gst.State.PLAYING)

    def close(self):
        # self.loop.quit()
        self.playbin.set_state(Gst.State.NULL)
