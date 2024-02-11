import sys
sys.path.append("swap_puzzle/")

from grid import Grid
from graph import Graph

g = Grid(2, 3)
print(g)

data_path = "/home/onyxia/ensae-prog24/input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)



# Création du graph

'Ici src est la grille source'
m = src.m
n = src.n

dst = [[i*n + j + 1 for j in range(n)] for i in range(n)]

graph = Graph(Grid(m,n).generate())

graph.graph = dict([(n, n.neighbors()) for n in graph.nodes])

graph.bfs(src, dst)
