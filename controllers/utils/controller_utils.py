from controllers.utils.const import MAX_SPEED


# set the speed to the maximum speed reachable by the robot
def normalize_speed(speed):
    if speed > MAX_SPEED:
        speed = MAX_SPEED
    elif speed < -MAX_SPEED:
        speed = -MAX_SPEED
    return speed


def goto(controller, start, end):
    controller.create_path(start, end)
    controller.step()
    controller.current_position = end
