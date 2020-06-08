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

# Const for robot path: turn coefficient and checkpoint distance tolerance
DISTANCE_TOLERANCE = 0.2
TURN_COEFFICIENT = 4.0
