from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]
grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(3, 2)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, _ = finder.find_path(start, end, grid)

print("Path:", path)
