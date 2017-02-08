from fields.BaseField import BaseField


class BaseModel:
    attributes = {}

    def __init__(self, **kwargs):
        self.set_attributes()
        self.check_attributes(**kwargs)

        self.__dict__.update(kwargs)

    def set_attributes(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, BaseField):
                self.attributes[attr_name] = attr

    def check_attributes(self, **kwargs):
        for attribute in kwargs.keys():
            if attribute not in self.attributes.keys():
                raise Exception('Attribute \'{0}\' not exists in current model!'.format(attribute))

            self.attributes[attribute].type_validation(kwargs[attribute])