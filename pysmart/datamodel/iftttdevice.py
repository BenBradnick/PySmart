from pysmart.datamodel.device import Device
from pysmart.dataaccess.webhooksender import WebhookSender
from pysmart.framework.state import State
from pysmart.framework.httpstatuscodes import StatusCodes


class IFTTTDevice(Device):

    def __init__(self, name, on_webhook_path, off_webhook_path, url_manager):
        self.raise_value_error_if_none("on_webhook_path", on_webhook_path)
        self.raise_value_error_if_none("off_webhook_path", off_webhook_path)
        self.raise_value_error_if_none("url_manager", url_manager)

        super().__init__(name)

        self.on_webhook_path = on_webhook_path
        self.off_webhook_path = off_webhook_path
        self.url_manager = url_manager

    def turn_on(self):
        status = WebhookSender.send(
            self.url_manager.build_url(self.on_webhook_path), None)
        if status is StatusCodes.OK:
            self.state = State.ON

    def turn_off(self):
        status = WebhookSender.send(
            self.url_manager.build_url(self.off_webhook_path), None)
        if status is StatusCodes.OK:
            self.state = State.OFF

    @staticmethod
    def raise_value_error_if_none(attribute, argument):
        if argument is None:
            raise ValueError("{0} cannot be None".format(attribute))
