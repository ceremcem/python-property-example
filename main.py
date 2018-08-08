#!/usr/bin/env python
class Stopwatch(object):
    """
    Initially taken from https://stackoverflow.com/a/4481861/1952991
    """
    def __init__(self, callback):
        print "Initialized a stopwatch"
        self._stop = False
        if callback:
            self.callback = callback

    def callback(self):
        print "...about to stop"

    @property
    def stop(self): return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value
        if value: self.callback()


x = Stopwatch(None)

x.stop = True
