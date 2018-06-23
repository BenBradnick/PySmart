from pysmart.dataaccess.xmlparser import XmlParser
from pysmart.utility.exceptionraiser import ExceptionRaiser


class IFTTTApiKeyParser(XmlParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def find_api_key(root):
        return root.find("ifttt_api_key")

    def get_api_key(self, xml_string):
        root = self.get_root(xml_string)
        api_key = self.find_api_key(root)
        return self.get_child_tag_text(api_key, "key")
