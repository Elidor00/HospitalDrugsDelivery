from controllers.utils.const import *


def init_distance_sensors(robot) -> list:
	# list for distance sensor (sonar sensor)
	distance_sensors = []

	# init distance sensor list with name and value
	for i in range(MAX_SENSOR_NUMBER):
		name_sensor = "so" + str(i)
		distance_sensors.append(robot.getDistanceSensor(name_sensor))
		distance_sensors[i].enable(TIME_STEP)
		# time step for frequency of upgrading value

	return distance_sensors


def init_gps(robot):

	name_gps = "gps"
	gps = robot.getGPS(name_gps)
	gps.enable(TIME_STEP)

	return gps
