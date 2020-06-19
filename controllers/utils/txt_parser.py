from controllers.utils.const import ROBOT_DELIVERY_TO_PATIENT, ROBOT_MOVE_TO_ROOM, ROBOT_MOVE_TO_ZONE
import re

dict_result = {ROBOT_MOVE_TO_ZONE: {}, ROBOT_DELIVERY_TO_PATIENT: {}, ROBOT_MOVE_TO_ROOM: {}}

regex_RobotMoveToZone = r"RobotMoveToZone \{([^}]*)}"
regex_RobotDeliveryToPatient = r"RobotDeliveryToPatient \{([^}]*)}"
regex_RobotMoveToRoom = r"RobotMoveToRoom \{([^}]*)}"
regex = [regex_RobotMoveToZone, regex_RobotDeliveryToPatient, regex_RobotMoveToRoom]


def get_regex_res(reg, filename):
	with open(filename, 'r') as fh:
		matches = re.findall(reg, fh.read(), re.MULTILINE)
		return matches


def create_dict_res(res, reg, index):
	dict_result[reg.split(" ")[0]]["Token" + str(index)] = res[1].split(":")[1]  # remove [1] if you want the token number
	dict_result[reg.split(" ")[0]]["start" + str(index)] = eval(res[3])  # remove eval() if you want string
	dict_result[reg.split(" ")[0]]["end" + str(index)] = eval(res[5])
	dict_result[reg.split(" ")[0]]["duration" + str(index)] = eval(res[7])
	return dict_result


def parse(filename):
	for reg in regex:
		matches = get_regex_res(reg, filename)
		matches = matches[0]

		matches = matches.strip().split("\n")
		matches = [x.strip(' ') for x in matches]

		for i in range(len(matches)):
			element = matches[i][:-1]

			[i.strip("[]").split(" ") for i in element]
			res = element.split(" ")
			# print(res[1])  # token value if needed

			return create_dict_res(res, reg, i)
			# dict_result[reg.split(" ")[0]]["Token" + str(i)] = res[1].split(":")[1]  # remove [1] if you want the token number
			# dict_result[reg.split(" ")[0]]["start" + str(i)] = eval(res[3])  # remove eval() if you want string
			# dict_result[reg.split(" ")[0]]["end" + str(i)] = eval(res[5])
			# dict_result[reg.split(" ")[0]]["duration" + str(i)] = eval(res[7])
	# print(dict_result)
	# return dict


