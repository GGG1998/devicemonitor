from devicemonitor.device.base import DictDevices, BaseDevice
from devicemonitor.device.pool import BaseEventPool


class DeviceObservable(object):
    def __init__(self, event_poller: BaseEventPool):
        self.pool = event_poller
        self.devices = DictDevices()

    def register(self, device: BaseDevice) -> int:
        return self.devices.add(device)

    def unregister(self, _type, _id):
        self.devices.remove(_type, _id)

    def open(self):
        for _id, device in self.devices:
            device.open()
            self.pool.push('open', 'Opened')
            self.get_statuses()

            # self.pool.push('open', e)

            device.close()
            self.pool.push('open', 'todo - read status from device')

    def get_statuses(self):
        status = {}
        for _id, device in self.devices:
            status[_id] = device.get_data()
        self.pool.push('devices', status)
