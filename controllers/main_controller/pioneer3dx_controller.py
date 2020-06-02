from controller import Robot
# from controllers.obstacle_avoidance.pioneer3dx import avoid_obstacles
from controllers.path_following.pioneer3dx_follow_mod import *
from controllers.utils.init_sensors import *
from controllers.utils.coordinate_utils import *


def check_next_checkpoint():
    #print("SONO DENTRO CHECK NEXT")
    checkpoint_result = TARGET_POINTS[current_target_index]
    if speed[0] == 0.0 and speed[1] == 0.0 and current_target_index == 0:
        updated_target = current_target_index + 1
        print("UPDATED TARGET " + str(updated_target))
        updated_target %= TARGET_POINTS_SIZE
        checkpoint_result = TARGET_POINTS[updated_target]
    return checkpoint_result


if __name__ == '__main__':
    # create the Robot instance.
    robot = Robot()

    leftMotor = robot.getMotor('left wheel')
    rightMotor = robot.getMotor('right wheel')

    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))

    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)

    current_target_index = 0
    checkpoint = TARGET_POINTS[current_target_index]

    # distance_sensors = init_distance_sensors(robot)

    gps = init_gps(robot)
    # compass = init_compass(robot)

    speed = [0.0, 0.0]

    #da buttare quando sistemiamo turn
    counter = 0

    new_checkpoint = TARGET_POINTS[0]


    while robot.step(TIME_STEP) != -1:
        # read gps position and compass values
        pos3D = gps.getValues()  # [x,y,z]
        #print("gps: " + str(pos3D))
        # north3D = compass.getValues()  # [x, NaN, z]  u = 1, v = 2
        # print("compass: " + str(north3D))

        # compute the 2D position of the robot and its orientation
        pos = [pos3D[0], pos3D[2]]
        # north = [north3D[0], north3D[2]]
        # front = [-north[0], north[1]]

        if current_target_index == 0:
            speed = run_forward(checkpoint, pos)
            new_checkpoint = check_next_checkpoint()
            print(new_checkpoint)

        if new_checkpoint != checkpoint:
            checkpoint = new_checkpoint
            [new_counter, speed] = turn(new_checkpoint, pos, counter)
            counter = new_counter

        leftMotor.setVelocity(speed[0])
        rightMotor.setVelocity(speed[1])
    # Enter here exit cleanup code.
