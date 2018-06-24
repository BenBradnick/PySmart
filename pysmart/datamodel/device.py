from pysmart.framework.devicestate import DeviceState
import logging


class Device:

    def __init__(self, name):
        if name is None:
            raise ValueError("Device name can not be None")

        self.name = name
        self.state = DeviceState.OFF
        self.logger = logging.getLogger(__name__)
        self.logger.info("Created device: {0}".format(name))

    def turn_on(self):
        self.state = DeviceState.ON

    def turn_off(self):
        self.state = DeviceState.OFF
