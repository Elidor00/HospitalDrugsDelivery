from controller import Robot
# from controllers.obstacle_avoidance.pioneer3dx import avoid_obstacles
from controllers.utils.init_sensors import *
from controllers.utils.functions_path_following import *

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
	compass = init_compass(robot)

	current_target_index = 0
	speed = [0.0, 0.0]

	checkpoint = TARGET_POINTS[current_target_index]

	while robot.step(TIME_STEP) != -1:

		# read gps position and compass values
		pos3D = gps.getValues()  # [x,y,z]
		print("gps: " + str(pos3D))
		north3D = compass.getValues()  # [x, NaN, z]  u = 1, v = 2
		print("compass: " + str(north3D))

		# compute the 2D position of the robot and its orientation
		pos = [pos3D[0], pos3D[2]]
		north = [north3D[0], north3D[2]]
		front = [-north[0], north[1]]

		# compute the direction and the distance to the target
		direction = minus(checkpoint, pos)
		distance = norm(direction)
		direction = normalize(direction)
		print("direction: " + str(direction))

		# compute the target angle
		# beta = angle(front, direction) - pi
		# beta = 0
		if qualcosa:

			run_forward(checkpoint, distance)
		elif:
			turn_left()
		else:
			turn_right()


	# Enter here exit cleanup code.

