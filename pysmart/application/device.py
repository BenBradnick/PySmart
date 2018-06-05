"""
DEVICE CLASS

Smart device

"""

from pysmart.application.state import State


class Device:

    def __init__(self, name):
        self.name = name
        self.state = State.OFF
