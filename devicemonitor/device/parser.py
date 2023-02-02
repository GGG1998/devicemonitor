import abc
import json

from typing import Dict, Union


class IParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, data: bytes) -> Dict[any, any]:
        raise NotImplementedError("parse() method is not implemented")


class JsonParser(IParser):
    def parse(self, data: Union[bytes, str]) -> Dict[any, any]:
        if data is None:
            return {}
        if isinstance(data, str):
            return json.loads(data)
        return json.loads(data.decode('utf-8'))
