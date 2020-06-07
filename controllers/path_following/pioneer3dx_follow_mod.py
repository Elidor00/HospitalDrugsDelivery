from controllers.utils.const import *
from controllers.utils.coordinate_utils import *


def move_to(robot, gps, compass, left_motor, right_motor, checkpoint_coord):
    while robot.step(TIME_STEP) != -1:

        # print("velocita sx: " + str(left_motor.getVelocity()))
        # print("velocita dx: " + str(right_motor.getVelocity()))

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
        print("North Angle: " + str(north_angle))

        new_checkpoint_coord = rotate(north_angle, new_checkpoint_coord)

        # calculate angle between robot position and checkpoint
        checkpoint_angle = polar_angle(new_checkpoint_coord)
        print("Checkpoint Angle: " + str(checkpoint_angle))

        #angle = checkpoint_angle + north_angle
        angle = checkpoint_angle


        '''
        if checkpoint_angle < 0 and north_angle < 0:
            # angle between robot and checkpoint
            angle = checkpoint_angle + north_angle + 360.0
        else:
            angle = checkpoint_angle + north_angle
        '''
        print("Angle Value " + str(angle))

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
        print("FINE CHECKPOINT")
        res = True
    return res
