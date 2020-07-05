from pymorse import Morse
import math
flag = 2

x1 = -12
y1 = 6
z1 = 0

kp = 0.2
tolerance = 0.5
rotation_offset = 5.5
obstacle_dist = 2
linear_speed = 1.5

# print(math.atan2(0,-12))
with Morse() as morse:
	pose = morse.rpc('robot.pose','get_local_data')
	# print(pose['x'])
	while ((pose['x']>(x1+tolerance)) or (pose['x']<(x1-tolerance)) or (pose['y']>(y1+tolerance)) or (pose['y']<(y1-tolerance))):
		pose = morse.rpc('robot.pose','get_local_data')
		sensor_data = morse.rpc('robot.laserscanner','get_local_data')
		print("Robot coordinates:",pose['x'],pose['y'])
		print("Yaw (actual vs. required):",pose['yaw'],math.atan2(y1-pose['y'],x1-pose['x']))
		# print(pose['yaw'])
		morse.rpc('robot.motion','set_speed',linear_speed,rotation_offset*kp*(pose['yaw']-math.atan2(y1-pose['y'],x1-pose['x'])))
		for i in range(85,95):
			if (sensor_data['range_list'][i] < obstacle_dist):
				while(sensor_data['range_list'][i] < obstacle_dist+1):
					sensor_data = morse.rpc('robot.laserscanner','get_local_data')
					if(i<90):
						morse.rpc('robot.motion','set_speed',kp*-5,kp*7)
					else:
						morse.rpc('robot.motion','set_speed',kp*-5,kp*-7)
	print("I have arrived!")
	morse.rpc('robot.motion','set_speed',0,0)
