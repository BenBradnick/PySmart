import requests
from pysmart.framework.httpstatuscodes import StatusCodes


class WebhookSender:

    def __init__(self):
        pass

    @staticmethod
    def send(url, data):
        try:
            response = requests.post(url, data=data)
            return response.status_code
        except Exception:
            return StatusCodes.CONNECTION_ERROR
