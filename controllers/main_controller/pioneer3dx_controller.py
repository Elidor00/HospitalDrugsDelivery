from controller import Robot
from controllers.obstacle_avoidance.pioneer3dx import avoid_obstacles
from controllers.utils.init_sensors import *

if __name__ == '__main__':
	# create the Robot instance.
	robot = Robot()

	leftMotor = robot.getMotor('left wheel')
	rightMotor = robot.getMotor('right wheel')

	leftMotor.setPosition(float('inf'))
	rightMotor.setPosition(float('inf'))

	leftMotor.setVelocity(0.0)
	rightMotor.setVelocity(0.0)

	distance_sensors = init_distance_sensors(robot)

	state = FORWARD

	gps = init_gps(robot)

	while robot.step(TIME_STEP) != -1:
		state = avoid_obstacles(distance_sensors, leftMotor, rightMotor, state)
		print(gps.getValues())  # [x,y,z]

	# Enter here exit cleanup code.

