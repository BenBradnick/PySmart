from pysmart.datamodel.urlmanager import UrlManager


class IFTTTUrlManager(UrlManager):

    def __init__(self, ifttt_api_key):
        hostname = "maker.ifttt.com"
        protocol = "HTTPS"
        super().__init__(hostname, protocol)

        self.raise_value_error_if_none("IFTTT API key", ifttt_api_key)
        self.key = ifttt_api_key

    def build_url(self, path):
        return self.protocol.lower() + "://" + self.hostname + '/trigger/' + path \
            + "/with/key/" + self.key
