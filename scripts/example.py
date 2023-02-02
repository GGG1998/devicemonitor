import time

from devicemonitor.device.base import UnixTextDevice
from devicemonitor.devicemonitor import DeviceMonitor
from devicemonitor.model.base import PowerSupplyModel


def main():
    dm = DeviceMonitor(1)
    dm.register(UnixTextDevice("./pseudodevice/pseudodevice1", "random_device", model=PowerSupplyModel))
    dm.register(UnixTextDevice("./pseudodevice/pseudodevice2", "random_device", model=PowerSupplyModel))

    dm.start()
    while True:
        dm.get_statuses(_type="devices")
        time.sleep(2)


if __name__ == '__main__':
    main()