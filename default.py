#! /usr/bin/env morseexec

from morse.builder import *
import bpy
from random import randrange,randint
import random
from morse.sensors import *

robot = ATRV()

robot.translate(0.0, 0.0, 0.9)
robot.rotate(0.0, 0.0, 0.0)

motion = MotionVW()
robot.append(motion)

# Add a keyboard controller to move the robot with arrow keys.
# keyboard = Keyboard()
# robot.append(keyboard)
# keyboard.properties(ControlType = 'Position')

pose = Pose()
robot.append(pose)

waypoint = Waypoint()

waypoint.properties(ObstacleAvoidance=False)
waypoint.translate(x=0.2,y=0.0,z=0.9)
waypoint.rotate(0.0, 0.0, 0.0)
waypoint.add_interface('socket')

robot.append(waypoint)

laserscanner = Sick()

laserscanner.translate(x=0.2, y=0.0,z=0.6)
laserscanner.rotate(0.0, 0.0, 0.0)

robot.append(laserscanner)
laserscanner.add_interface('socket')
laserscanner.properties(visible_arc=True)
robot.add_default_interface('socket')

env = Environment('indoors-1/indoor-1', fastmode = False)

env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
