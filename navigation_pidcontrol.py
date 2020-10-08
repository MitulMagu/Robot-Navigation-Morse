from pymorse import Morse
from simple_pid import PID
import math

# Coordinates
x1 = -12
y1 = 5
z1 = 0

# Tune values here
kp = 0.7
ki = 0.01
kd = 0.45

tolerance = 0.5
rotation_offset = 5.5
obstacle_dist = 2
linear_speed = 1.5

# pid = PID(kp, kd, ki, setpoint=1)

# print(math.atan2(0,-12))
with Morse() as morse:
	pose = morse.rpc('robot.pose','get_local_data')
	v = pose['yaw']
	while ((pose['x']>(x1+tolerance)) or (pose['x']<(x1-tolerance)) or (pose['y']>(y1+tolerance)) or (pose['y']<(y1-tolerance))):
		pose = morse.rpc('robot.pose','get_local_data')
		sensor_data = morse.rpc('robot.laserscanner','get_local_data')
		print("Robot coordinates:",pose['x'],pose['y'])
		print("Yaw (actual vs. required):",pose['yaw'],math.atan2(y1-pose['y'],x1-pose['x']))
		des_yaw = math.atan2(y1-pose['y'],x1-pose['x'])
		# pid.setpoint(des_yaw)
		pid = PID(kp, ki, kd, setpoint=des_yaw)
		control = pid(v)
		v = pose['yaw']
		morse.rpc('robot.motion','set_speed',linear_speed,control)
		for i in range(85,95):
			if (sensor_data['range_list'][i] < obstacle_dist):
				while(sensor_data['range_list'][i] < obstacle_dist+1):
					sensor_data = morse.rpc('robot.laserscanner','get_local_data')
					if(i<90):
						morse.rpc('robot.motion','set_speed',-1,1.5)
					else:
						morse.rpc('robot.motion','set_speed',-1,1.5)
	print("I have arrived!")
	morse.rpc('robot.motion','set_speed',0,0)
