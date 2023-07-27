""" What is maze labyrinth game?
ans) The maze labyrinth game is a simple text-based game. The maze is represented as a grid of cells, where each cell can be a wall, 
a path , or an exit .The player's objective is to find the exit from the maze. The maze is randomly generated each time the game is played,
offering a new challenge with each playthrough.Players can navigate through the maze by following the paths while avoiding the walls until 
they reach the exit."""


import random

WALL = "W"
PATH = "."
EXIT = "E"

def create_maze(rows, cols):
	maze = [[None for _ in range(cols)]for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			maze[i][j] = random.choice([WALL,PATH,PATH,PATH,EXIT])
			
	return maze
	
def display_maze(maze):

	for row in maze:
		print(" ".join(row))
		
def main():
	rows, cols = 5, 10
	maze = create_maze(rows, cols)
	display_maze(maze)
	
if __name__ == "__main__":
	main()

""""
Explanation:-
(1)import random
Import the random module to generate random elements for the maze.

(2)WALL = "W", PATH = ".", EXIT = "E"
Define constants for maze elements to represent walls, paths, and exits.

(3)def create_maze(rows, cols)
Define a function to create a random maze grid.

(4)maze = [[None for _ in range(cols)] for _ in range(rows)]
Create an empty maze grid using a nested list comprehension, with rows rows and cols columns, filled with None.

(5)for i in range(rows):
Loop through each row.

(6)for j in range(cols):
Loop through each column.

(7)maze[i][j] = random.choice([WALL, PATH, EXIT])
Randomly choose an element for each cell in the maze grid with a 60% chance of being a path (.), 20% chance of being a wall (W), and 20% chance of being an exit (E).

(8)def display_maze(maze): 
Define a function to display the maze grid.

(9)for row in maze:
Loop through each row in the maze grid.

(10)print(" ".join(row)): 
Join each element in the row with a space and print the row, effectively displaying the maze grid row by row.

(11)def main(): 
Define the main function to create and display the maze.

(12)rows, cols = 5, 10: 
Define the number of rows and columns for the maze (a 5x10 maze in this case).

(13)maze = create_maze(rows, cols): 
Create the maze using the create_maze() function with the specified number of rows and columns.

(14)display_maze(maze): 
Display the maze using the display_maze() function.

(15)if __name__ == "__main__":
Check if the script is being run as the main program.

(16)main(): 
Call the main() function to create and display the maze when the script is run.
