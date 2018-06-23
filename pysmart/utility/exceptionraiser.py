class ExceptionRaiser:

    @staticmethod
    def raise_value_error_if_none(attribute, argument):
        if argument is None:
            raise ValueError("{0} cannot be None".format(attribute))
