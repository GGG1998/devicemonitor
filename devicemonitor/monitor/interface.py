import abc


class IMonitor(abc.ABC):
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError("start() method is not implemented")

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError("stop() method is not implemented")

    @abc.abstractmethod
    def get_statuses(self):
        raise NotImplementedError("get_statuses() method is not implemented")