import unittest
from pysmart.dataaccess.webhookdevicexmlparser import WebhookDeviceXmlParser


class ParsingWebhookDeviceXmlFile(unittest.TestCase):

    def test_parser_gets_one_webhook_device_from_valid_xml_string(self):
        parser = WebhookDeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
            <webhook_device>
                <name>Fairy lights</name>
                <on_webhook_path>fairy_lights_on</on_webhook_path>
                <off_webhook_path>fairy_lights_off</off_webhook_path>
            </webhook_device>
        </devices>"""

        webhook_devices = parser.get_webhook_devices(xml_string)

        self.assertEquals(1, len(webhook_devices))
        self.assertEquals("Fairy lights", webhook_devices[0].name)
        self.assertEquals("fairy_lights_on", webhook_devices[0].on_webhook_path)
        self.assertEquals("fairy_lights_off", webhook_devices[0].off_webhook_path)

    def test_parser_gets_two_webhook_devices_from_valid_string(self):
        parser = WebhookDeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
            <webhook_device>
                <name>Fairy lights</name>
                <on_webhook_path>fairy_lights_on</on_webhook_path>
                <off_webhook_path>fairy_lights_off</off_webhook_path>
            </webhook_device>
            <webhook_device>
                <name>Master bedroom lamp</name>
                <on_webhook_path>master_bedroom_lamp_on</on_webhook_path>
                <off_webhook_path>master_bedroom_lamp_off</off_webhook_path>
            </webhook_device>
        </devices>"""

        webhook_devices = parser.get_webhook_devices(xml_string)

        self.assertEquals(2, len(webhook_devices))
        self.assertEquals("Fairy lights", webhook_devices[0].name)
        self.assertEquals("fairy_lights_on", webhook_devices[0].on_webhook_path)
        self.assertEquals("fairy_lights_off", webhook_devices[0].off_webhook_path)
        self.assertEquals("Master bedroom lamp", webhook_devices[1].name)
        self.assertEquals("master_bedroom_lamp_on", webhook_devices[1].on_webhook_path)
        self.assertEquals("master_bedroom_lamp_off", webhook_devices[1].off_webhook_path)

    def test_empty_webhook_device_element_in_xml_string_returns_no_webhook_devices(self):
        parser = WebhookDeviceXmlParser()
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <devices>
            <webhook_device>
            </webhook_device>
        </devices>"""

        webhook_devices = parser.get_webhook_devices(xml_string)

        self.assertEquals(0, len(webhook_devices))

    def test_empty_xml_string_with_header_returns_empty_webhook_device_list(self):
        parser = WebhookDeviceXmlParser()
        xml_string = '<?xml version="1.0" encoding="UTF-8"?>'

        webhook_devices = parser.get_webhook_devices(xml_string)

        self.assertEquals(0, len(webhook_devices))

    def test_empty_xml_string_returns_empty_webhook_device_list(self):
        parser = WebhookDeviceXmlParser()
        xml_string = ''

        webhook_devices = parser.get_webhook_devices(xml_string)

        self.assertEquals(0, len(webhook_devices))

