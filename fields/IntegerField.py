from .BaseField import BaseField


class IntegerField(BaseField):

    def __init__(self):
        super(IntegerField, self).__init__()

    def set_value(self, value):
        if type(value) != int:
            raise Exception('Value must be integer! Not {0}!'.format(type(value).__name__))