import logging
from pysmart.datamodel.device import Device


class DeviceManager:

    def __init__(self, devices=None):
        self.logger = logging.getLogger(__name__)
        self.device_list = []

        if devices is not None:
            self.add_list(devices)

    def add(self, device):
        if isinstance(device, Device):
            if self.device_with_same_name_already_exists(device):
                raise ValueError("Device already exists with same name")
            self.device_list.append(device)
        else:
            raise TypeError("Cannot add type {0} to device list".format(type(device)))

    def add_list(self, devices):
        if isinstance(devices, list):
            for device in devices:
                self.add(device)
        elif isinstance(devices, Device):
            self.add(devices)
        else:
            raise TypeError("Expected type Device or list. Got {0}".format(type(devices)))

    def find(self, device_name):
        for device in self.device_list:
            if device.name == device_name:
                return device
        return None

    def device_with_same_name_already_exists(self, new_device):
        for device in self.device_list:
            if new_device.name == device.name:
                return True
        return False

    def delete(self, device_name):
        for index, device in enumerate(self.device_list):
            if device.name == device_name:
                del self.device_list[index]
                return

    # TODO: turn on and turn off methods by name
