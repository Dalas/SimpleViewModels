

# Base class
class BaseField:
    value = None

    def __init__(self, value):
        self.value = value


    def get_value(self):
        return self.value