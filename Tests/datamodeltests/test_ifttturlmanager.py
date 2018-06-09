import unittest
from pysmart.datamodel.ifttturlmanager import IFTTTUrlManager


class CreateIFTTTUrlManager(unittest.TestCase):

    def test_hostname_is_maker_ifttt_dot_com(self):
        api_key = "API_KEY"
        ifttt_url_manager = IFTTTUrlManager(api_key)

        self.assertEquals("maker.ifttt.com", ifttt_url_manager.hostname)

    def test_protocol_is_https(self):
        api_key = "API_KEY"
        ifttt_url_manager = IFTTTUrlManager(api_key)

        self.assertEquals("HTTPS", ifttt_url_manager.protocol)

    def test_ValueError_is_raised_when_api_key_is_none(self):
        api_key = None

        self.assertRaises(ValueError, IFTTTUrlManager, api_key)


class UsingIFTTTBuildUrl(unittest.TestCase):

    def test_actual_url_built_matches_expected_url(self):
        api_key = "API_KEY"
        path = "fairy_lights_on"
        expected_url = "https://maker.ifttt.com/trigger/fairy_lights_on/with/key/API_KEY"
        ifttt_url_manager = IFTTTUrlManager(api_key)

        url = ifttt_url_manager.build_url(path)

        self.assertEquals(expected_url, url)