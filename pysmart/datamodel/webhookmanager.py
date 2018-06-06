import logging
from pysmart.dataaccess.webhooksender import WebhookSender


class WebhookManager:

    valid_protocols = ["HTTPS", "HTTP"]

    def __init__(self, hostname, protocol="HTTPS"):
        self.hostname_check(hostname)
        self.protocol_check(protocol)
        self.hostname = hostname
        self.protocol = protocol
        self.webhook_sender = WebhookSender()
        self.logger = logging.getLogger(__name__)

    def hostname_check(self, hostname):
        self.raise_value_error_if_none("Hostname", hostname)

    def protocol_check(self, protocol):
        self.raise_value_error_if_none("Protocol", protocol)
        if protocol not in self.valid_protocols:
            raise ValueError("Invalid protocol")

    @staticmethod
    def raise_value_error_if_none(attribute, argument):
        if argument is None:
            raise ValueError("{0} cannot be None".format(attribute))
