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

    def get_webhook_devices(self, xml_string):
        webhook_device_list = []
        try:
            root = self.get_root(xml_string)
        except ValueError:
            self.logger.error("Could not find root in xml string.")
            return webhook_device_list
        if root is not None:
            webhook_devices = self.find_webhook_devices(root)
            for device in webhook_devices:
                try:
                    xml_ifttt_device = self.parse_webhook_device(device)
                    webhook_device_list.append(xml_ifttt_device)
                except ValueError:
                    self.logger.error("Error parsing device: {0}".format(device))

        return webhook_device_list
