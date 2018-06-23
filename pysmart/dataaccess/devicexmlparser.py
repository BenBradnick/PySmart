from pysmart.datamodel.xmliftttdevice import XmlIFTTTDevice
from pysmart.dataaccess.xmlparser import XmlParser


class DeviceXmlParser(XmlParser):

    def __init__(self):
        super().__init__()

    @staticmethod
    def find_ifttt_devices(root):
        return root.findall("iftttdevice")

    def parse_ifttt_device(self, ifttt_device):
        name = self.get_child_tag_text(ifttt_device, "name")
        on_webhook_path = self.get_child_tag_text(ifttt_device, "on_webhook_path")
        off_webhook_path = self.get_child_tag_text(ifttt_device, "off_webhook_path")

        return XmlIFTTTDevice(name, on_webhook_path, off_webhook_path)

    def get_ifttt_devices(self, xml_string):
        list_ifttt_devices = []
        try:
            root = self.get_root(xml_string)
        except ValueError:
            self.logger.error("Could not find root in xml string.")
            return list_ifttt_devices
        if root is not None:
            ifttt_devices = self.find_ifttt_devices(root)
            for device in ifttt_devices:
                try:
                    xml_ifttt_device = self.parse_ifttt_device(device)
                    list_ifttt_devices.append(xml_ifttt_device)
                except ValueError:
                    self.logger.error("Error parsing device: {0}".format(device))

        return list_ifttt_devices
