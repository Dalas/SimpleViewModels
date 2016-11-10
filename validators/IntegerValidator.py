from .BaseValidator import BaseValidator


class IntegerValidator(BaseValidator):

    @staticmethod
    def min(min, value):
        return value < min