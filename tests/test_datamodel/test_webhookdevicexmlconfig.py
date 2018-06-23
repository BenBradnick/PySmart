import unittest
from pysmart.datamodel.webhookdevicexmlconfig import WebhookDeviceXmlConfig


class CreatingWebhookDeviceXmlConfig(unittest.TestCase):

    def test_name_raises_ValueError_if_None(self):
        name = None
        on_webhook_path = "on_path"
        off_webhook_path = "off_path"
        self.assertRaises(ValueError, WebhookDeviceXmlConfig, name, on_webhook_path,
                          off_webhook_path)

    def test_webhook_on_raises_ValueError_if_None(self):
        name = "Bedroom lamp"
        on_webhook_path = None
        off_webhook_path = "off_path"
        self.assertRaises(ValueError, WebhookDeviceXmlConfig, name, on_webhook_path,
                          off_webhook_path)

    def test_webhook_off_raises_ValueError_if_None(self):
        name = "Bedroom lamp"
        on_webhook_path = "on_path"
        off_webhook_path = None
        self.assertRaises(ValueError, WebhookDeviceXmlConfig, name, on_webhook_path,
                          off_webhook_path)

    def test_attributes_are_initialised_correctly(self):
        name = "Bedroom lamp"
        on_webhook_path = "on_path"
        off_webhook_path = "off_path"

        device = WebhookDeviceXmlConfig(name, on_webhook_path, off_webhook_path)

        self.assertEquals(name, device.name)
        self.assertEquals(on_webhook_path, device.on_webhook_path)
        self.assertEquals(off_webhook_path, device.off_webhook_path)
