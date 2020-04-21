import main

def shortest_path_BFS(grid, start_coordinates, end_coordinates):
	grid.set_goal(grid, end_coordinates)
	# To find the shortest path
	# We will get every single path from [start_node] to Every Node
	# Due to the nature of BFS, when we reach [end_node]
	# that path will always be the shortest path between [start_node] and [end_node]
	# so we will introduce a list containing the paths
	# we will also use the same list as our queue
	# as we dequeue from the list, we will use the last node to continue searching
	visited = []
	paths = [[start_coordinates]] # will keep track of all the paths
	found = False
	while paths:
		curr_path = paths.pop(0) # dequeuing from queue
		curr_node = curr_path[-1] # getting last node to continue the search
		if curr_node not in visited:
			grid.change_explored(grid, curr_node)
			grid.draw(grid)
			for node in grid.get_neighbours(grid, curr_node):
				new_path = curr_path.copy() # new path will be continuation of curr path
				new_path.append(node)
				grid.change_explored(grid, node)
				grid.draw(grid)
				if node == end_coordinates:
					grid.draw_path(grid, new_path)
					print("\n\tDONE!!")
					found = True
					break
				paths.append(new_path)
			visited.append(curr_node)
			if found == True:
				break
	if found == False:
		print("No Paths Sorry")