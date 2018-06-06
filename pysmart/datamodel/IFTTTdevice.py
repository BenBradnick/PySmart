from pysmart.datamodel.device import Device


class IFTTTDevice(Device):

    def __init__(self, name, on_webhook, off_webhook):
        super().__init__(name)
        self.on_webhook = on_webhook
        self.off_webhook = off_webhook
