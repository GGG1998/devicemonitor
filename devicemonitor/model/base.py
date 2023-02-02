from abc import ABC, abstractmethod
from typing import Union

from devicemonitor.model.input import FloatInput, IntegerInput, BooleanInput, StringInput


class BaseModel(ABC):
    def __init__(self, _json):
        self._data = _json
        _schema = self.__class__.__dict__
        _fields = _schema.keys()
        for field in _fields:
            serialized = self._serialize(_schema[field])
            if serialized is not None:
                setattr(self, field, serialized)

    def _serialize(self, field) -> Union[float, int, bool, str]:
        # List of fields from Model and constrain by FloatInput, IntegerInput, BooleanInput, StringInput
        if isinstance(field, FloatInput) or \
                isinstance(field, IntegerInput) or \
                isinstance(field, BooleanInput) or \
                isinstance(field, StringInput):
            return field.type(self._data[field.field_name])

    @abstractmethod
    def show(self):
        raise NotImplementedError("show method is not implemented")


class PowerSupplyModel(BaseModel):
    # Map json field to Input object
    output_current = FloatInput(field_name="current")
    output_voltage = FloatInput(field_name="voltage")

    def show(self):
        return {
            "output_current": self.output_current,
            "output_voltage": self.output_voltage
        }

