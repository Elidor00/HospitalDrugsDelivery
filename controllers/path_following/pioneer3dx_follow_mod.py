from controllers.utils.const import TIME_STEP, TURN_COEFFICIENT, DISTANCE_TOLERANCE, MAX_SPEED, DISTANCE_BRAKE, \
    MIN_SPEED
from controllers.utils.coordinate_utils import *
from math import pi


def move_to(robot, gps, compass, left_motor, right_motor, checkpoint_coord, keyboard, check_keyboard):
    while robot.step(TIME_STEP) != -1:

        # check if enable manual controller for robot
        manual_control = check_keyboard(keyboard, gps)
        print(manual_control)
        if manual_control:
            return

        # read gps position and compass values
        pos3d = gps.getValues()  # [x,y,z]
        pos = [pos3d[0], pos3d[2]]  # robot's coordinate x and z
        north3d = compass.getValues()  # [x, NaN, z]  u = 0, v = 2
        north = [north3d[0], north3d[2]]

        # compute the 2D position of the robot and its orientation
        direction = minus(checkpoint_coord, pos)
        distance = norm(direction)

        new_checkpoint_coord = minus(checkpoint_coord, pos)
        # print("New checkpoint Coord: " + str(new_checkpoint_coord))

        # calculate angle between front of robot and north
        north_angle = polar_angle(north)
        # print("North Angle: " + str(north_angle))

        new_checkpoint_coord = rotate(north_angle, new_checkpoint_coord)

        # calculate angle between robot orientation and checkpoint
        angle = polar_angle(new_checkpoint_coord)
        # print("Angle Value " + str(angle))

        left_motor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
        right_motor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * angle)

        if check_arrived(left_motor, right_motor, distance):
            return


def check_arrived(left_motor, right_motor, distance):
    res = False
    # a target position has been reached
    if distance <= DISTANCE_TOLERANCE:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("Checkpoint reached")
        res = True
    elif distance <= DISTANCE_BRAKE:
        left_motor.setVelocity(MIN_SPEED)
        right_motor.setVelocity(MIN_SPEED)
    return res
