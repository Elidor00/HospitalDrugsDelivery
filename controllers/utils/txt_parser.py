from controllers.utils.const import ROBOT_DELIVERY_TO_PATIENT, ROBOT_MOVE_TO_ROOM, ROBOT_MOVE_TO_ZONE

import re

dict_result = {}


regex_RobotMoveToZone = r"RobotMoveToZone \{([^}]*)}"
regex_RobotDeliveryToPatient = r"RobotDeliveryToPatient \{([^}]*)}"
regex_RobotMoveToRoom = r"RobotMoveToRoom \{([^}]*)}"
regex = [regex_RobotMoveToZone, regex_RobotDeliveryToPatient, regex_RobotMoveToRoom]

dict_result[ROBOT_MOVE_TO_ZONE] = {}
dict_result[ROBOT_DELIVERY_TO_PATIENT] = {}
dict_result[ROBOT_MOVE_TO_ROOM] = {}


def parse(filename):
	with open(filename, 'r') as fh:
		'''
		matches = re.finditer(regex_RobotMoveToRoom, str(fh.read()), re.MULTILINE)
		for matchNum, match in enumerate(matches, start=1):

			print(match.group())
		'''

		matches: list = re.findall(regex_RobotMoveToRoom, str(fh.read()), re.MULTILINE)
		matches: str = matches[0]
		# print(matches)

		matches = matches.strip().split("\n")
		matches = [x.strip(' ') for x in matches]
		print(len(matches))
		for i in range(len(matches)):
			element = matches[i][:-1]
			# print("MATCHES: " + str(element))
			[i.strip("[]").split(" ") for i in element]
			res = element.split(" ")
			# print("RES: " + str(res))
			# print(res[1].split(":")[1])
			dict_result["RobotDeliveryToPatient"]["Token" + str(i)] = res[1].split(":")[1]  # remove [1] if you want the token number
			dict_result["RobotDeliveryToPatient"]["start" + str(i)] = eval(res[3])  # remove eval() if you want string
			dict_result["RobotDeliveryToPatient"]["end" + str(i)] = eval(res[5])
			dict_result["RobotDeliveryToPatient"]["duration" + str(i)] = eval(res[7])
	print(dict_result)


