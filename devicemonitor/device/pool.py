import abc


class BaseEventPool(abc.ABC):
    @abc.abstractmethod
    def push(self, event_type=None, message=None):
        pass

    @abc.abstractmethod
    def pop(self, event_type=None):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass


class EventPool(BaseEventPool):
    def __init__(self, tag):
        self.tag = tag
        self.event = {}

    def push(self, event_type=None, message=None):
        if event_type is None:
            return
        if message is None:
            return
        if event_type not in self.event.keys():
            self.event[event_type] = [message]
        else:
            self.event[event_type].append(message)

    def pop(self, event_type=None):
        if event_type is None:
            return
        if event_type not in self.event.keys():
            return
        return self.event[event_type].pop()

    def has(self, event_type=None):
        if event_type is None:
            return False
        if event_type not in self.event.keys():
            return False
        if len(self.event[event_type]) == 0:
            return False
        return True

    def __str__(self):
        return str(self.tag)

    def __repr__(self):
        return str(self.tag)