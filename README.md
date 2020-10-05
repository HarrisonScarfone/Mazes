# Mazes

Written in Python 3.8.2 using Pygame, `Mazes` procedural generates than solves mazes.

## Current Information and Potential Upcoming

Mazes is currently hardcoded to use a single generation type and a single solve type.  There is a nice bar of space in the window that in the future, will hopefully hold some controls for the program and allow the user to swap out generation and solving algorithms, run multiple cycles, compare solve times, etc. 

## Requirements

Python 3.8.2 (should be fine on anything 3.7+ though)

Pygame

```shell
sudo apt-get install python3-pygame
```

## Running the Program

Run the `main.py` file in the parent directory with:

```shell
python3 main.py
```

As of now, there is no user input required.  A window will pop up and the run will begin in 2 seconds.

## Example Run

Looks smoother when run vs this animation but hopefully this gives an idea of what the code does.

![Failed to load example GIF](/sample_maze_run.gif?raw=true "Maze Gen/Solve Sample Run")

## Generation Algorithms

### Randomized Prim's (or at least my take on it) - Currently hardcoded as the only generation method

Randomized Prim's uses a starting node position to randomly generate a guarenteed spanning set across the board.

## Solving Algorithms

### Depth First Search (recursive) - Currently hardcoded as the only solve method

Recursive DFS takes a starting node and traverses the entire board (I thought the fill looked really cool) and spits out a path when it finds the end node. This path is then drawn on the board in a different color than the search.



