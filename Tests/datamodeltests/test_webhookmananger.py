import unittest
from pysmart.datamodel.webhookmanager import WebhookManager


class TestCreatingWebhookManager(unittest.TestCase):

    def test_new_WebhookSender_hostname_cannot_be_None(self):
        hostname = None

        self.assertRaises(ValueError, WebhookManager, hostname)

    def test_new_WebhookSender_hostname_is_correctly_initialised(self):
        hostname = "google.co.uk"
        webhook_sender = WebhookManager(hostname)

        self.assertEquals(hostname, webhook_sender.hostname)

    def test_new_WebhookSender_protocol_cannot_be_None(self):
        protocol = None

        self.assertRaises(ValueError, WebhookManager, protocol)

    def test_new_WebhookSender_protocol_is_initialised_when_valid(self):
        protocol = "HTTPS"
        hostname = "google.co.uk"

        webhook_sender = WebhookManager(hostname, protocol=protocol)

        self.assertEquals(protocol, webhook_sender.protocol)

    def test_new_WebhookSender_throws_ValueError_for_invalid_protocol(self):
        protocol = "FTP"
        hostname = "google.co.uk"

        self.assertRaises(ValueError, WebhookManager, hostname, protocol=protocol)


class TestWebhookManagerRaisesExceptions(unittest.TestCase):

    def test_raise_ValueError_raises_ValueError_exception_when_argument_is_None(self):
        attribute = "Attribute"
        argument = None
        hostname = "google.co.uk"
        webhook_sender = WebhookManager(hostname)

        self.assertRaises(ValueError, webhook_sender.raise_value_error_if_none, attribute, argument)
