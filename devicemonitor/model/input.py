from types import MethodType


class Input(object):
    def __init__(self, field_name=None):
        self.field_name = field_name
        self.type = None

    def __str__(self):
        return str(self.field_name)

    def __repr__(self):
        return str(self.field_name)


class FloatInput(Input):
    def __init__(self, field_name=None):
        super().__init__(field_name=field_name)
        self.type = float


class IntegerInput(Input):
    def __init__(self, field_name=None):
        super().__init__(field_name=field_name)
        self.type = int


class BooleanInput(Input):
    def __init__(self, field_name=None):
        super().__init__(field_name=field_name)
        self.type = bool


class StringInput(Input):
    def __init__(self, field_name=None):
        super().__init__(field_name=field_name)
        self.type = str

