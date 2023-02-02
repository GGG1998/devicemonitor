import abc
from typing import Dict, Tuple

from devicemonitor.device.parser import JsonParser


class BaseDevice(abc.ABC):
    buffer = None
    status = None
    instance = None
    fd = None

    def __init__(self, path: str, _type: str, model=None, parser=JsonParser):
        self.path = path
        self.type = _type

        if model is None:
            raise ValueError("model is not defined")

        self._model = model
        print("model: ", self._model)
        self._parser = parser()

    def open(self):
        self.status = "opened"
        self._open()
        self.close()

        parsed = self._parser.parse(self.buffer)
        self.instance = self._model(parsed)

    @abc.abstractmethod
    def _open(self) -> None:
        raise NotImplementedError("open() method is not implemented")

    @abc.abstractmethod
    def _close(self) -> None:
        raise NotImplementedError("close() method is not implemented")

    def close(self) -> None:
        self.status = "closed"
        if self.fd is not None:
            self._close()

    def get_data(self) -> Dict[any, any]:
        if self.instance is None:
            return {}
        return self.instance.show()

    def __str__(self) -> str:
        return str(self.path)


class UnixTextDevice(BaseDevice):
    def _open(self) -> None:
        self.fd = open(self.path, 'r')
        self.buffer = self.fd.read()

    def _close(self) -> None:
        self.fd.close()


class DictDevices(object):
    def __init__(self):
        self.devices = {}

    def add(self, device: BaseDevice) -> int:
        _type = device.type
        if self._count(_type) == 0:
            self.devices[_type] = {self._count(_type): device}
        else:
            self.devices[_type].update({self._count(_type): device})
        return self._count(_type)

    def remove(self, _type, _id) -> int:
        self.devices[type].remove(self.devices[type][_id])
        return len(self.devices[type])

    def _count(self, _type) -> int:
        if _type not in self.devices.keys():
            return 0
        return len(self.devices[_type])

    def __getitem__(self, _type):
        if _type not in self.devices.keys():
            return {}
        return self.devices[_type]

    def __iter__(self) -> Tuple[int, BaseDevice]:
        for _type in self.devices.keys():
            for _id in self.devices[_type].keys():
                yield _id, self.devices[_type][_id]
