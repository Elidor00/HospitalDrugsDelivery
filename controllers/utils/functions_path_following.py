from math import sqrt, atan2, pi
from controllers.utils.const import *


# u = vector[0], v = vector[1]
# vector = [u,v]
def norm(vector: list) -> float:
	return sqrt(vector[0] * vector[0] + vector[1] * vector[1])


def normalize(vector: list) -> list:
	n = norm(vector)
	u = vector[0] / n
	v = vector[1] / n
	return [u, v]


def modulus_double(a: float, m: float) -> float:
	div_i = int(a / m)
	div_d = float(div_i)
	r = a - div_d * m
	if r < 0.0: 
		r += m
	return r

'''
def angle(vector1: list, vector2: list) -> float:
	print(vector2)
	print(vector1)
	return modulus_double(atan2(vector2[1], vector2[0]) - atan2(vector1[1], vector1[0]), 2.0 * pi)
'''


def minus(vector1: list, vector2: list) -> list:
	vector_res = [0.0, 0.0]
	vector_res[0] = vector1[0] - vector2[0]
	vector_res[1] = vector1[1] - vector2[1]
	return vector_res

# questo deve essere messo dentro un package
# path_following e si chiama
# pioneer3dx_qualcosa
# e rinominare pioneer3dx dentro obstacles avoidance
def run_forward(checkpoint_coord, distance):
	# comment avoid_obstacles for testing gps
	# state = avoid_obstacles(distance_sensors, leftMotor, rightMotor, state)

	# a target position has been reached
	if distance < DISTANCE_TOLERANCE:
		print("Checkpoint" + str(checkpoint_coord) + "raggiunto!")
		# current_target_index += 1
		# current_target_index %= TARGET_POINTS_SIZE
		return
	else:
		# move the robot to the next target
		speed[0] = MAX_SPEED
		speed[1] = MAX_SPEED

	robot.leftMotor.setVelocity(speed[0])
	robot.rightMotor.setVelocity(speed[1])


def turn_left():
	pass

def turn_right():
	pass