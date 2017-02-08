from .BaseField import BaseField
from validators import IntegerValidator


class IntegerField(BaseField):

    def __init__(self, **kwargs):
        super(IntegerField, self).__init__()

        self.rules = kwargs

    def type_validation(self, value):
        if type(value) != int:
            raise Exception('Value must be integer! Not {0}!'.format(type(value).__name__))

    def validate(self):
        for rule, value in self.rules:
            IntegerValidator.__call__(rule, value)