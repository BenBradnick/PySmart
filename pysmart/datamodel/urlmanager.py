import logging
from pysmart.utility.exceptionraiser import ExceptionRaiser


class UrlManager:

    valid_protocols = ["HTTPS", "HTTP"]

    def __init__(self, hostname, protocol="HTTPS"):
        ExceptionRaiser.raise_value_error_if_none("Hostname", hostname)
        ExceptionRaiser.raise_value_error_if_none("Protocol", protocol)
        self.protocol_check(protocol)

        self.logger = logging.getLogger(__name__)
        self.hostname = hostname
        self.protocol = protocol

    def protocol_check(self, protocol):
        if protocol not in self.valid_protocols:
            raise ValueError("Invalid protocol")

    def build_url(self, path):
        return self.protocol.lower() + "://" + self.hostname + '/' + path
