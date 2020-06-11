from math import pi

from controller import Robot
from controllers.hospital_map.graph import MAP_POINTS
from controllers.path_following.astar_alg import astar
from controllers.utils.const import *
from controllers.utils.coordinate_utils import minus, norm, polar_angle, rotate
from controllers.utils.init_sensors import init_gps, init_compass, init_motor, init_keyboard


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

    def create_path(self, start, end):
        self.path = astar(start, end)
        if self.path is None:
            raise Exception(f"Path from {start} to {end} does not exist")

    def step(self):
        while self.robot.step(TIME_STEP) != -1:
            self.check_keyboard()
            if self.mode == AUTOMATIC:
                if self.current_checkpoint < len(self.path):
                    checkpoint = self.path[self.current_checkpoint]
                    self.move_to(MAP_POINTS[checkpoint])
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

        self.left_motor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * angle)
        self.right_motor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * angle)

        self.check_arrived(distance)

    def check_arrived(self, distance):
        # a target position has been reached
        if distance <= DISTANCE_TOLERANCE:
            self.left_motor.setVelocity(0.0)
            self.right_motor.setVelocity(0.0)
            print("Checkpoint reached")
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
                print("GPS " + str(self.gps.getValues()))
            elif key == ord('E'):
                self.mode = MANUAL
            else:
                print("Key value not valid")

    def manual_control(self):
        self.set_velocity(0.0, 0.0)
        self.robot.step(1000)
        while self.robot.step(TIME_STEP) != -1:
            self.set_velocity(0.0, 0.0)  # TODO: si ferma un po' troppo bruscamente
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
                    print("Key value not valid")

    def set_velocity(self, left_speed=MAX_SPEED, right_speed=MAX_SPEED):
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)


if __name__ == '__main__':
    controller = Controller()

    controller.create_path("Warehouse", "EntryR4")
    controller.step()
