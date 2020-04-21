from os import system
import platform
from time import sleep
import math

import a_star
import bfs
import bfs_shortest_path
import dfs

def get_neighbours(grid, coordinates):
	neighbours = []
	x = coordinates[0]
	y = coordinates[1]

	global global_x
	global global_y

	if y > 0: # LEFT
		neighbours.append([x, y - 1])
	if x < global_x: # DOWN
		neighbours.append([x + 1, y])
	if y < global_y: # RIGHT
		neighbours.append([x, y + 1])
	if x > 0: # UP
		neighbours.append([x - 1, y])

	return neighbours

def add_barriers(grid):
	draw(grid)

	prompt = input("\n\tDo You Want to Add Barriers [Y/N]: ")

	while prompt == "Y":
		coordinates = list((input("\n\tEnter Barrier Coordinates [x,y]: ")).split(","))
		coordinates[0] = int(coordinates[0])
		coordinates[1] = int(coordinates[1])

		grid[coordinates[0]][coordinates[1]] = "#"

		draw(grid)

		again = input("\n\tDo you want to Add More [Y/N]: ")
		if again == "Y":
			pass
		else:
			prompt = "N"


def check_barrier(grid, coordinates):
	x = coordinates[0]
	y = coordinates[1]

	if grid[x][y] == "#":
		return True
	return False

def change_explored(grid, coordinates):
	x = coordinates[0]
	y = coordinates[1]

	grid[x][y] = "X"

def change_fringe(grid, coordinates):
	x = coordinates[0]
	y = coordinates[1]

	grid[x][y] = "Q"

def set_goal(grid, coordinates):
	x = coordinates[0]
	y = coordinates[1]

	grid[x][y] = "G"

def draw_path(grid, path):
	for n in path:
		x = n[0]
		y = n[1]
		grid[x][y] = "P"

	draw(grid)

def clear_screen():
	if platform.system() == "Windows":
		system("cls")
	elif platform.system() == "Linux":
		system("clear")

def draw(grid):
	sleep(0.2)
	clear_screen()

	print("\t- : Unexplored")
	print("\tX : Explored")
	print("\tQ : In Queue")
	print("\t# : Barrier")
	print("\tG : Goal Node")
	print("\tP : Path\n")

	for row in grid:
		string = ""
		for n in row:
			string += n + "  "
		print("\t" + string)

if __name__ == "__main__":
	clear_screen()

	global_x = int(input("Enter Rows   : "))
	global_y = int(input("Enter Columns: "))

	clear_screen()

	start_coordinates = list((input("Enter Start Coordinates [x,y]: ")).split(","))
	start_coordinates[0] = int(start_coordinates[0])
	start_coordinates[1] = int(start_coordinates[1])

	grid = [["-"] * global_y for i in range(global_x)]

	set_goal(grid, end_coordinates)

	global_x -= 1
	global_y -= 1

	print("\n\tSelect Algorithm:")
	print("\t1. A Star")
	print("\t2. BFS")
	print("\t3. DFS")
	print("\t4. BFS Shortest Path")
	algorithm = int(input("\tSelection: "))

	if algorithm == 1 or algorithm == 4:
		end_coordinates = list((input("Enter End Coordinates [x,y]: ")).split(","))
		end_coordinates[0] = int(end_coordinates[0])
		end_coordinates[1] = int(end_coordinates[1])

		set_goal()

	add_barriers(grid)