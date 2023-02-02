import os
import unittest

from devicemonitor.device.base import UnixTextDevice
from devicemonitor.model.base import PowerSupplyModel


class TestUnixTextDevice(unittest.TestCase):
    def setUp(self):
        # Create text file with contect: {"current": 1.0, "voltage": 10.0}
        with open('test.txt', 'w') as f:
            f.write('{"current": 1.0, "voltage": 10.0}')

        self.unix_device = UnixTextDevice('test.txt', 'random_device', model=PowerSupplyModel)

    def tearDown(self):
        # Remove text file
        os.remove('test.txt')

    def test_open(self):
        """
        Test open method
        Load file content into buffer
        Parse data into model
        """
        self.unix_device.open()
        self.assertEqual(self.unix_device.instance.output_current, 1.0)
        self.assertEqual(self.unix_device.instance.output_voltage, 10.0)
        self.assertEqual(self.unix_device.status, 'closed')
        self.assertEqual(self.unix_device.buffer, '{"current": 1.0, "voltage": 10.0}')
        self.assertEqual(self.unix_device.instance.show(), {'output_current': 1.0, 'output_voltage': 10.0})
        self.assertEqual(self.unix_device.get_data(), {'output_current': 1.0, 'output_voltage': 10.0})


if __name__ == '__main__':
    # If darwin or Linux, run the tests
    import sys
    if sys.platform == 'darwin' or sys.platform == 'linux':
        unittest.main()
