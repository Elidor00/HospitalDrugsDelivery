from controller import Robot
from controllers.hospital_map.graph import MAP_POINTS
from controllers.path_following.pioneer3dx_follow_mod import move_to
from controllers.path_following.search_alg import astar
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

    # calculate path between start and end with A* algorithm
    nodes_path = astar("Warehouse", "R4Bed0")
    print(nodes_path)

    for checkpoint in nodes_path:
        move_to(robot, gps, compass, leftMotor, rightMotor, MAP_POINTS[checkpoint])
