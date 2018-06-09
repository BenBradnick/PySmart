import requests


class WebhookSender:

    def __init__(self):
        pass

    @staticmethod
    def send(url, data):
        response = requests.post(url, data=data)
        return response
