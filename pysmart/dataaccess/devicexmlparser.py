from xml.etree import ElementTree
from pysmart.datamodel.xmliftttdevice import XmlIFTTTDevice
import logging

class DeviceXmlParser:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_root(self, xml_string):
        try:
            return ElementTree.fromstring(xml_string)
        except Exception as e:
            self.logger.error("Could not find root of XML string")
            return None

    def get_child_tag_text(self,parent, name):
        tag = parent.find(name)
        try:
            return tag.text
        except:
            self.logger.warning("Could not find text for required tag: {0}".format(name))

    @staticmethod
    def find_ifttt_devices(root):
        return root.findall("iftttdevice")

    def parse_ifttt_device(self, ifttt_device):
        name = self.get_child_tag_text(ifttt_device, "name")
        on_webhook_path = self.get_child_tag_text(ifttt_device, "on_webhook_path")
        off_webhook_path = self.get_child_tag_text(ifttt_device, "off_webhook_path")

        return XmlIFTTTDevice(name, on_webhook_path, off_webhook_path)

    def get_ifttt_devices(self, xml_string):
        root = self.get_root(xml_string)
        list_ifttt_devices = []
        if root is not None:
            ifttt_devices = self.find_ifttt_devices(root)
            for device in ifttt_devices:
                try:
                    xml_ifttt_device = self.parse_ifttt_device(device)
                    list_ifttt_devices.append(xml_ifttt_device)
                except ValueError:
                    self.logger.error("Error parsing device: {0}".format(device))

        return list_ifttt_devices
