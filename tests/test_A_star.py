from grid import Grid
from graph import Graph

# Define a test grid for A* algorithm
test_grid = Grid(3, 3, [[1, 2, 3], [5, 4, 6], [8, 9, 7]])
sorted_grid = Grid(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize the graph based on the generated nodes of test_grid
graph_a_star = Graph(test_grid.generate())

# Populate the graph's adjacency list with neighboring nodes for A* algorithm
for node_tuple in graph_a_star.nodes:
    node = Grid(test_grid.m, test_grid.n, [list(row) for row in node_tuple])
    graph_a_star.graph[node_tuple] = [Grid(3, 3, neighbor) for neighbor in node.neighbors()]

# Run A* algorithm to find the solution from test_grid to sorted_grid
path_a_star = graph_a_star.a_star(test_grid, sorted_grid)
print("A* Path:", path_a_star)

# Define another test grid for BFS algorithm
test_grid_bfs = Grid(3, 2, [[1, 6], [2, 3], [4, 5]])
sorted_grid_bfs = Grid(3, 2, [[1, 2], [3, 4], [5, 6]])

# Initialize the graph based on the generated nodes of test_grid_bfs
graph_bfs = Graph(test_grid_bfs.generate())

# Populate the graph's adjacency list with neighboring nodes for BFS algorithm
for node_tuple in graph_bfs.nodes:
    node = Grid(test_grid_bfs.m, test_grid_bfs.n, [list(row) for row in node_tuple])
    graph_bfs.graph[node_tuple] = [Grid(3, 2, neighbor) for neighbor in node.neighbors()]

# Run BFS algorithm to find the solution from test_grid_bfs to sorted_grid_bfs
path_bfs = graph_bfs.bfs(test_grid_bfs, sorted_grid_bfs)
print("BFS Path:", path_bfs)
