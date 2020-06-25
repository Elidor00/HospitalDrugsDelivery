from math import pi

import logging
import sys

from controller import Robot
from controllers.hospital_map.graph import MAP_POINTS
from controllers.main_controller.handler_planner import exec_plan
from controllers.path_following.astar_alg import astar
from controllers.utils.const import LOGGING_FILE, AUTOMATIC, TIME_STEP, MAX_SPEED, TURN_COEFFICIENT, DISTANCE_TOLERANCE, \
    DISTANCE_BRAKE, MIN_SPEED, MANUAL, PLANNING_FILE, LEFT_WHEEL, RIGHT_WHEEL
from controllers.utils.controller_utils import normalize_speed
from controllers.utils.coordinate_utils import minus, norm, polar_angle, rotate
from controllers.utils.init_sensors import init_gps, init_compass, init_motor, init_keyboard
from controllers.utils.txt_parser import parse


def setup_logger():
    # log info on pioneer3dx.log in write mode (without append)
    logging.basicConfig(filename=LOGGING_FILE,
                        filemode='w',
                        level=logging.INFO,
                        format='%(levelname)s: %(message)s')
    # and log also in stdout
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


class Controller:

    def __init__(self):
        self.robot = Robot()
        self.left_motor = init_motor(self.robot, LEFT_WHEEL)
        self.right_motor = init_motor(self.robot, RIGHT_WHEEL)
        self.keyboard = init_keyboard(self.robot)
        self.gps = init_gps(self.robot)
        self.compass = init_compass(self.robot)
        self.mode = AUTOMATIC
        self.path = []
        self.current_checkpoint = 0
        self.time = 0
        self.current_position = ""

    def create_path(self, start, end):
        self.path = astar(start, end)
        if self.path is None:
            raise Exception(f"Path from {start} to {end} does not exist")
        else:
            logging.info(f"Best path from {start} to {end} = {self.path}")

    def global_clock(self, counter):
        counter += 1
        if counter % (int(1000 / TIME_STEP)) == 0:  # about one second
            self.time += 1
            counter = 0
        return counter

    def step_with_time(self, stop):
        counter = 0
        while self.time < stop:
            self.robot.step(TIME_STEP)
            counter = self.global_clock(counter)

    def step(self):
        self.current_checkpoint = 0
        counter = 0
        while self.robot.step(TIME_STEP) != -1:
            counter = self.global_clock(counter)
            self.check_keyboard()
            if self.mode == AUTOMATIC:
                if self.current_checkpoint < len(self.path):
                    checkpoint = self.path[self.current_checkpoint]
                    self.move_to(MAP_POINTS[checkpoint])
                else:
                    point = self.path[self.current_checkpoint - 1]
                    if not (point == "Warehouse" or point == "SafePoint"):
                        logging.info(f"Drug deliver to {point} after {round(self.time / 60, 2)} min")
                    return
            else:
                self.manual_control()

    def move_to(self, checkpoint_coord):
        # read gps position and compass values
        pos3d = self.gps.getValues()  # [x,y,z]
        pos = [pos3d[0], pos3d[2]]  # robot's coordinate x and z
        north3d = self.compass.getValues()  # [x, NaN, z]  u = 0, v = 2
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

        left_speed = normalize_speed(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
        right_speed = normalize_speed(MAX_SPEED - pi - TURN_COEFFICIENT * angle)

        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)

        self.check_arrived(distance)

    def check_arrived(self, distance):
        # a target position has been reached
        if distance <= DISTANCE_TOLERANCE:
            self.left_motor.setVelocity(0.0)
            self.right_motor.setVelocity(0.0)
            logging.info(f"Checkpoint reached after {round(self.time / 60, 2)} min")
            self.current_checkpoint += 1
        elif distance <= DISTANCE_BRAKE:
            self.left_motor.setVelocity(MIN_SPEED)
            self.right_motor.setVelocity(MIN_SPEED)

    def check_keyboard(self):
        key = self.keyboard.getKey()
        if key <= 0:
            return
        else:
            if key == ord('P'):  # 80 is the ASCII for 'P'
                logging.info(f"GPS {str(self.gps.getValues())}")
            elif key == ord('E'):
                logging.info("Change to manual control")
                self.mode = MANUAL
            else:
                logging.info("Key value not valid")

    def manual_control(self):
        self.set_velocity(0.0, 0.0)
        self.robot.step(1000)
        while self.robot.step(TIME_STEP) != -1:
            self.set_velocity(0.0, 0.0)
            key = self.keyboard.getKey()
            if key <= 0:
                continue
            else:
                if key == ord('W'):
                    self.set_velocity()
                elif key == ord('A'):
                    self.set_velocity(left_speed=-MAX_SPEED)
                elif key == ord('D'):
                    self.set_velocity(right_speed=-MAX_SPEED)
                elif key == ord('S'):
                    self.set_velocity(-MAX_SPEED, -MAX_SPEED)
                else:
                    logging.info("Key value not valid")

    def set_velocity(self, left_speed=MAX_SPEED, right_speed=MAX_SPEED):
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)


if __name__ == '__main__':
    setup_logger()
    controller = Controller()
    # dict generated by parsing the output of platinum planner
    plan = parse(PLANNING_FILE)
    exec_plan(controller, plan)
