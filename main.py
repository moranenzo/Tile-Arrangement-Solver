# main.py
import os
from src.grid import Grid
from src.graph import Graph

# Initialisation d'une grille de dimensions 2x3
g = Grid(2, 3)
print("Grille initiale vide :")
print(g)

# Chemin vers le fichier d'entrée
data_path = os.path.join("input", "grid0.in")
print(f"Chemin du fichier d'entrée : {data_path}")

# Chargement de la grille depuis le fichier
g = Grid.grid_from_file(data_path)
print("Grille chargée depuis le fichier :")
print(g)

# Création et configuration du graphe
print("\nCréation du graphe à partir de la grille.")
m, n = g.m, g.n
destination = [[i * n + j + 1 for j in range(n)] for i in range(m)]
graph = Graph(g.generate())

# Construire le graphe en ajoutant les voisins de chaque nœud
graph.graph = {node: node.neighbors() for node in graph.nodes}

# Recherche d'un chemin entre l'état source et l'état cible
print("\nRecherche du chemin optimal à l'aide de BFS.")
graph.bfs(g, destination)