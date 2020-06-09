def check_keyboard(robot, keyboard, gps):
    key = keyboard.getKey()
    if key <= 0:
        return
    else:
        return {
            ord('P'): lambda: print("GPS " + str(gps.getValues()))  # 80 is the ASCII for 'P'
        }[key]()
