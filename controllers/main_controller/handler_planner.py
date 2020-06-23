import logging


def exec_plan(controller, plan):
    start_index = int(len(plan["MissionTimeline"].keys()) / 3)
    stop_index = start_index + int(len(plan["RobotDeliveryToPatient"].keys()) / 3)
    # [(lb_start, ub_start, action)]
    ordered_list = []

    for i in range(start_index, stop_index):
        action = plan["RobotDeliveryToPatient"]["Action " + str(i)]
        start_time = plan["RobotDeliveryToPatient"]["Start " + str(i)]
        if "MoveTo" in action:
            new_action = action.replace("MoveTo", "").replace("-", "")
            ordered_list.append((int(start_time[0]), int(start_time[1]), new_action))

    sorted(ordered_list, key=lambda x: x[0])
    ordered_list.insert(0, (0, 0, "Warehouse"))

    def run(index):
        if index == len(ordered_list):
            return
        else:
            time_to_go = [ordered_list[index][0], ordered_list[index][1]]
            if time_to_go[0] <= controller.time <= time_to_go[1]:
                controller.create_path(ordered_list[index - 1][2], ordered_list[index][2])
                controller.step()
                run(index + 1)
            elif controller.time < time_to_go[0]:
                # waiting start time
                # TODO  add safe point if time for waiting is too high
                controller.step_with_time(time_to_go[0])
                run(index)
            else:
                logging.info("We are late but we continue the delivery")
                controller.create_path(ordered_list[index - 1][2], ordered_list[index][2])
                controller.step()
                run(index + 1)
    run(1)
