from grid import Grid
from graph import Graph

grille_test= Grid(2,2,[[1,2],[4,3]])
test_bfs=Graph(grille_test.generate())
grille_sorted= Grid(2,2,[[1,2],[3,4]])

for n in test_bfs.nodes:
    node= Grid(grille_test.m, grille_test.n, [ list(k) for k in n] )
    test_bfs.graph[n]=[Grid(2,2,neighbor) for neighbor in node.neighbors()]
test_bfs.bfs(grille_test,grille_sorted) 

grille_test= Grid(3,2,[[1,6],[2,3],[4,5]])
test_bfs=Graph(grille_test.generate())
grille_sorted= Grid(3,2,[[1,2],[3,4],[5,6]])


for n in test_bfs.nodes:
    node= Grid(grille_test.m, grille_test.n, [ list(k) for k in n] )
    test_bfs.graph[n]=[Grid(3,2,neighbor) for neighbor in node.neighbors()]
test_bfs.bfs(grille_test,grille_sorted) 
test_bfs.bfs_improved(grille_test,grille_sorted)