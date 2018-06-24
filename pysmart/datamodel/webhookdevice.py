from pysmart.datamodel.device import Device
from pysmart.dataaccess.webhooksender import WebhookSender
from pysmart.framework.devicestate import DeviceState
from pysmart.framework.httpstatuscodes import StatusCodes
from pysmart.utility.exceptionraiser import ExceptionRaiser


class WebhookDevice(Device):

    def __init__(self, name, on_webhook_path, off_webhook_path, url_manager):
        ExceptionRaiser.raise_value_error_if_none("on_webhook_path", on_webhook_path)
        ExceptionRaiser.raise_value_error_if_none("off_webhook_path", off_webhook_path)
        ExceptionRaiser.raise_value_error_if_none("url_manager", url_manager)

        super().__init__(name)

        self.on_webhook_path = on_webhook_path
        self.off_webhook_path = off_webhook_path
        self.url_manager = url_manager

    def turn_on(self):
        status = WebhookSender.send(
            self.url_manager.build_url(self.on_webhook_path), None)
        if status is StatusCodes.OK:
            self.logger.info("{0} switched on".format(self.name))
            self.state = DeviceState.ON
        else:
            self.logger.error("{0} webhook request failed ({1})".format(
                self.name, status))

    def turn_off(self):
        status = WebhookSender.send(
            self.url_manager.build_url(self.off_webhook_path), None)
        if status is StatusCodes.OK:
            self.logger.info("{0} switched off".format(self.name))
            self.state = DeviceState.OFF
        else:
            self.logger.error("{0} webhook request failed ({1})".format(
                self.name, status))
