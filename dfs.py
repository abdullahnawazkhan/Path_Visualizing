import main

def DFS(grid, start_coordinates):
	fringe = [] # will act as a stack, with fringe[0] being stack-top
	visited = []
	fringe.append(start_coordinates)
	while fringe:
		curr = fringe.pop(0)
		visited.append(curr)
		main.change_explored(grid, curr)
		# to maintain the order of left-right
		# so that we go deeper down the left path first and then the right ones
		# we need to insert neighbour nodes in fringe in with respect to the top of stack
		neighbours = []
		for node in main.get_neighbours(grid, curr):
			if node not in fringe and node not in visited:
				neighbours.append(node)
		for node in reversed(neighbours): # will maintain left-right
			fringe.insert(0, node)
		main.draw(grid)
	print("\n\tDONE!\n")