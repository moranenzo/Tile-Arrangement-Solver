from grid import Grid
from graph import Graph

# Define a test grid for BFS algorithm
test_grid_2x2 = Grid(2, 2, [[1, 2], [4, 3]])
sorted_grid_2x2 = Grid(2, 2, [[1, 2], [3, 4]])

# Initialize the graph based on the generated nodes of test_grid_2x2
graph_bfs_2x2 = Graph(test_grid_2x2.generate())

# Populate the graph's adjacency list with neighboring nodes
for node_tuple in graph_bfs_2x2.nodes:
    node = Grid(test_grid_2x2.m, test_grid_2x2.n, [list(row) for row in node_tuple])
    graph_bfs_2x2.graph[node_tuple] = [Grid(2, 2, neighbor) for neighbor in node.neighbors()]

# Run BFS algorithm to find the solution from test_grid_2x2 to sorted_grid_2x2
path_bfs_2x2 = graph_bfs_2x2.bfs(test_grid_2x2, sorted_grid_2x2)
print("BFS Path (2x2 Grid):", path_bfs_2x2)

# Define another test grid for BFS with different dimensions
test_grid_3x2 = Grid(3, 2, [[1, 6], [2, 3], [4, 5]])
sorted_grid_3x2 = Grid(3, 2, [[1, 2], [3, 4], [5, 6]])

# Initialize the graph based on the generated nodes of test_grid_3x2
graph_bfs_3x2 = Graph(test_grid_3x2.generate())

# Populate the graph's adjacency list with neighboring nodes
for node_tuple in graph_bfs_3x2.nodes:
    node = Grid(test_grid_3x2.m, test_grid_3x2.n, [list(row) for row in node_tuple])
    graph_bfs_3x2.graph[node_tuple] = [Grid(3, 2, neighbor) for neighbor in node.neighbors()]

# Run BFS and improved BFS algorithms to find the solution from test_grid_3x2 to sorted_grid_3x2
path_bfs_3x2 = graph_bfs_3x2.bfs(test_grid_3x2, sorted_grid_3x2)
print("BFS Path (3x2 Grid):", path_bfs_3x2)

path_bfs_improved_3x2 = graph_bfs_3x2.bfs_improved(test_grid_3x2, sorted_grid_3x2)
print("Improved BFS Path (3x2 Grid):", path_bfs_improved_3x2)
