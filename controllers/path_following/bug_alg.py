
CRUISING_SPEED = 7.5
TOLERANCE = -0.1
OBSTACLE_THRESHOLD = 0.5
SLOWDOWN_FACTOR = 0.5

FOLLOW_OBSTACLE = 1
GO_TO_TARGET = 2

def bug_algorithm(robot, left_motor, right_motor, back_gps, center_gps, kinect, distance_sensors):
    kinect_width = kinect.getWidth()
    kinect_height = kinect.getHeight()

    half_width = kinect_width/2 #CONTROLLA SE È IL CASO DI CASTARLI AD INT
    view_height = kinect_height/2 + 10

    max_range = kinect.getMaxRange()
    range_threshold = 0.7
    inv_max_range_times_width = 1.0/(max_range * kinect_width)

    target_x = 0
    target_z = 4.684

    left_obstacle = 0.0
    right_obstacle = 0.0
    obstacle = 0.0

    delta_obstacle = 0.0
    left_speed = CRUISING_SPEED
    right_speed = CRUISING_SPEED

    speedFactor = 1.0

    value = 0.0
    i = 0
    side_obstacle = 0.0
    mode = GO_TO_TARGET
    distance_value = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    while True:
        for i in range(8):
            distance_value[i] = distance_sensors[i].getValue()
        side_obstacle = distance_value[0] + distance_value[1] + distance_value[6] + distance_value[7]

        kinectValues = kinect.getRangeImage()

        for i in range(half_width):
            value =  kinectValues.getRangeImage
