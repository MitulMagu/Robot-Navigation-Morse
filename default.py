#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <Robot-Navigation-Morse> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
import bpy
from random import randrange,randint
import random
from morse.sensors import *

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> trial' can help you to build custom robots.
robot = ATRV()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot.translate(0.0, 0.0, 0.9)
robot.rotate(0.0, 0.0, 0.0)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> trial' can help you with the creation of a custom
# actuator.
motion = MotionVW()
robot.append(motion)

# Add a keyboard controller to move the robot with arrow keys.
# keyboard = Keyboard()
# robot.append(keyboard)
# keyboard.properties(ControlType = 'Position')

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> trial' can help you with the creation of a custom
# sensor.
pose = Pose()
robot.append(pose)

# creates a new instance of the actuator
waypoint = Waypoint()

waypoint.properties(ObstacleAvoidance=False)
# place your component at the correct location
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
# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html
# the other available interfaces (like ROS, YARP...)
robot.add_default_interface('socket')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('../wall_obs.blend', fastmode = False)

env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])

# # Randomly spawn objects
cube = bpy.data.objects["Cube"]
cube01 = bpy.data.objects["Cube.001"]
cube02 = bpy.data.objects["Cube.002"]
cylinder02 = bpy.data.objects["Cylinder.002"]
plane02 = bpy.data.objects["Plane.002"]
plane05 = bpy.data.objects["Plane.005"]
cylinder01 = bpy.data.objects["Cylinder.002"]
cylinder03 = bpy.data.objects["Cylinder.003"]
cylinder = bpy.data.objects["Cylinder"]

frame_number = 0

# Cube
spawn_range = [(-15, -12),(-3, 0),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cube.location = (x,y,z)
cube.keyframe_insert(data_path="location",index=-1)

# Cube01
spawn_range = [(-6, 8),(-10, 0),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cube01.location = (x,y,z)
cube01.keyframe_insert(data_path="location",index=-1)

# Cylinder02
spawn_range = [(-12, -10),(-9, 8),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cylinder02.location = (x,y,z)
cylinder02.keyframe_insert(data_path="location",index=-1)

# Cylinder01
spawn_range = [(-12, 10),(-9, 8),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cylinder01.location = (x,y,z)
cylinder01.keyframe_insert(data_path="location",index=-1)

# Cylinder03
spawn_range = [(-12, 10),(-9, 8),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cylinder03.location = (x,y,z)
cylinder03.keyframe_insert(data_path="location",index=-1)

# Cylinder
spawn_range = [(-12, 10),(-9, 8),(0,1)]
x = random.randrange(spawn_range[0][0], spawn_range[0][1])
y = random.randrange(spawn_range[1][0], spawn_range[1][1])
z = (-0.2)
bpy.context.scene.frame_set(frame_number)
cylinder.location = (x,y,z)
cylinder.keyframe_insert(data_path="location",index=-1)

# frame_number += 2
