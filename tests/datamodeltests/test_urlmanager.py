import unittest
from pysmart.datamodel.urlmanager import UrlManager


class CreatingUrlManager(unittest.TestCase):

    def test_new_UrlManager_hostname_cannot_be_None(self):
        hostname = None

        self.assertRaises(ValueError, UrlManager, hostname)

    def test_new_UrlManager_hostname_is_correctly_initialised(self):
        hostname = "google.co.uk"
        url_manager = UrlManager(hostname)

        self.assertEquals(hostname, url_manager.hostname)

    def test_new_UrlManager_protocol_cannot_be_None(self):
        protocol = None

        self.assertRaises(ValueError, UrlManager, protocol)

    def test_new_UrlManager_protocol_is_initialised_when_valid(self):
        protocol = "HTTPS"
        hostname = "google.co.uk"

        url_manager = UrlManager(hostname, protocol=protocol)

        self.assertEquals(protocol, url_manager.protocol)

    def test_new_UrlManager_raises_ValueError_for_invalid_protocol(self):
        protocol = "FTP"
        hostname = "google.co.uk"

        self.assertRaises(ValueError, UrlManager, hostname, protocol=protocol)


class UrlManagerRaisesExceptions(unittest.TestCase):

    def test_raise_ValueError_raises_ValueError_exception_when_argument_is_None(self):
        attribute = "Attribute"
        argument = None
        hostname = "google.co.uk"

        self.assertRaises(ValueError, UrlManager, attribute, argument)


class UrlManagerBuildsUrl(unittest.TestCase):

    def test_building_url_is_equal_to_expected_url_using_https(self):
        hostname = "google.co.uk"
        protocol = "HTTPS"
        url_manager = UrlManager(hostname, protocol)
        path = "info/extra"
        expected_url = "https://google.co.uk/info/extra"

        url = url_manager.build_url(path)

        self.assertEquals(expected_url, url)

    def test_building_url_is_equal_to_expected_url_using_http(self):
        hostname = "google.co.uk"
        protocol = "HTTP"
        url_manager = UrlManager(hostname, protocol)
        path = "info/extra"
        expected_url = "http://google.co.uk/info/extra"

        url = url_manager.build_url(path)

        self.assertEquals(expected_url, url)