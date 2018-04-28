import sys
import threading

import gi
gi.require_version('Gst','1.0')
from gi.repository import GLib, Gst

def gst_event_loop(loop, playbin):
    try:
        loop.run()
    except:
        pass
    # cleanup
    playbin.set_state(Gst.State.NULL)

def bus_call(bus, message, loop):
    t = message.type
    if t == Gst.MessageType.EOS:
        sys.stdout.write('GST: End of Stream\n')
        loop.quit()
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        sys.stderr.write("Error: %s: %s\n" % (err, debug))
        loop.quit()
    return True

class Player():

    def __init__(self):
        # init gobject threads
        # GObject.threads_init() # no longer required
        # init gstreamer
        Gst.init(None)
    
    def play_uri(self, uri):
        # create gstreamer playbin
        self.playbin = Gst.ElementFactory.make('playbin', None)
        if self.playbin is None:
            raise RuntimeError('failed to create gstreamer playbin')        
        # create gstreamer event loop
        self.loop = GLib.MainLoop()
        # configure bus callbacks
        self.bus = self.playbin.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', bus_call, self.loop)
        self.playbin.set_property('uri', uri)
        self.playbin.set_state(Gst.State.PLAYING)
        self.playthread = threading.Thread(target=gst_event_loop, args=(self.loop, self.playbin,))
        self.playthread.start()
    
    def close(self):
        self.playbin.set_state(Gst.State.NULL)
        self.loop.quit()
        self.playthread.join()

