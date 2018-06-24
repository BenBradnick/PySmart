from pysmart.datamodel.webhookdevicexmlconfig import WebhookDeviceXmlConfig
from pysmart.dataaccess.xmlparser import XmlParser


class WebhookDeviceXmlParser(XmlParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def find_webhook_devices(root):
        return root.findall("webhook_device")

    def parse_webhook_device(self, webhook_device):
        name = self.get_child_tag_text(webhook_device, "name")
        on_webhook_path = self.get_child_tag_text(webhook_device, "on_webhook_path")
        off_webhook_path = self.get_child_tag_text(webhook_device, "off_webhook_path")

        return WebhookDeviceXmlConfig(name, on_webhook_path, off_webhook_path)

    def get_webhook_device_configurations(self, xml_string):
        webhook_device_xml_config_list = []
        try:
            root = self.get_root(xml_string)
        except ValueError:
            self.logger.error("Could not find root in xml string.")
            return webhook_device_xml_config_list
        if root is not None:
            webhook_devices = self.find_webhook_devices(root)
            for webhook_device in webhook_devices:
                try:
                    webhook_device_xml_config = self.parse_webhook_device(webhook_device)
                    webhook_device_xml_config_list.append(webhook_device_xml_config)
                except ValueError:
                    self.logger.error("Error parsing webhook_device: {0}".format(
                        webhook_device))

        return webhook_device_xml_config_list
