import re
import logging

from controllers.utils.const import ROBOT_DELIVERY_TO_PATIENT, ROBOT_MOVE_TO_ROOM, ROBOT_MOVE_TO_ZONE

dict_result = {ROBOT_MOVE_TO_ZONE: {}, ROBOT_DELIVERY_TO_PATIENT: {}, ROBOT_MOVE_TO_ROOM: {}}

regex_RobotMoveToZone = r"MissionTimeline \{([^}]*)}"
regex_RobotDeliveryToPatient = r"RobotDeliveryToPatient \{([^}]*)}"
regex_RobotMoveToRoom = r"RobotMoveToRoom \{([^}]*)}"
regex = [regex_RobotMoveToZone, regex_RobotDeliveryToPatient, regex_RobotMoveToRoom]


def get_match(reg, filename):
	try:
		with open(filename, 'r') as f:
			matches = re.findall(reg, f.read(), re.MULTILINE)
			return matches
	except IOError:
		print("File does not exist!")


def create_dict_res(res, reg, index):
	dict_result[reg.split(" ")[0]]["Token" + str(index)] = res[1].split(":")[1] 
	dict_result[reg.split(" ")[0]]["start" + str(index)] = eval(res[3])  # remove eval() if you want string
	dict_result[reg.split(" ")[0]]["end" + str(index)] = eval(res[5])
	dict_result[reg.split(" ")[0]]["duration" + str(index)] = eval(res[7])


def parse(filename):
	for r in regex:
		matches = get_match(r, filename)
		matches = matches[0]

		matches = matches.strip().split("\n")
		matches = [x.strip(" ") for x in matches]

		for i in range(len(matches)):
			element = matches[i][:-1]
			res = element.split(" ")
			# print(res[1])  # token value if needed

			create_dict_res(res, r, i)

	logging.info(f"Dictionary resulted from planning file: {dict_result}")
	return dict_result
