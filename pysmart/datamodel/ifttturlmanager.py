from pysmart.datamodel.urlmanager import UrlManager
from pysmart.utility.exceptionraiser import ExceptionRaiser


class IFTTTUrlManager(UrlManager):

    def __init__(self, ifttt_api_key):
        ExceptionRaiser.raise_value_error_if_none("IFTTT API Key", ifttt_api_key)

        hostname = "maker.ifttt.com"
        protocol = "HTTPS"
        super().__init__(hostname, protocol)

        self.key = ifttt_api_key

    def build_url(self, path):
        return self.protocol.lower() + "://" + self.hostname + '/trigger/' + path \
            + "/with/key/" + self.key
