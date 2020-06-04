# Const per avoid obstacles

MAX_SENSOR_NUMBER = 16
MAX_SPEED = 5.24
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
    (150, 0),  (200, 0),  (300, 0),  (600, 0),
    (0, 600),  (0, 300),  (0, 200),  (0, 150),
    (0, 0),    (0, 0),    (0, 0),    (0, 0),
    (0, 0),    (0, 0),    (0, 0),    (0, 0)
]


# Const for gps

DISTANCE_TOLERANCE = 0.2
TURN_COEFFICIENT = 4.0

# coordinate for target points
TARGET_POINTS = [
    [1.44, 31.03], [-5.19, 31.03], [-5.19, 26.99]
]

TARGET_POINTS_SIZE = len(TARGET_POINTS)
