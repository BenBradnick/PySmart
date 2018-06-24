from pysmart.datamodel.ifttturlmanager import IFTTTUrlManager
from pysmart.datamodel.webhookdevice import WebhookDevice
from pysmart.dataaccess.filereader import FileReader
from pysmart.dataaccess.webhookdevicexmlparser import WebhookDeviceXmlParser
from pysmart.dataaccess.iftttapixmlparser import IFTTTApiKeyParser
from pysmart.datamodel.devicemanager import DeviceManager
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

    # Read in configuration file
    configuration_filepath = "configuration/config.xml"
    file_reader = FileReader()
    xml_string = file_reader.read(configuration_filepath)

    # Configure URL manager
    api_parser = IFTTTApiKeyParser()
    api_key = api_parser.get_api_key(xml_string)
    url_manager = IFTTTUrlManager(api_key)

    # Get list of device configurations
    device_parser = WebhookDeviceXmlParser()
    webhook_device_configs = device_parser.get_webhook_device_configurations(xml_string)

    # Create devices
    webhook_devices = []
    for device_config in webhook_device_configs:
        webhook_devices.append(
            WebhookDevice(
                device_config.name,
                device_config.on_webhook_path,
                device_config.off_webhook_path,
                url_manager
            )
        )

    # Create device manager
    device_manager = DeviceManager(webhook_devices)

    device_manager.turn_on("Fairy lights")


if __name__ == "__main__":
    run()
