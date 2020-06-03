import time

from controller import Robot
# from controllers.obstacle_avoidance.pioneer3dx import avoid_obstacles
from controllers.path_following.pioneer3dx_follow_mod import *
from controllers.utils.init_sensors import *
from controllers.utils.coordinate_utils import *


def set_forward_speed():
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)


def update_checkpoint(index):
    if index < TARGET_POINTS_SIZE - 1:
        return [index + 1, TARGET_POINTS[index + 1]]


def step_turn():
    while robot.step(TIME_STEP) != -1:
        north3d = compass.getValues()  # [x, NaN, z]  u = 1, v = 2
        print("compass: " + str(north3d))
        # a target position has been reached
        if north3d[0] < 0.005:
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            time.sleep(1)
            return


def step(checkpoint_coord):
    while robot.step(TIME_STEP) != -1:
        # read gps position and compass values
        pos3d = gps.getValues()  # [x,y,z]
        # print("gps: " + str(pos3D))
        pos = [pos3d[0], pos3d[2]]
        north = compass.getValues()  # [x, NaN, z]  u = 0, v = 2
        #print("NORTH " + north)
        front = [-north[0], north[2]]
        # print("compass: " + str(north3D))

        # compute the 2D position of the robot and its orientation

        direction = minus(checkpoint_coord, pos)
        #print("DIRECTION " + str(direction))
        distance = norm(direction)
        direction = normalize(direction)
        #print("FRONT " + str(front))
        #print("DIRECTION " + str(direction))
        beta = angle(front, direction) - pi
        print("beta in gradi " + str(beta / pi * 180))

        beta_nord = atan2(north[0], north[2])
        beta_nord_degree = beta_nord / pi * 180
        print("beta nord in gradi " + str(beta_nord_degree))

        beta_direction = atan2(direction[0], direction[1])
        beta_direction_degree = beta_direction / pi * 180
        print("beta direction in gradi " + str(beta_direction_degree) + "\n")

        #leftMotor.setVelocity(MAX_SPEED - pi + TURN_COEFFICIENT * beta)
        #rightMotor.setVelocity(MAX_SPEED - pi - TURN_COEFFICIENT * beta)
        #speed_vector = [MAX_SPEED, MAX_SPEED]
        # a target position has been reached
        if distance <= DISTANCE_TOLERANCE:
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            time.sleep(1)
            return

        # def check_next_checkpoint():


#     #print("SONO DENTRO CHECK NEXT")
#     checkpoint_result = TARGET_POINTS[current_target_index]
#     if speed[0] == 0.0 and speed[1] == 0.0 and current_target_index == 0:
#         updated_target = current_target_index + 1
#         print("UPDATED TARGET " + str(updated_target))
#         updated_target %= TARGET_POINTS_SIZE
#         checkpoint_result = TARGET_POINTS[updated_target]
#     return checkpoint_result

def turn(checkpoint_coord):
    pos3d = gps.getValues()
    current_position = [pos3d[0], pos3d[2]]
    # TODO generalise for both axes
    if abs(checkpoint_coord[0]) > abs(current_position[0]):
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(MAX_SPEED)

    ##beta = -1.5708
    # direction = minus(checkpoint_coord, current_position)
    # print("DIRECTION " + str(direction))
    # distance = norm(direction)
    # direction = normalize(direction)
    ##speed_vector = [MAX_SPEED - pi + TURN_COEFFICIENT * beta,  MAX_SPEED - pi - TURN_COEFFICIENT * beta]
    # a target position has been reached
    # if distance < DISTANCE_TOLERANCE:
    ##print("COUNTER " + str(counter))
    ##if counter > 13:
        # print("Checkpoint " + str(checkpoint_coord) + " raggiunto!")
        # current_target_index += 1
        # current_target_index %= TARGET_POINTS_SIZE
    ##    speed_vector = [0.0, 0.0]
    ##return [counter+1, speed_vector]



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

    # distance_sensors = init_distance_sensors(robot)

    set_forward_speed()
    step(checkpoint)
    [current_target_index, checkpoint] = update_checkpoint(current_target_index)
    print(checkpoint)
    turn(checkpoint)
    step_turn()

    set_forward_speed()
    step(checkpoint)

    # while robot.step(TIME_STEP) != -1:
    #     # read gps position and compass values
    #     pos3D = gps.getValues()  # [x,y,z]
    #     #print("gps: " + str(pos3D))
    #     # north3D = compass.getValues()  # [x, NaN, z]  u = 1, v = 2
    #     # print("compass: " + str(north3D))
    #
    #     # compute the 2D position of the robot and its orientation
    #     pos = [pos3D[0], pos3D[2]]
    #     # north = [north3D[0], north3D[2]]
    #     # front = [-north[0], north[1]]
    #
    #     if current_target_index == 0:
    #         speed = run_forward(checkpoint, pos)
    #         new_checkpoint = check_next_checkpoint()
    #         print(new_checkpoint)
    #
    #     if new_checkpoint != checkpoint:
    #         checkpoint = new_checkpoint
    #         [new_counter, speed] = turn(new_checkpoint, pos, counter)
    #         counter = new_counter
    #
    #     leftMotor.setVelocity(speed[0])
    #     rightMotor.setVelocity(speed[1])
    # Enter here exit cleanup code.
