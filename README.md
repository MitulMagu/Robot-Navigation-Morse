# Robot-Navigation-Morse

The simulation provides a convenient method to implement robot navigation in the Morse simulator with obstacle avoidance using the P controller. The ATRV robot can be provided 3D coordinates in the script and it will navigate to that location with the help of a laser scanner. The parameters such as kp, tolerance and linear speed can be modified directly. A custom environment has been provided that can randomly generate obstacles.

## Usage

First, the package needs to be imported to Morse simulator and then it can be run directly using morse run.
```
morse import <path>
morse run Robot-Navigation-Morse
```
Once Morse is running, run the python script provided for navigation.

```
python3 navigation_pcontrol.py
```

## Dependencies

Requires Morse simulator which can be found here: https://github.com/morse-simulator/morse
