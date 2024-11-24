#Build in libray Import
import random
import time

# Constants for the game
MAZE_SIZE = 5  # Size of the maze
EMPTY = " "     # Empty space
WALL = "#"      # Wall
START = "S"     # Start position
EXIT = "E"      # Exit position
PLAYER = "P"    # Player position

# Maze class for generating and displaying the maze
class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = self.generate_maze()
        self.start_position = (0, 0)
        self.exit_position = (size - 1, size - 1)
        self.player_position = self.start_position

    def generate_maze(self):
        # Generate a random maze with walls
        maze = [[WALL for _ in range(self.size)] for _ in range(self.size)]

        # Make random paths
        for _ in range(self.size * 2):  # Randomly open some paths
            x, y = random.randint(1, self.size - 2), random.randint(1, self.size - 2)
            maze[x][y] = EMPTY

        # Set start and exit points
        maze[0][0] = START
        maze[self.size - 1][self.size - 1] = EXIT

        return maze

    def display(self):
        for row in self.maze:
            print(" ".join(row))
        print()

    def move_player(self, direction):
        x, y = self.player_position

        if direction == "north" and x > 0 and self.maze[x - 1][y] != WALL:
            x -= 1
        elif direction == "south" and x < self.size - 1 and self.maze[x + 1][y] != WALL:
            x += 1
        elif direction == "east" and y < self.size - 1 and self.maze[x][y + 1] != WALL:
            y += 1
        elif direction == "west" and y > 0 and self.maze[x][y - 1] != WALL:
            y -= 1
        else:
            print("Can't move in that direction! It's either a wall or out of bounds.")

        # Update player position
        self.player_position = (x, y)
        self.maze[x][y] = PLAYER

        # Check for victory condition
        if self.player_position == self.exit_position:
            return True
        return False

# Game loop
def play_game():
    print("Welcome to Escape the Maze!\n")
    time.sleep(1)

    maze_game = Maze(MAZE_SIZE)
    maze_game.display()

    while True:
        print("Your current position:", maze_game.player_position)
        move = input("Enter move (north, south, east, west): ").lower()

        if move in ["north", "south", "east", "west"]:
            if maze_game.move_player(move):
                print("Congratulations! You've escaped the maze!")
                break
        else:
            print("Invalid move. Please enter 'north', 'south', 'east', or 'west'.")

        maze_game.display()

# Run the game
if __name__ == "__main__":
    play_game()
