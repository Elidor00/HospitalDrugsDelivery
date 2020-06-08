from controllers.hospital_map.graph import *
# Const per avoid obstacles

MAX_SENSOR_NUMBER = 16
MAX_SPEED = 12.00
MAX_SENSOR_VALUE = 1024
MIN_DISTANCE = 1.0
WHEEL_WEIGHT_THRESHOLD = 100
SPEED_CHANGE_FACTOR = 0.7
TIME_STEP = 16

FORWARD = 0
LEFT = 1
RIGHT = 2

# 16 distance sensors
WEIGHT_SENSORS = [
    (150, 0), (200, 0), (300, 0), (600, 0),
    (0, 600), (0, 300), (0, 200), (0, 150),
    (0, 0), (0, 0), (0, 0), (0, 0),
    (0, 0), (0, 0), (0, 0), (0, 0)
]

# Const for gps

DISTANCE_TOLERANCE = 0.2
TURN_COEFFICIENT = 4.0

'''
# coordinate for target points
TARGET_POINTS = [
    [-10.26, -3.5], [-10.26, -9.56], [-3.67, -9.56], [-3.67, -3.1],
    [1.41, -3.1], [1.41, -7.39], [3.98, -7.39], [-1.18, -7.39],
    [-1.14, -3.1], [-1.14, -4.03], [3.7, -3.1], [3.7, -4.22]
]
'''

TARGET_POINTS = [
    MAP_POINTS["Warehouse"],
    MAP_POINTS["ExitWareHouse"],
    MAP_POINTS["Hallway0"],
    MAP_POINTS["EntryR1"],
    MAP_POINTS["NearR1B0"],
    MAP_POINTS["R1Bed0"],
    MAP_POINTS["NearR1B0"],
    MAP_POINTS["BetweenR1B0B3"],
    MAP_POINTS["EntryR1"],
    MAP_POINTS["Hallway0"],
    MAP_POINTS["ExitWareHouse"]
]

TARGET_POINTS_SIZE = len(TARGET_POINTS)
