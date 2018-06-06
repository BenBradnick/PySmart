import unittest
from pysmart.dataaccess.webhooksender import WebhookSender


class TestWebhookSender(unittest.TestCase):

    def test_webhook_sender_builds_correct_url(self):
        hostname = "google.co.uk"
        protocol = "HTTPS"
        path = "/test/path"
        webhook_sender = WebhookSender()
        expected_url = "https://google.co.uk/test/path"

        url = webhook_sender.build_url(hostname, path, protocol)

        self.assertEquals(url, expected_url)