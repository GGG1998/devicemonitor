# Task Description
Design and implement with tests the DeviceMonitor library for monitoring various types of devices.

Device monitoring should consist in the ability to continuously read a list of parameters defined for a given type of device.
We assume that device parameters do not change quickly (once every few seconds) and there is no need to detect all changes of these parameters, but only to know the current state of the device.
of these parameters, but only to know the relatively current value of the parameters.
Possible parameter types are string, int, float, bool.
Each monitored device is to have an identifier associated with its parameters.

**Example 1**  
There is a given type of power supply for airport lamps that allows the current output current and output voltage to be read.
Assuming that there are three power supply units to be monitored and their identifiers are 1, 2, 3, DeviceMonitor should enable the following
retrieve the current and output voltage values from all power supplies in the form:
```
{
  '1': { 'output_current': 0.5, 'output_voltage': 450},
  '2': { 'output_current': 0.6, 'output_voltage': 449},
  '3': { 'output_current': 0.4, 'output_voltage': 451}
}
```

A sample implementation for the device to be simulated should also be provided via a text file (one file for one device).
The text file will contain the device parameters in JSON form along with its parameters, e.g:
```
{
  'voltage': 666,
  'current': 4
}
```

Changing the parameter values should be possible at runtime and reflected in the value returned by the get_statuses method.

1. The tool should provide the following api interface:
- start() method - starts DeviceMonitor in a separate thread
- stop() method - stops the DeviceMonitor thread
- get_statuses() method - returns a dictionary with the monitored devices (as in example 1)
2. the start, stop, get_statuses methods should be thread-safe, in particular the start and stop methods will be called from the main thread of the
 application using DeviceMonitor and the get_statuses method can be called from any other application thread.
3. the tool should allow new device types to be easily added. It is important that adding support for a new device type does not require changes to the code of the library itself.
4. it is required to provide a test script using the DeviceMonitor library along with a simulated device that will output the parameters of that device every second.
5. the code should be 100% covered by unit tests.