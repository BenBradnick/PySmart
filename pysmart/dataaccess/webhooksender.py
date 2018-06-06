import requests


class WebhookSender:

    def __init__(self):
        pass

    def send(self, hostname, path, data, protocol):
        url = self.build_url(hostname, path, protocol)
        response = requests.post(url, data=data)
        return response

    @staticmethod
    def build_url(hostname, path, protocol):
        return protocol.lower() + "://" + hostname + path
