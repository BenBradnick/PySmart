import unittest
from unittest.mock import MagicMock
from pysmart.datamodel.iftttdevice import IFTTTDevice


class CreateNewIFTTTDevice(unittest.TestCase):

    def test_on_webhook_path_cannot_be_none(self):
        name = "Lamp switch"
        on_webhook_path = "lamp_on"
        off_webhook_path = None
        url_manager = MagicMock()

        self.assertRaises(ValueError, IFTTTDevice, name, on_webhook_path,
                          off_webhook_path, url_manager)

    def test_off_webhook_path_cannot_be_none(self):
        name = "Lamp switch"
        on_webhook_path = None
        off_webhook_path = "lamp_off"
        url_manager = MagicMock()

        self.assertRaises(ValueError, IFTTTDevice, name, on_webhook_path,
                          off_webhook_path, url_manager)

    def test_url_manager_cannot_be_none(self):
        name = "Lamp switch"
        on_webhook_path = "lamp_on"
        off_webhook_path = "lamp_off"
        url_manager = None

        self.assertRaises(ValueError, IFTTTDevice, name, on_webhook_path,
                          off_webhook_path, url_manager)

    def test_creating_device_with_valid_params_does_not_raise_ValueError(self):
        name = "Lamp switch"
        on_webhook_path = "lamp_on"
        off_webhook_path = "lamp_off"
        url_manager = MagicMock()

        try:
            IFTTTDevice(name, on_webhook_path, off_webhook_path,
                        url_manager)
        except ValueError:
            self.fail("Unexpected ValueError raised")
