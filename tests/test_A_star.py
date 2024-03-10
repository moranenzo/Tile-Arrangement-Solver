from grid import Grid
from graph import Graph

grille_test= Grid(3,3,[[1,2,3],[5,4,6],[8,9,7]])
test_A_star = Graph(grille_test.generate())

for n in test_A_star.nodes:
    node= Grid(grille_test.m, grille_test.n, [ list(k) for k in n] )
    test_A_star.graph[n]=[Grid(2,2,neighbor) for neighbor in node.neighbors()]
test_A_star.A_star(grille_test,grille_sorted)