import os
from src.grid import Grid
from src.graph import Graph

def main():
    """
    Main function for testing and running search algorithms on a grid.
    """
    # Initialize a grid from a file
    data_path = os.path.join("input", "grid0.in")
    print(f"Loading grid from file: {data_path}")
    grid = Grid.grid_from_file(data_path)
    print("Loaded grid:")
    print(grid)

    # Define the target (sorted) configuration for comparison
    m, n = grid.m, grid.n
    target_state = [[i * n + j + 1 for j in range(n)] for i in range(m)]
    target_grid = Grid(m, n, target_state)
    print("Target grid configuration:")
    print(target_grid)

    # Initialize graph and generate nodes
    graph = Graph(grid.generate())
    graph.graph = {node: Grid(m, n, [list(row) for row in node]).neighbors() for node in graph.nodes}

    # Run BFS algorithm
    print("\nRunning BFS to find the shortest path to the target configuration...")
    bfs_path = graph.bfs(grid, target_grid)
    if bfs_path:
        print("BFS found a path:")
        print(bfs_path)
    else:
        print("BFS could not find a path to the target.")

    # Run Improved BFS algorithm
    print("\nRunning Improved BFS to find the shortest path to the target configuration...")
    bfs_improved_path = graph.bfs_improved(grid, target_grid)
    if bfs_improved_path:
        print("Improved BFS found a path:")
        print(bfs_improved_path)
    else:
        print("Improved BFS could not find a path to the target.")

    # Run A* algorithm
    print("\nRunning A* algorithm to find the optimal path to the target configuration...")
    a_star_path = graph.a_star(grid, target_grid)
    if a_star_path:
        print("A* found a path:")
        print(a_star_path)
    else:
        print("A* could not find a path to the target.")

if __name__ == "__main__":
    main()
