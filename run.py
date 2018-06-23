from pysmart.datamodel.ifttturlmanager import IFTTTUrlManager
from pysmart.datamodel.iftttdevice import IFTTTDevice
from pysmart.dataaccess.filereader import FileReader
from pysmart.dataaccess.devicexmlparser import DeviceXmlParser
from pysmart.dataaccess.iftttapixmlparser import IFTTTApiKeyParser
import logging


def run():

    # Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Console logging
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Device file
    device_xml_filepath = "configuration/config.xml"

    # Read in device file
    file_reader = FileReader()
    xml_string = file_reader.read(device_xml_filepath)

    # Configure URL manager
    api_parser = IFTTTApiKeyParser()
    api_key = api_parser.get_api_key(xml_string)
    url_manager = IFTTTUrlManager(api_key)

    # Get list of devices to configure
    device_parser = DeviceXmlParser()
    xml_ifttt_devices = device_parser.get_ifttt_devices(xml_string)

    # Create devices
    ifttt_devices = []
    for xml_ifttt_device in xml_ifttt_devices:
        ifttt_devices.append(
            IFTTTDevice(
                xml_ifttt_device.name,
                xml_ifttt_device.on_webhook_path,
                xml_ifttt_device.off_webhook_path,
                url_manager
            )
        )

    ifttt_devices[0].turn_on()


if __name__ == "__main__":
    run()
