import unittest
from pysmart.utility.exceptionraiser import ExceptionRaiser


class RaiseValueErrorIfNone(unittest.TestCase):

    def test_raises_ValueError_if_argument_is_None(self):
        attribute = "Attribute"
        argument = None

        self.assertRaises(ValueError, ExceptionRaiser.raise_value_error_if_none, attribute, argument)

    def test_does_not_raise_if_argument_is_not_None(self):
        attribute = "Attribute"
        argument = "Argument"

        try:
            ExceptionRaiser.raise_value_error_if_none(attribute, argument)
        except Exception as e:
            self.fail("No Exception expected. Got: {0}".format(e))
