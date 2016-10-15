from fields.BaseField import BaseField


class BaseModel:
    def __init__(self, **kwargs):
        for attribute in self.get_attributes():
            if attribute not in kwargs:
                raise Exception('Attribute \'{0}\' not exists in current model!'.format(attribute))

            print(attribute)

    def get_attributes(self):
        return [attr for attr in dir(self) if isinstance(getattr(self, attr), BaseField)]