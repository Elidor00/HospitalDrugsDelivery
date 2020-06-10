from controllers.utils.const import TIME_STEP, MAX_SPEED
from controllers.utils.init_sensors import set_velocity


def check_keyboard(keyboard, gps):
    key = keyboard.getKey()
    print(key)
    if key <= 0:
        return False
    else:
        if key == ord('P'):  # 80 is the ASCII for 'P'
            print("GPS " + str(gps.getValues()))
            return False
        elif key == ord('E'):
            return True
        else:
            print("Key value not valid")
            return False


def manual_control(robot, left_motor, right_motor, keyboard, gps):
    print("SONO QUA")
    robot.step(1000)
    while robot.step(TIME_STEP) != -1:
        set_velocity(left_motor, right_motor, 0.0, 0.0)  # TODO: si ferma un po' troppo bruscamente
        key = keyboard.getKey()
        print(key)
        if key <= 0:
            continue
        else:
            if key == ord('P'):
                print("GPS " + str(gps.getValues()))
            elif key == ord('W'):
                set_velocity(left_motor, right_motor)
            elif key == ord('A'):
                set_velocity(left_motor, right_motor, left_speed=-MAX_SPEED)
            elif key == ord('D'):
                set_velocity(left_motor, right_motor, right_speed=-MAX_SPEED)
            elif key == ord('S'):
                set_velocity(left_motor, right_motor, -MAX_SPEED, -MAX_SPEED)
            else:
                print("Key value not valid")
                return False
