# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

MAX_SENSOR_NUMBER = 16
MAX_SPEED = 5.24
MAX_SENSOR_VALUE = 1024
MIN_DISTANCE = 1.0
WHEEL_WEIGHT_THRESHOLD = 100

FORWARD = 0
LEFT = 1
RIGHT = 2
state = FORWARD

sensors = [
    (150, 0),  (200, 0),  (300, 0),  (600, 0),
    (0, 600),  (0, 300),  (0, 200),  (0, 150),
    (0, 0),    (0, 0),    (0, 0),    (0, 0),
    (0, 0),    (0, 0),    (0, 0),    (0, 0)
]

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
TIME_STEP = int(robot.getBasicTimeStep())

leftMotor = robot.getMotor('left wheel')
rightMotor = robot.getMotor('right wheel')

# lista vuota per i sensori di posizione
distance_sensors = []

#inizializzo la lista di posizione con i loro nomi
for i in range(MAX_SENSOR_NUMBER):
    name_sensor = "so" + str(i)
    distance_sensors.append(robot.getDistanceSensor(name_sensor))
    distance_sensors[i].enable(TIME_STEP)  # TIME_STEP dovrebbe dire ogni quanto
    # aggiornare il valore dei sensori

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

speed = [0.0, 0.0]

# speed[1] = motore sx
# speed[0] = motore dx
leftMotor.setVelocity(speed[0])
rightMotor.setVelocity(speed[1])

wheel_weight_total = [0.0, 0.0]

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    speed = [0.0, 0.0]
    wheel_weight_total = [0.0, 0.0]

    for i in range(16):
        sensor_value = distance_sensors[i].getValue()

        if sensor_value == 0.0:
            speed_modifier = 0.0
        else:
            distance = 5.0 * (1.0 - (sensor_value / MAX_SENSOR_VALUE))
            if distance < MIN_DISTANCE:
                speed_modifier = 1 - (distance / MIN_DISTANCE)
            else:
                speed_modifier = 0.0
        for j in range(2):
            wheel_weight_total[j] += sensors[i][j] * speed_modifier

    # 1 = sx, 0 = dx
    if state == FORWARD:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = 0.7 * MAX_SPEED
            speed[1] = -0.7 * MAX_SPEED
            state = LEFT
        elif wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = -0.7 * MAX_SPEED
            speed[1] = 0.7 * MAX_SPEED
            state = RIGHT
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
    elif state == LEFT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = 0.7 * MAX_SPEED
            speed[1] = -0.7 * MAX_SPEED
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
            state = FORWARD
    elif state == RIGHT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = -0.7 * MAX_SPEED
            speed[1] = 0.7 * MAX_SPEED
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
            state = FORWARD

    leftMotor.setVelocity(speed[0])
    rightMotor.setVelocity(speed[1])

# Enter here exit cleanup code.
