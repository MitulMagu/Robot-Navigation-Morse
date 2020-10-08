# Robot-Navigation-Morse

The simulation provides a convenient method to implement robot navigation in the Morse simulator using the PID controller. The ATRV robot can be provided 3D coordinates in the script and it will navigate to that location. The parameters such as kp, kd, ki, tolerance and linear speed can be modified directly. A custom environment has been provided.

## Usage

First, the package needs to be imported to Morse simulator and then it can be run directly using morse run.
```
morse import <path>
morse run Robot-Navigation-Morse
```
Once Morse is running, run the python script provided for navigation.

```
python3 navigation_pidcontrol.py
```
The variables such as kp, kd, ki, tolerance and linear speed can be set in navigation_pidcontrol.py.

## Dependencies

Requires Morse simulator which can be found here: https://github.com/morse-simulator/morse
Requires simple-pid to be installed: https://pypi.org/project/simple-pid/
