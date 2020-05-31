# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LED, Motor

MAX_SENSOR_NUMBER = 16
MAX_SPEED = 5.24
MAX_SENSOR_VALUE = 1024
MIN_DISTANCE = 1.0
WHEEL_WEIGHT_THRESHOLD = 200

sensors = [ 
    (150, 0), (200, 0), (300, 0), (600, 0),
    (0, 600), (0, 300),  (0, 200),  (0, 150),
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
distance_sensor_names = []

FORWARD = 0
LEFT = 1
RIGHT = 2
state = FORWARD

#inizializzo la lista di posizione con i loro nomi
for i in range(MAX_SENSOR_NUMBER):
    name_sensor = "so"
    distance_sensor_names.append(name_sensor + str(i))

print(*distance_sensor_names)
# inizializzo distance_sensors con i sensori
for i in range(16):
    distance_sensors.append(robot.getDistanceSensor(distance_sensor_names[i]))
    distance_sensors[i].enable(TIME_STEP)  # TIME_STEP dovrebbe dire ogni quanto
    # aggiornare il valore dei sensori

print(*distance_sensors)

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

left_speed = 0.0
right_speed = 0.0

leftMotor.setVelocity(left_speed)
rightMotor.setVelocity(right_speed)

wheel_weight_total = [0.0, 0.0]

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    left_speed = 0
    right_speed = 0
    wheel_weight_total = [0.0, 0.0]

    speed_modifier = 0.0
    for i in range(16):
        sensor_value = distance_sensors[i].getValue()

        if sensor_value == 0.0:
            speed_modifier = 0.0
        else:
            distance = 5.0 * (1.0 - (sensor_value / MAX_SENSOR_VALUE))
            if distance < MIN_DISTANCE:
                speed_modifier = 1 - (distance / MIN_DISTANCE)
                #print("Speed_modifier MODIFICATO " + str(speed_modifier))
            else:
                speed_modifier = 0.0
        for j in range(2):
            #print("Speed_modifier IN FOR " + str(speed_modifier))
            wheel_weight_total[j] += sensors[i][j] * speed_modifier

    # 1 = sx, 0 = dx
    if state == FORWARD:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD:
            right_speed = 0.7 * MAX_SPEED
            left_speed = -0.7 * MAX_SPEED
            state = LEFT
        elif wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            right_speed = -0.7 * MAX_SPEED
            left_speed = 0.7 * MAX_SPEED
            state = RIGHT
        else:
            right_speed = MAX_SPEED
            left_speed = MAX_SPEED
    elif state == LEFT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            right_speed = 0.7 * MAX_SPEED
            left_speed = -0.7 * MAX_SPEED
        else:
            right_speed = MAX_SPEED
            left_speed = MAX_SPEED
            state = FORWARD
    elif state == RIGHT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            right_speed = -0.7 * MAX_SPEED
            left_speed = 0.7 * MAX_SPEED
        else:
            right_speed = MAX_SPEED
            left_speed = MAX_SPEED
            state = FORWARD


    '''        
    print(*distance_sensor_values)
    # Process sensor data here.
    # detect obstacles

    right_obstacles = distance_sensor_values[5] > 50.0 \
                      or distance_sensor_values[6] > 50.0 or distance_sensor_values[7] > 50.0
    left_obstacles = distance_sensor_values[0] > 50.0 or distance_sensor_values[1] > 50.0 \
                     or distance_sensor_values[2] > 50.0

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

    # initialize motor speeds
    # mi serve per settare la velocità delle ruote a seconda
    # se ci sia l'ostacolo a dx o sx
    leftSpeed = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    # se l'ostacolo è a sx, giro a dx e viceversa
    if left_obstacles:
        leftSpeed += 0.8 * MAX_SPEED
        rightSpeed -= 0.8 * MAX_SPEED
    elif right_obstacles:
        leftSpeed -= 0.8 * MAX_SPEED
        rightSpeed += 0.8 * MAX_SPEED
    '''
    leftMotor.setVelocity(left_speed)
    rightMotor.setVelocity(right_speed)

# Enter here exit cleanup code.
