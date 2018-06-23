from pysmart.utility.exceptionraiser import ExceptionRaiser


class XmlIFTTTDevice:

    def __init__(self, name, on_webhook_path, off_webhook_path):
        ExceptionRaiser.raise_value_error_if_none("on_webhook_path", on_webhook_path)
        ExceptionRaiser.raise_value_error_if_none("off_webhook_path", off_webhook_path)
        ExceptionRaiser.raise_value_error_if_none("name", name)

        self.name = name
        self.on_webhook_path = on_webhook_path
        self.off_webhook_path = off_webhook_path
