import main

def BFS(grid, start_coordinates):
	fringe = [] # will act as a queue
	visited = []
	fringe.append(start_coordinates)
	while fringe:
		curr = fringe.pop(0) # dequeuing from queue
		visited.append(curr)
		grid.change_explored(grid, curr)
		for node in grid.get_neighbours(grid, curr):
			if node not in fringe and node not in visited:
				grid.change_fringe(grid, node)
				fringe.append(node)
		grid.draw(grid)
	print("\n\tDONE!\n")