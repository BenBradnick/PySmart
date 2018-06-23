import unittest
from unittest.mock import MagicMock
from pysmart.datamodel.iftttdevice import IFTTTDevice
from pysmart.dataaccess.webhooksender import WebhookSender
from pysmart.framework.httpstatuscodes import StatusCodes
from pysmart.framework.state import State


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


class SwitchingDeviceState(unittest.TestCase):

    def test_turning_on_device_changes_state_to_on_when_http_status_ok(self):
        name = "Lamp switch"
        on_webhook_path = "lamp_on"
        off_webhook_path = "lamp_off"
        url_manager = MagicMock()
        WebhookSender.send = MagicMock()
        WebhookSender.send.return_value = StatusCodes.OK
        device = IFTTTDevice(name, on_webhook_path, off_webhook_path, url_manager)

        device.turn_on()

        WebhookSender.send.assert_called_once()
        self.assertEquals(State.ON, device.state)

    def test_turning_on_device_keeps_state_off_when_http_status_not_ok(self):
        name = "Lamp switch"
        on_webhook_path = "lamp_on"
        off_webhook_path = "lamp_off"
        url_manager = MagicMock()
        WebhookSender.send = MagicMock()
        WebhookSender.send.return_value = StatusCodes.BAD_REQUEST
        device = IFTTTDevice(name, on_webhook_path, off_webhook_path, url_manager)

        device.turn_on()

        WebhookSender.send.assert_called_once()
        self.assertEquals(State.OFF, device.state)
