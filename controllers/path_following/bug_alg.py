from controller import RangeFinder, Robot
from controllers.utils.init_sensors import *
from math import atan2, sqrt
import time

from controllers.utils.const import TIME_STEP

CRUISING_SPEED = 7.5
TOLERANCE = -0.1
OBSTACLE_THRESHOLD = 0.5
SLOWDOWN_FACTOR = 0.5

FOLLOW_OBSTACLE = 1
GO_TO_TARGET = 2


def bug_algorithm(robot, left_motor, right_motor, back_gps, center_gps, kinect, camera, distance_sensors):

    kinect_width = int(kinect.getWidth())
    kinect_height = int(kinect.getHeight())

    half_width = int(kinect_width/2)  # CONTROLLA SE È IL CASO DI CASTARLI AD INT
    view_height = kinect_height/2 + 10

    view_height = int(view_height)
    print(view_height)

    max_range = kinect.getMaxRange()
    range_threshold = 0.7
    inv_max_range_times_width = 1.0/(max_range * kinect_width)

    target_x = -9.86
    target_z = -5.7

    left_obstacle = 0.0
    right_obstacle = 0.0

    left_speed = CRUISING_SPEED
    right_speed = CRUISING_SPEED

    mode = GO_TO_TARGET
    distance_value = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    min_distance_to_target = 0.0
    min_distance_x = 0.0
    min_distance_z = 0.0

    min_distance_time = 0

    while robot.step(TIME_STEP) != -1:
        for i in range(8):
            distance_value[i] = distance_sensors[i].getValue()
        # side_obstacle = distance_value[0] + distance_value[1] + distance_value[6] + distance_value[7]
        print(distance_value)

        kinect_values = kinect.getRangeImage()
        print("KINECT VALUE " + str(kinect_values))

        for i in range(half_width):
            value = RangeFinder.rangeImageGetDepth(kinect_values, kinect_width, i, view_height)
            if value < range_threshold:
                left_obstacle += value
                print("Left obstacle " + str(left_obstacle))

            value = RangeFinder.rangeImageGetDepth(kinect_values, kinect_width, kinect_width - i, view_height)
            if value < range_threshold:
                right_obstacle += value
                print("Right obstacle " + str(right_obstacle))

            print("VALUE " + str(value))

        obstacle = left_obstacle + right_obstacle
        print("CALCOLO OBSTACLE " + str(obstacle))
        point1 = back_gps.getValues()  # maybe cast to float?
        print("back gps " + str(point1))
        point2 = center_gps.getValues()
        print("center gps " + str(point2))

        target_angle = atan2(target_z - point1[2], target_x - point1[0])
        current_angle = atan2(point2[2] - point1[2], point2[0] - point1[0])

        # if reach the target, stop
        distance_to_target = sqrt(pow(target_z - point2[2], 2) + pow(target_x - point2[0], 2))
        print("distance to target " + str(distance_to_target))
        if distance_to_target < 0.6:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
            print("Target reached!!!")
            break

        if mode == FOLLOW_OBSTACLE:
            print("Follow obstacle")
            sqrt(pow(target_z-point2[2], 2) + pow(target_x - point2[0], 2))
            if min_distance_to_target > distance_to_target:
                min_distance_time = time.time()  # second from 1 jan 1970
                min_distance_to_target = distance_to_target
                min_distance_x = point2[0]
                min_distance_z = point2[2]
            elif sqrt(pow(min_distance_z - point2[2], 2) + pow(min_distance_x-point2[0], 2) < 0.01):
                current_time = time.time()
                if (current_time - min_distance_time) > 2.00:
                    mode = GO_TO_TARGET

            if obstacle > 3.0:
                # compute the relevant overall quantity of obstacle
                obstacle = 1.0 - obstacle * inv_max_range_times_width
                speed_factor = 0.0 if obstacle > OBSTACLE_THRESHOLD else SLOWDOWN_FACTOR
                left_speed = CRUISING_SPEED
                right_speed = speed_factor * CRUISING_SPEED
            elif distance_value[0] < 1.0:
                left_speed -= 1
                right_speed += 1
            else:
                left_speed = CRUISING_SPEED
                right_speed = CRUISING_SPEED
        
        elif GO_TO_TARGET:
            print("Go to target")
            print("Angle value " + str(abs(target_angle - current_angle)))
            if abs(target_angle - current_angle) > 0.3:
                if target_angle < current_angle:
                    left_speed -= 0.5
                    right_speed += 0.5
                else:
                    left_speed += 0.5
                    right_speed -= 0.5
            else:
                print("Cruising speed")
                left_speed = CRUISING_SPEED
                right_speed = CRUISING_SPEED

            print("obstacle " + str(obstacle))
            if obstacle > 5.0:
                print("SONO QUA")
                min_distance_time = time.time()
                print(min_distance_time)
                min_distance_x = point2[0]
                print(min_distance_x)
                min_distance_z = point2[2]
                print(min_distance_z)
                min_distance_to_target = distance_to_target
                mode = FOLLOW_OBSTACLE
                
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        print("Left obstacle " + str(left_obstacle) + " Right obstacle " + str(right_obstacle))
        print("Min distance " + str(min_distance_x) + " " + str(min_distance_z))
        
        # robot.step(TIME_STEP)
        left_obstacle = 0.0
        right_obstacle = 0.0

if __name__ == '__main__':
    robot = Robot()
    left_motor = init_motor(robot, LEFT_WHEEL)
    right_motor = init_motor(robot, RIGHT_WHEEL)
    keyboard = init_keyboard(robot)
    back_gps = init_gps_back(robot)
    center_gps = init_gps(robot)
    components_kinect = init_kinect_range(robot)  # 0 = kinect RangeFinder  1 = camera
    distance_sensors = init_distance_sensors(robot)

    bug_algorithm(robot, left_motor, right_motor, back_gps, center_gps, components_kinect[0], components_kinect[1], distance_sensors)
