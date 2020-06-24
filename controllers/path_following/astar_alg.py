from controllers.hospital_map.graph import MAP_POINTS, EDGES
from controllers.utils.coordinate_utils import calculate_distance


def astar(start: str, end: str):

	closed_list = []  # the set of nodes already evaluated
	open_list = [start]  # the set of tentative nodes to be evaluated

	g_score = h_score = f_score = {}
	came_from = {}

	g_score[start] = 0  # distance from start along optimal path
	h_score[start] = calculate_distance(MAP_POINTS[start], MAP_POINTS[end])  # heuristic for estimate of distance
	f_score[start] = h_score[start]  # estimated total distance from start to goal through y

	optimal_path = []

	while open_list:
		f_score_value = [(x, f_score[x]) for x in open_list]
		min_f_score_value = min(map(lambda x: x[1], f_score_value))
		list_node_name = [x[0] for x in f_score_value if x[1] == min_f_score_value]  # list with a single value

		node_name = list_node_name[0]

		if node_name == end:
			return reconstruct_path(came_from, end, optimal_path)
		open_list.remove(node_name)
		closed_list.append(node_name)

		neighbor_nodes = [e[(i + 1) % 2] for e in EDGES for i, _ in enumerate(e) if node_name == e[i]]

		for y in neighbor_nodes:
			if y in closed_list:
				continue

			tentative_g_score = g_score[node_name] + calculate_distance(MAP_POINTS[node_name], MAP_POINTS[y])

			if y not in open_list:
				open_list.append(y)
				tentative_is_better = True
			elif tentative_g_score < g_score[y]:
				tentative_is_better = True
			else:
				tentative_is_better = False
			if tentative_is_better:
				came_from[y] = node_name
				g_score[y] = tentative_g_score
				h_score[y] = calculate_distance(MAP_POINTS[start], MAP_POINTS[end])
				f_score[y] = g_score[y] + h_score[y]
	return None


def reconstruct_path(came_from, current_node, result):
	if current_node in came_from:
		result.insert(0, current_node)
		reconstruct_path(came_from, came_from[current_node], result)
		return result
	else:
		return []
