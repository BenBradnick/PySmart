import unittest
from pysmart.dataaccess.iftttapixmlparser import IFTTTApiKeyParser


class GettingApiKey(unittest.TestCase):

    def test_api_key_obtained_when_provided_in_xml_string(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
                <ifttt_api_key>
                    <key>abcdefghijklmnop</key>
                </ifttt_api_key>
            </config>
        """
        expected_api_key = "abcdefghijklmnop"
        ifttt_api_key_parser = IFTTTApiKeyParser()

        actual_api_key = ifttt_api_key_parser.get_api_key(xml_string)

        self.assertEquals(expected_api_key, actual_api_key)

    def test_raises_ValueError_if_no_api_key_in_xml_string(self):
        xml_string = """
            <?xml version="1.0" encoding="UTF-8"?>
            <config>
            </config>
        """
        ifttt_api_key_parser = IFTTTApiKeyParser()

        self.assertRaises(ValueError, ifttt_api_key_parser.get_api_key, xml_string)

    def test_raises_ValueError_if_api_key_has_no_key_field_in_xml_string(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
                <ifttt_api_key>
                </ifttt_api_key>
            </config>
        """
        ifttt_api_key_parser = IFTTTApiKeyParser()

        self.assertRaises(ValueError, ifttt_api_key_parser.get_api_key, xml_string)