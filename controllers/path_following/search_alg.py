from controllers.hospital_map.graph import *
from controllers.utils.coordinate_utils import minus, norm


def astarv2(start, end):
	closed_list = []
	open_list = []

	open_list.append(start)

	g_score = h_score = f_score = {}

	g_score[start] = 0
	came_from = {}
	h_score[start] = norm(minus(MAP_POINTS[start], MAP_POINTS[end]))
	f_score[start] = h_score[start]
	res = []

	while open_list is not []:
		f_score_value = [(x, f_score[x]) for x in open_list]
		min_f_score_value = min(map(lambda x: x[1], f_score_value))
		x = [x[0] for x in f_score_value if x[1] == min_f_score_value]

		if x[0] == end:
			x = reconstruct_path(came_from, end, res)
			return x
		open_list.remove(x[0])
		closed_list.append(x[0])

		# [e[(i+1) % 2] for e in list for i,_ in enumerate(e) if "corr" == e[i]]
		neighbor_nodes = [e[(i + 1) % 2] for e in EDGES for i, _ in enumerate(e) if x[0] == e[i]]
		for y in neighbor_nodes:
			if y in closed_list:
				continue
			tentative_g_score = g_score[x[0]] + norm(minus(MAP_POINTS[x[0]], MAP_POINTS[y]))

			if y not in open_list:
				open_list.append(y)
				tentative_is_better = True
			elif tentative_g_score < g_score[y]:
				tentative_is_better = True
			else:
				tentative_is_better = False
			if tentative_is_better:
				came_from[y] = x[0]
				g_score[y] = tentative_g_score
				h_score[y] = norm(minus(MAP_POINTS[start], MAP_POINTS[end]))
				f_score[y] = g_score[y] + h_score[y]
	return None


def reconstruct_path(came_from, current_node, result):
	if current_node in came_from:
		# print("CAME_FROM " + str(came_from))
		# print("CURRENT_NODE " + str(current_node))
		# print("FINE " + str(came_from[current_node]))
		result.insert(0, current_node)
		reconstruct_path(came_from, came_from[current_node], result)
		# tmp = p.append(current_node)
		# print(tmp)
		# print(result)
		return result
	else:
		return []


'''
class Node():
	"""A node class for A* Pathfinding"""

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position  # coord vector [...]

		self.g = 0  # g is the distance between the current node and the start node
		self.h = 0  # h is the heuristic — estimated distance from the current node to the end node
		self.f = 0  # f = g + h

	def __eq__(self, other):
		return self.position == other.position


def astar(maze, start, end):
	"""Returns a list of tuples as a path from the given start to the given end in the given maze"""

	# Create start and end node
	start_node = Node(None, start)
	start_node.g = start_node.h = start_node.f = 0
	end_node = Node(None, end)
	end_node.g = end_node.h = end_node.f = 0

	# Initialize both open and closed list
	open_list = []
	closed_list = []

	# Add the start node
	open_list.append(start_node)

	# Loop until you find the end
	while len(open_list) > 0:

		# Get the current node
		current_node = open_list[0]
		current_index = 0
		for index, item in enumerate(open_list):
			if item.f < current_node.f:
				current_node = item
				current_index = index

		# Pop current off open list, add to closed list
		open_list.pop(current_index)
		closed_list.append(current_node)

		# Found the goal
		if current_node == end_node:
			path = []
			current = current_node
			while current is not None:
				path.append(current.position)
				current = current.parent
			return path[::-1]  # Return reversed path

		# Generate children
		children = []
		for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

			new_position =

		for new_position in maze[qualcosa]


			# Get node position
			node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
			# -10.26 + 0 , 0.22 - 1




			# Make sure within range
			if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
					len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
				continue

			# Make sure walkable terrain
			if maze[node_position[0]][node_position[1]] != 0:
				continue

			# Create new node
			new_node = Node(current_node, node_position)

			# Append
			children.append(new_node)

		# Loop through children
		for child in children:

			# Child is on the closed list
			for closed_child in closed_list:
				if child == closed_child:
					continue

			# Create the f, g, and h values
			child.g = current_node.g + 1
			child.h = ((child.position[0] - end_node.position[0]) ** 2) + \
					  ((child.position[1] - end_node.position[1]) ** 2)
			child.f = child.g + child.h

			# Child is already in the open list
			for open_node in open_list:
				if child == open_node and child.g > open_node.g:
					continue

			# Add the child to the open list
			open_list.append(child)


def create_dict_from_list(tup):
	dictionary = {}
	for a, b in tup:
		dictionary.setdefault(a, b)
	return dictionary


def main():
	index_point = [(x, i) for (i, x) in enumerate(MAP_POINTS)]
	# print(index_point)

	dict_index_point = create_dict_from_list(index_point)
	# print(dict_index_point)

	# nodes must be numbers in a sequential range starting at 0 - so this is the
	# number of nodes. you can assert this is the case as well if desired
	size = len(set([n for e in EDGES for n in e]))
	# make an empty adjacency list
	adjacency = [[0] * size for _ in range(size)]
	# populate the list for each edge
	for sink, source in EDGES:
		adjacency[dict_index_point[sink]][dict_index_point[source]] = 1
		adjacency[dict_index_point[source]][dict_index_point[sink]] = 1

	print(adjacency)

	start = MAP_POINTS["Warehouse"]
	end = MAP_POINTS["EntryR0"]

	path = astar(adjacency, start, end)
	print(path)
'''

def main():
	path = astarv2("Warehouse", "BetweenR1B1B2")
	print(path)

if __name__ == '__main__':
	main()
