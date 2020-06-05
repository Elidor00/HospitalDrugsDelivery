from controller import Robot
from controllers.path_following.pioneer3dx_follow_mod import move_to
from controllers.utils.const import TARGET_POINTS
from controllers.utils.init_sensors import init_gps, init_compass


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

    for checkpoint in TARGET_POINTS:
        move_to(robot, gps, compass, leftMotor, rightMotor, checkpoint)
