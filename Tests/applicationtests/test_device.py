import unittest
from pysmart.application.device import Device
from pysmart.application.state import State


class TestDevice(unittest.TestCase):

    def test_new_device_is_in_off_state(self):
        device = Device("Test")
        self.assertEquals(State.OFF, device.state)

    def test_new_device_has_correct_name(self):
        name = "TestName"
        device = Device(name)
        self.assertEquals(name, device.name)
