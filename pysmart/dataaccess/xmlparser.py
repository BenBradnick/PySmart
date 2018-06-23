from xml.etree import ElementTree
import logging


class XmlParser:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def get_root(xml_string):
        try:
            return ElementTree.fromstring(xml_string)
        except ElementTree.ParseError:
            raise ValueError("Could not find root")

    @staticmethod
    def get_child_tag_text(parent, name):
        tag = parent.find(name)
        try:
            return tag.text
        except Exception as e:
            raise ValueError("Could not find text for required tag: {0} ({1})".format(
                name, e
            ))
