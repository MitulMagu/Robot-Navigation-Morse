#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <Robot-Navigation-Morse> environment

Feel free to edit this template as you like!
"""

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
