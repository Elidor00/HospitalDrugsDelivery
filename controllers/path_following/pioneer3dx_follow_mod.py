from controllers.utils.const import *
from controllers.utils.coordinate_utils import *


def run_forward(checkpoint_coord, current_position):
    # TODO add check in proximity of checkpoint_coord for reduce velocity
    # comment avoid_obstacles for testing gps
    # state = avoid_obstacles(distance_sensors, leftMotor, rightMotor, state)

    # compute the direction and the distance from the target
    direction = minus(checkpoint_coord, current_position)
    print("DIRECTION " + str(direction))
    distance = norm(direction)
    # direction = normalize(direction)
    speed_vector = [MAX_SPEED, MAX_SPEED]
    # a target position has been reached
    if distance < DISTANCE_TOLERANCE:
        # print("Checkpoint " + str(checkpoint_coord) + " raggiunto!")
        # current_target_index += 1
        # current_target_index %= TARGET_POINTS_SIZE
        speed_vector = [0.0, 0.0]
    return speed_vector



def turn(checkpoint_coord, current_position, counter):
    #if abs(checkpoint_coord[0]) > abs(current_position[0]):
    beta = -1.5708
    # direction = minus(checkpoint_coord, current_position)
    # print("DIRECTION " + str(direction))
    # distance = norm(direction)
    # direction = normalize(direction)
    speed_vector = [MAX_SPEED - pi + TURN_COEFFICIENT * beta,  MAX_SPEED - pi - TURN_COEFFICIENT * beta]
    # a target position has been reached
    # if distance < DISTANCE_TOLERANCE:
    print("COUNTER " + str(counter))
    if counter > 13:
        # print("Checkpoint " + str(checkpoint_coord) + " raggiunto!")
        # current_target_index += 1
        # current_target_index %= TARGET_POINTS_SIZE
        speed_vector = [0.0, 0.0]
    return [counter+1, speed_vector]



