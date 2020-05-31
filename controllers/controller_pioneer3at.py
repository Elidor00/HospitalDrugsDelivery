# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# WorldInfo -> basicTimeStep
# il TIME_STEP deve essere multiplo di basicTimeStep
TIME_STEP = 64
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# lista vuota per i sensori di posizione
so = []
# nomi dei sensori di posizione
soNames = ['so0', 'so2', 'so2', 'so3', 'so4', 'so5', 'so6', 'so7']

# popoliamo ps con i valori
for i in range(8):
    so.append(robot.getDistanceSensor(soNames[i]))
    so[i].enable(TIME_STEP)  # TIME_STEP dovrebbe dire ogni quanto
    # aggiornare il valore dei sensori

leftMotor = robot.getMotor('left wheel')
rightMotor = robot.getMotor('right wheel')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    soValues = []
    for i in range(8):
        soValues.append(so[i].getValue())

    # Process sensor data here.
    # detect obstacles

    right_obstacles = soValues[0] > 80.0 or soValues[1] > 80.0 or soValues[2] > 80.0
    left_obstacles = soValues[5] > 80.0 or soValues[6] > 80.0 or soValues[7] > 80.0

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

    # initialize motor speeds
    # mi serve per settare la velocità delle ruote a seconda
    # se ci sia l'ostacolo a dx o sx
    leftSpeed = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    # se l'ostacolo è a sx, giro a dx e viceversa
    if left_obstacles:
        leftSpeed += 0.5 * MAX_SPEED
        rightSpeed -= 0.5 * MAX_SPEED
    elif right_obstacles:
        leftSpeed -= 0.5 * MAX_SPEED
        rightSpeed += 0.5 * MAX_SPEED
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)

# Enter here exit cleanup code.
