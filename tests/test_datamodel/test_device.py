import unittest
from pysmart.datamodel.device import Device
from pysmart.framework.devicestate import DeviceState


class CreatingNewDevice(unittest.TestCase):

    def test_new_device_is_in_off_state(self):
        device = Device("Light")

        self.assertEquals(DeviceState.OFF, device.state)

    def test_new_device_has_correct_name(self):
        name = "Light"
        device = Device(name)

        self.assertEquals(name, device.name)

    def test_new_device_name_cannot_be_None(self):
        name = None

        self.assertRaises(ValueError, Device, name)


class SwitchingDeviceState(unittest.TestCase):

    def test_turning_device_on_changes_state_to_on(self):
        device = Device("Light")

        device.turn_on()

        self.assertEquals(DeviceState.ON, device.state)

    def test_turning_device_off_changes_state_to_off(self):
        device = Device("Light")
        device.state = DeviceState.ON

        device.turn_off()

        self.assertEquals(DeviceState.OFF, device.state)
