from controllers.utils.const import MAX_SENSOR_NUMBER, MAX_SENSOR_VALUE, MIN_DISTANCE, WEIGHT_SENSORS, FORWARD, \
    WHEEL_WEIGHT_THRESHOLD, SPEED_CHANGE_FACTOR, MAX_SPEED, LEFT, RIGHT


def obstacle_avoid(distance_sensors, leftMotor, rightMotor, state):

    speed = [0.0, 0.0]
    wheel_weight_total = [0.0, 0.0]

    for i in range(MAX_SENSOR_NUMBER):
        sensor_value = distance_sensors[i].getValue()

        if sensor_value == 0.0:
            speed_modifier = 0.0
        else:
            distance = 5.0 * (1.0 - (sensor_value / MAX_SENSOR_VALUE))
            if distance < MIN_DISTANCE:
                speed_modifier = 1 - (distance / MIN_DISTANCE)
            else:
                speed_modifier = 0.0
        for j in range(2):
            wheel_weight_total[j] += WEIGHT_SENSORS[i][j] * speed_modifier

    if state == FORWARD:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = SPEED_CHANGE_FACTOR * MAX_SPEED
            speed[1] = -SPEED_CHANGE_FACTOR * MAX_SPEED
            state = LEFT
        elif wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = -SPEED_CHANGE_FACTOR * MAX_SPEED
            speed[1] = SPEED_CHANGE_FACTOR * MAX_SPEED
            state = RIGHT
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
    elif state == LEFT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = SPEED_CHANGE_FACTOR * MAX_SPEED
            speed[1] = -SPEED_CHANGE_FACTOR * MAX_SPEED
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
            state = FORWARD
    elif state == RIGHT:
        if wheel_weight_total[0] > WHEEL_WEIGHT_THRESHOLD \
                or wheel_weight_total[1] > WHEEL_WEIGHT_THRESHOLD:
            speed[0] = -SPEED_CHANGE_FACTOR * MAX_SPEED
            speed[1] = SPEED_CHANGE_FACTOR * MAX_SPEED
        else:
            speed[0] = MAX_SPEED
            speed[1] = MAX_SPEED
            state = FORWARD

    leftMotor.setVelocity(speed[0])
    rightMotor.setVelocity(speed[1])

    return state
