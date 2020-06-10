from controller import Robot
from controllers.hospital_map.graph import MAP_POINTS
from controllers.manual_pilot.pioneer3dx_manual_mod import check_keyboard, manual_control
from controllers.path_following.pioneer3dx_follow_mod import move_to
from controllers.path_following.search_alg import astar
from controllers.utils.const import LEFT_WHEEL, RIGHT_WHEEL
from controllers.utils.init_sensors import init_gps, init_compass, init_motor, init_keyboard, set_velocity

if __name__ == '__main__':
    # create the Robot instance.
    robot = Robot()

    leftMotor = init_motor(robot, LEFT_WHEEL)
    rightMotor = init_motor(robot, RIGHT_WHEEL)

    keyboard = init_keyboard(robot)

    gps = init_gps(robot)
    compass = init_compass(robot)

    # calculate path between start and end with A* algorithm
    start = "Warehouse"
    stop = "EntryR4"
    nodes_path = astar(start, stop)
    print(nodes_path)

    if nodes_path is None:
        raise Exception(f"Path from {start} to {stop} does not exist")
    else:
        for checkpoint in nodes_path:
            move_to(robot, gps, compass, leftMotor, rightMotor, MAP_POINTS[checkpoint], keyboard, check_keyboard)

    manual_control(robot, leftMotor, rightMotor, keyboard, gps)
