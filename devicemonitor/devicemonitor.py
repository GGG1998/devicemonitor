import threading
import time

from devicemonitor.device.base import BaseDevice
from devicemonitor.device.observable import DeviceObservable
from devicemonitor.device.pool import EventPool
from devicemonitor.monitor.interface import IMonitor


class DeviceMonitor(IMonitor):
    _thread = None
    _data = None

    def __init__(self, interval,
                 devices_observable=None,
                 global_type=None,
                 event_pool=EventPool("Device"),
                 logger=None):
        self._pool = event_pool
        self._interval = interval
        self._stop_event = threading.Event()
        self._devices = devices_observable
        self._global_type = global_type
        self._logger = logger

        if logger is None:
            import logging
            self._logger = logging.getLogger(__name__)
            self._logger.setLevel(logging.DEBUG)
            self._logger.addHandler(logging.StreamHandler())

        if devices_observable is None:
            self._devices = DeviceObservable(self._pool)

    def start(self):
        self._logger.info("Starting device monitor")
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def stop(self):
        self._logger.info("Stop device monitor")
        self._stop_event.set()
        self._thread.join()

    def get_statuses(self, _type=None):
        self._logger.info("Get statuses")
        which_type_device = _type if _type is not None else self._global_type
        # pop all statuses
        while self._pool.has(which_type_device):
            self._logger.debug(f'Pop status from pool: {which_type_device}')
            self._logger.info(self._pool.pop(which_type_device))

    def _run(self):
        self._logger.info("Run device monitor")
        while not self._stop_event.is_set():
            self._logger.debug("Running...")
            self._devices.open()
            time.sleep(self._interval)

    def register(self, device: BaseDevice):
        self._devices.register(device)

    def unregister(self, device: BaseDevice):
        self._devices.unregister(device)