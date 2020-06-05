import time

from controller import Robot
from controllers.utils.init_sensors import *
from controllers.utils.coordinate_utils import *


def update_checkpoint(index):
    if index < TARGET_POINTS_SIZE - 1:
        return [index + 1, TARGET_POINTS[index + 1]]


def step(checkpoint_coord):

    while robot.step(TIME_STEP) != -1:

        print("velocita sx: " + str(leftMotor.getVelocity()))
        print("velocita dx: " + str(rightMotor.getVelocity()))

        # read gps position and compass values
        pos3d = gps.getValues()  # [x,y,z]
        pos = [pos3d[0], pos3d[2]]  # robot's coordinate x and z
        north3d = compass.getValues()  # [x, NaN, z]  u = 0, v = 2
        north = [north3d[0], north3d[2]]

        # compute the 2D position of the robot and its orientation
        direction = minus(checkpoint_coord, pos)
        distance = norm(direction)

        new_checkpoint_coord = minus(checkpoint_coord, pos)
        print("New checkpoint Coord: " + str(new_checkpoint_coord))

        # calculate angle between robot position and checkpoint
        checkpoint_angle = polar_angle(new_checkpoint_coord)
        print("Checkpoint Angle: " + str(checkpoint_angle))
        # calculate angle between front of robot and north
        north_angle = polar_angle(north)
        print("North Angle: " + str(north_angle))

        if checkpoint_angle < 0 and north_angle < 0:
            # angle between robot and checkpoint
            angle = checkpoint_angle + north_angle + 360.0
        else:
            angle = checkpoint_angle + north_angle

        print("Angle Value " + str(angle))
        # go forward
        if 0.5 > angle > -0.5:
            leftMotor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
            rightMotor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * angle)
        # turn left
        elif angle <= -0.01:
            # rotate anticlockwise
            leftMotor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
            rightMotor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * angle)
        # turn right
        else:
            # rotate clockwise
            leftMotor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
            rightMotor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * angle)
        if check_arrived(distance):
            return


def check_arrived(distance):
    res = False
    # a target position has been reached
    if distance <= DISTANCE_TOLERANCE:
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(0.0)
        print("FINE CHECKPOINT")
        # time.sleep(5)
        res = True
    return res


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

    step(checkpoint)
    [current_target_index, checkpoint] = update_checkpoint(current_target_index)


    step(checkpoint)
    print(checkpoint)
    # turn(checkpoint)
    # step_turn(checkpoint)
