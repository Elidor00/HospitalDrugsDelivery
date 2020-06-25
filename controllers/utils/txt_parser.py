import re
import logging

from controllers.utils.const import ROBOT_DELIVERY_TO_PATIENT, ROBOT_MOVE_TO_ROOM, ROBOT_MISSION_TIMELINE

dict_result = {ROBOT_MISSION_TIMELINE: {}, ROBOT_DELIVERY_TO_PATIENT: {}, ROBOT_MOVE_TO_ROOM: {}}

regex_MissionTimeline = r"MissionTimeline \{((.|\n)*?)\}\s+}"
regex_RobotDeliveryToPatient = r"RobotDeliveryToPatient \{((.|\n)*?)\}\s+}"
regex_RobotMoveToRoom = r"RobotMoveToRoom \{((.|\n)*?)\}\s+}"
regex = [regex_MissionTimeline, regex_RobotDeliveryToPatient, regex_RobotMoveToRoom]

regex_value = r"token (\d+)\s+\{ ([a-zA-Z-0-9]*) \[(\d+),\s*(\d+)\] \[(\d+),\s*(\d+)\] \}"


def get_interesting_value(matches):
	return [re.findall(regex_value, x, re.MULTILINE) for x in matches]


def get_match(reg, filename):
	try:
		with open(filename, 'r') as f:
			matches = re.findall(reg, f.read(), re.MULTILINE)
			return str(matches[0])
	except IOError as e:
		logging.error(f"{e}")


def create_dict_res(el, reg):
	dict_result[reg.split(" ")[0]]["Action " + str(el[0][0])] = el[0][1]
	dict_result[reg.split(" ")[0]]["Start " + str(el[0][0])] = [el[0][2], el[0][3]]
	dict_result[reg.split(" ")[0]]["End " + str(el[0][0])] = [el[0][4], el[0][5]]


def parse(filename):
	for r in regex:
		matches = get_match(r, filename)

		matches = matches[1:-1].replace("\\t", "").split("\\n")
		matches[len(matches)-1] = matches[len(matches)-1][:-7] + " }"
		matches = matches[1:]

		value = get_interesting_value(matches)

		for i in range(len(value)):
			element = value[i]
			create_dict_res(element, r)

	logging.info(f"Dictionary resulted from planning file: \n {pretty(dict_result)}")
	return dict_result


def pretty(d):
	res = ""
	for x in d:
		res += str(x) + '\n'
		for y in d[x]:
			res += '\t' + str(y) + ' = ' + str(d[x][y]) + '\n'
	return res
