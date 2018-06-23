import unittest
from pysmart.dataaccess.devicexmlparser import DeviceXmlParser


class ParsingDeviceXmlFile(unittest.TestCase):

    def test_parser_gets_one_ifttt_device_from_valid_xml_string(self):
        parser = DeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
            <iftttdevice>
                <name>Fairy lights</name>
                <on_webhook_path>fairy_lights_on</on_webhook_path>
                <off_webhook_path>fairy_lights_off</off_webhook_path>
            </iftttdevice>
        </devices>"""

        ifttt_devices = parser.get_ifttt_devices(xml_string)

        self.assertEquals(1, len(ifttt_devices))
        self.assertEquals("Fairy lights", ifttt_devices[0].name)
        self.assertEquals("fairy_lights_on", ifttt_devices[0].on_webhook_path)
        self.assertEquals("fairy_lights_off", ifttt_devices[0].off_webhook_path)

    def test_parser_gets_two_ifttt_devices_from_valid_string(self):
        parser = DeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
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
        </devices>"""

        ifttt_devices = parser.get_ifttt_devices(xml_string)

        self.assertEquals(2, len(ifttt_devices))
        self.assertEquals("Fairy lights", ifttt_devices[0].name)
        self.assertEquals("fairy_lights_on", ifttt_devices[0].on_webhook_path)
        self.assertEquals("fairy_lights_off", ifttt_devices[0].off_webhook_path)
        self.assertEquals("Master bedroom lamp", ifttt_devices[1].name)
        self.assertEquals("master_bedroom_lamp_on", ifttt_devices[1].on_webhook_path)
        self.assertEquals("master_bedroom_lamp_off", ifttt_devices[1].off_webhook_path)

    def test_empty_ifttt_device_element_in_xml_string_returns_no_ifttt_devices(self):
        parser = DeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
            <iftttdevice>
            </iftttdevice>
        </devices>"""

        ifttt_devices = parser.get_ifttt_devices(xml_string)

        self.assertEquals(0, len(ifttt_devices))

    def test_empty_xml_string_with_header_returns_empty_ifttt_device_list(self):
        parser = DeviceXmlParser()
        xml_string = '<?xml version="1.0" encoding="UTF-8"?>'

        ifttt_devices = parser.get_ifttt_devices(xml_string)

        self.assertEquals(0, len(ifttt_devices))

    def test_empty_xml_string_returns_empty_ifttt_device_list(self):
        parser = DeviceXmlParser()
        xml_string = ''

        ifttt_devices = parser.get_ifttt_devices(xml_string)

        self.assertEquals(0, len(ifttt_devices))

