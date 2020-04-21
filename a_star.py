import main

def get_heuristic(curr_coordinates, goal_coordinates):
    # using manhattan distance
	x1 = curr_coordinates[0]
	y1 = curr_coordinates[1]

	x2 = goal_coordinates[0]
	y2 = goal_coordinates[1]

	result = abs(x2 - x1) + abs(y2 - y1)
	return result # for getting an under-estimate we round down

def a_star_algorithm(grid, start_node, stop_node):
	main.set_goal(grid, stop_node)

	open_list = [start_node] # nodes evaluated but not expanded on
	closed_list = [] # nodes expanded on

	g = {} # will contain g(n), distance from start_node, for all nodes
	g[str(start_node)] = 0

	parents = {} # will be used to keep paths
	parents[str(start_node)] = str(start_node)

	while open_list:
		curr_node = None
		for node in open_list:
			# selecting node with lowest A* score (g(n) + h(n))
			if curr_node == None:
				curr_node = node
			else:
				scoreA = g[str(curr_node)] + get_heuristic(curr_node, stop_node)
				scoreB = g[str(node)] + get_heuristic(node, stop_node)
				if scoreB < scoreA:
					curr_node = node

		if curr_node == stop_node:
			print("Path Found")

			path = []
			path.append(curr_node)
			node = curr_node
			while node != start_node:
				temp = parents[str(node)]
				temp = temp.replace("[", "")
				temp = temp.replace("]", "")
				temp = temp.split(", ")
				n_node = []
				n_node.append(int(temp[0]))
				n_node.append(int(temp[1]))
				node = n_node
				path.append(node)
			path.reverse()
			main.draw_path(grid, path)
			break

		else:
			main.change_explored(grid, curr_node)
			main.draw(grid)
			open_list.remove(curr_node)
			closed_list.append(curr_node)
			for neighbour in main.get_neighbours(grid, curr_node):
				if main.check_barrier(grid, neighbour) == True:
					continue
				if neighbour in closed_list:
					continue # will skip the current iteration
				elif neighbour in open_list:
					# if specific node is already in open_list we can compare its g(n) value and the new g(n)
					# if new g(n) value is lower than old then we will update the values of g[n] and parent[n]
					new_g = g[str(curr_node)] + get_heuristic(neighbour, stop_node)
					if new_g > g[str(neighbour)]:
						continue # will skip current iteration as new value is greater

				g[str(neighbour)] = g[str(curr_node)] + 1
				parents[str(neighbour)] = str(curr_node)

				if neighbour not in open_list and neighbour not in closed_list:
					main.change_fringe(grid, neighbour)
					open_list.append(neighbour)
			main.draw(grid)