import time

from controller import Robot
from controllers.utils.init_sensors import *
from controllers.utils.coordinate_utils import *


def set_forward_speed():
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)


def update_checkpoint(index):
    if index < TARGET_POINTS_SIZE - 1:
        return [index + 1, TARGET_POINTS[index + 1]]


def step_turn(checkpoint_coord):
    while robot.step(TIME_STEP) != -1:
        north3d = compass.getValues()  # [x, NaN, z]  u = 1, v = 2
        print("compass: " + str(north3d))
        # a target position has been reached
        #if north3d[0] < 0.005:
        beta_nord = atan2(north3d[0], north3d[2])
        beta_nord_degree = beta_nord / pi * 180
        print("beta nord in gradi durante il turn " + str(beta_nord_degree) + "\n")
        pos3d = gps.getValues()
        current_position = [pos3d[0], pos3d[2]]
        # TODO generalise for both axes
        print("checkpoint x = " + str(abs(checkpoint_coord[0])))
        print("my position x = " + str(abs(current_position[0])))
        print("checkpoint y = " + str(abs(checkpoint_coord[1])))
        print("my position y = " + str(abs(current_position[1])))
        if abs(beta_nord_degree) < abs(checkpoint_coord[0]) - abs(current_position[0]) or \
                abs(beta_nord_degree) < abs(checkpoint_coord[1]) - abs(current_position[1]):
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            time.sleep(5)
            return


def step(checkpoint_coord):

    # allineamento rispetto alle coordinate del checkpoint da raggiungere
    # turn(checkpoint_coord)

    while robot.step(TIME_STEP) != -1:

        print("velocita sx: " + str(leftMotor.getVelocity()))
        print("velocita dx: " + str(rightMotor.getVelocity()))

        # read gps position and compass values
        pos3d = gps.getValues()  # [x,y,z]
        pos = [pos3d[0], pos3d[2]]  # robot's coordinate x and z
        north3d = compass.getValues()  # [x, NaN, z]  u = 0, v = 2
        north = [north3d[0], north3d[2]]
        # front = [-north[0], north[2]]

        # compute the 2D position of the robot and its orientation
        direction = minus(checkpoint_coord, pos)
        distance = norm(direction)

        # direction = normalize(direction)
        # beta = angle(front, direction) - pi
        # beta_nord = atan2(north[0], north[2])
        # beta_nord_degree = beta_nord / pi * 180
        # beta_direction = atan2(direction[0], direction[1])
        # beta_direction_degree = beta_direction / pi * 180

        # change axis coordinate TODO: minus or plus?
        new_checkpoint_coord = minus(checkpoint_coord, pos)
        print("New checkpoint Coord: " + str(new_checkpoint_coord))

        # calculate angle between robot position and checkpoint
        checkpoint_angle = polar_angle(new_checkpoint_coord)
        print("Checkpoint Angle: " + str(checkpoint_angle))
        north_angle = polar_angle(north)
        print("North Angle: " + str(north_angle))

        # angle between robot and checkpoint
        angle = checkpoint_angle + north_angle
        print("Angle Value " + str(angle))
        # go forward
        if 0.5 > angle > -0.5:
            # ruoto antiorario
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(MAX_SPEED)
        # turn left
        elif angle <= -0.01:
            # ruoto orario
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(MAX_SPEED)
        # turn right
        else:
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(0.0)


        # a target position has been reached
        if distance <= DISTANCE_TOLERANCE:
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            print("FINE CHECKPOINT")
            time.sleep(5)
            return


def turn(checkpoint_coord):
    pos3d = gps.getValues()
    current_position = [pos3d[0], pos3d[2]]
    # TODO generalise for both axes
    print("checkpoint x = " + str(abs(checkpoint_coord[0])))
    print("my position x = " + str(abs(current_position[0])))
    if abs(checkpoint_coord[0]) >= abs(current_position[0]):
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(MAX_SPEED)


if __name__ == '__main__':
    # create the Robot instance.
    robot = Robot()

    leftMotor = robot.getMotor('left wheel')
    rightMotor = robot.getMotor('right wheel')

    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))

    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)

    gps = init_gps(robot)
    compass = init_compass(robot)

    speed = [0.0, 0.0]

    current_target_index = 0
    checkpoint = TARGET_POINTS[current_target_index]

    step(checkpoint)
    [current_target_index, checkpoint] = update_checkpoint(current_target_index)
    print(checkpoint)
    # turn(checkpoint)
    # step_turn(checkpoint)

    step(checkpoint)
    [current_target_index, checkpoint] = update_checkpoint(current_target_index)
    print(checkpoint)
    # turn(checkpoint)
    # step_turn(checkpoint)
