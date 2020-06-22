from controllers.utils.const import MAX_SENSOR_NUMBER, NAME_SENSOR, TIME_STEP, GPS, COMPASS


def init_distance_sensors(robot) -> list:
    # list for distance sensor (sonar sensor)
    distance_sensors = []

    # init distance sensor list with name and value
    for i in range(MAX_SENSOR_NUMBER):
        distance_sensors.append(robot.getDistanceSensor(NAME_SENSOR + str(i)))
        distance_sensors[i].enable(TIME_STEP)
    # time step for frequency of upgrading value
    return distance_sensors


def init_keyboard(robot):
    keyboard = robot.getKeyboard()
    keyboard.enable(TIME_STEP*64)
    return keyboard


def init_gps(robot):
    gps = robot.getGPS(GPS)
    gps.enable(TIME_STEP)
    return gps


def init_gps_back(robot):
    gps_back = robot.getGPS("gps_back")
    gps_back.enable(TIME_STEP)
    return gps_back


def init_compass(robot):
    compass = robot.getCompass(COMPASS)
    compass.enable(TIME_STEP)
    return compass


def init_kinect_range(robot):
    kinect = robot.getRangeFinder("kinect range")
    kinect.enable(TIME_STEP)
    camera = robot.getCamera("kinect color")
    camera.enable(TIME_STEP)
    return kinect, camera


def init_motor(robot, string):
    motor = robot.getMotor(string)
    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)
    return motor

