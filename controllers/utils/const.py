# Const per avoid obstacles
MAX_SENSOR_NUMBER = 16
MAX_SPEED = 12.00
MIN_SPEED = MAX_SPEED / 2
MAX_SENSOR_VALUE = 1024
MIN_DISTANCE = 1.0
NAME_SENSOR = "so"
WHEEL_WEIGHT_THRESHOLD = 100
SPEED_CHANGE_FACTOR = 0.7
TIME_STEP = 16

TIME_ALIGN = 15

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
DISTANCE_BRAKE = 0.8
DISTANCE_TOLERANCE = 0.2
TURN_COEFFICIENT = 4.0

# Const for motor
LEFT_WHEEL = "left wheel"
RIGHT_WHEEL = "right wheel"

# Const for gps
GPS = "gps"

# Const for compass
COMPASS = "compass"

# Const for controller mode
AUTOMATIC = 0
MANUAL = 1

# State variable for Platinum
ROBOT_MISSION_TIMELINE = "MissionTimeline"
ROBOT_DELIVERY_TO_PATIENT = "RobotDeliveryToPatient"
ROBOT_MOVE_TO_ROOM = "RobotMoveToRoom"

# Logger
LOGGING_FILE = "../../pioneer3dx.log"

# Planning (file txt must be in main project dir)
PLANNING_FILE = "../../plan.txt"
