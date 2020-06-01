from controller import Robot
from controllers.utils.const import *
from controllers.obstacle_avoidance.pioneer3dx import avoid_obstacles
from controllers.utils.init_sensors import init_distance_sensors

if __name__ == '__main__':
	# create the Robot instance.
	robot = Robot()

	# get the time step of the current world.
	TIME_STEP = int(robot.getBasicTimeStep())

	leftMotor = robot.getMotor('left wheel')
	rightMotor = robot.getMotor('right wheel')

	leftMotor.setPosition(float('inf'))
	rightMotor.setPosition(float('inf'))

	leftMotor.setVelocity(0.0)
	rightMotor.setVelocity(0.0)

	distance_sensors = init_distance_sensors(robot)

	state = FORWARD

	while robot.step(TIME_STEP) != -1:
		state = avoid_obstacles(distance_sensors, leftMotor, rightMotor, state)

	# Enter here exit cleanup code.

