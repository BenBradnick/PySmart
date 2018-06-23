import unittest
from pysmart.dataaccess.xmlparser import XmlParser


class GetRootMethod(unittest.TestCase):

    def test_raises_ValueError_when_xml_string_is_empty(self):
        xml_string = ""

        self.assertRaises(ValueError, XmlParser.get_root, xml_string)

    def test_raises_TypeError_when_xml_string_is_None(self):
        xml_string = None

        self.assertRaises(TypeError, XmlParser.get_root, xml_string)

    def test_does_not_raise_when_xml_string_has_root(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
                <ifttt_api_key>
                    <key>abcdefghijklmnop</key>
                </ifttt_api_key>
            </config>
        """

        try:
            XmlParser.get_root(xml_string)
        except Exception as e:
            self.fail("No exception expected. Got: {0}".format(e))


class GetChildTagTextMethod(unittest.TestCase):

    def test_raises_ValueError_when_name_does_not_exist(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
                <ifttt_api_key>
                </ifttt_api_key>
                <iftttdevice>
                    <name>Fairy lights</name>
                    <on_webhook_path>fairy_lights_on</on_webhook_path>
                    <off_webhook_path>fairy_lights_off</off_webhook_path>
                </iftttdevice>
                <iftttdevice>
                    <name>Master bedroom lamp</name>
                    <on_webhook_path>master_bedroom_lamp_on</on_webhook_path>
                    <off_webhook_path>master_bedroom_lamp_off</off_webhook_path>
                </iftttdevice>
            </config>
        """
        root = XmlParser.get_root(xml_string)
        ifttt_api_key = root.find("ifttt_api_key")

        self.assertRaises(
            ValueError, XmlParser.get_child_tag_text, ifttt_api_key, "key")

    def test_raises_AttributeError_when_parent_does_not_exist(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
            </config>
        """
        root = XmlParser.get_root(xml_string)
        ifttt_api_key = root.find("ifttt_api_key")

        self.assertRaises(
            AttributeError, XmlParser.get_child_tag_text, ifttt_api_key,"key")

    def test_does_not_raise_when_child_tag_exists(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
            <config>
                <ifttt_api_key>
                    <key>abcdefghijklmnop</key>
                </ifttt_api_key>
            </config>
        """
        root = XmlParser.get_root(xml_string)
        ifttt_api_key = root.find("ifttt_api_key")

        try:
            XmlParser.get_child_tag_text(ifttt_api_key, "key")
        except Exception as e:
            self.fail("Did not expect exception. Got: {0}".format(e))
