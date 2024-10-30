"""
This is the graph module. It contains a minimalistic Graph class.
"""
from grid import Grid


class Graph:
    """
    A class representing undirected graphs as adjacency lists.

    Attributes:
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges.

        Parameters:
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self):
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters:
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.

        Parameters:
        -----------
        src: Grid
            The source node.
        dst: Grid
            The destination node.

        Output:
        -------
        path: list[tuple] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """

        # Initialisation
        graph = self.graph
        queue = [src]
        father = {}
        found_path = False

        # On détermine un chemin reliant src et dst
        for node in queue:
            father[node.hash()] = None

        while queue and not found_path:
            current = queue.pop(0)
            if current.hash() == dst.hash():
                found_path = True  # permet de sortir de la boucle while

            else:
                neighbors = graph[current.hash()]  # liste des voisins de current

                for neighbor in neighbors:

                    # On vérifie que neighbor n'a pas déjà été traité (i.e. visité ou ajouté à la file)
                    if (neighbor.hash() not in father) and (neighbor not in queue):
                        queue.append(neighbor)
                        father[neighbor.hash()] = current

        # On vérifie qu'un chemin entre src et dst a bien été trouvé
        if not found_path:
            return None

        # Construction du chemin reliant src et dst à partir du dico father
        child = dst
        chemin = []
        while child:
            chemin = [child.hash()] + chemin
            child = father[child.hash()]

        return chemin

    def bfs_improved(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.

        Parameters:
        -----------
        src: Grid
            The source node.
        dst: Grid
            The destination node.

        Output:
        -------
        path: list[tuple] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """

        # Initialisation
        queue = [src]
        father = {}
        found_path = False

        # On détermine un chemin reliant src et dst
        for node in queue:
            father[node.hash()] = None

        while queue and not found_path:
            current = queue.pop(0)
            if current.hash() == dst.hash():
                found_path = True

            else:
                matrice_neighbors = current.neighbors()
                for matrice_neighbor in matrice_neighbors:
                    # Construction de la grid voisine à current
                    neighbor = Grid(src.m, src.n, matrice_neighbor)

                    # On vérifie que neighbor n'a pas déjà été traité (i.e. visité ou ajouté à la file)
                    if (neighbor.hash() not in father) and (neighbor not in queue):
                        queue.append(neighbor)
                        father[neighbor.hash()] = current

        # On vérifie qu'un chemin entre src et dst a bien été trouvé
        if not found_path:
            return None

        # Construction du chemin reliant src et dst à partir du dico father
        child = dst
        chemin = []
        while child:
            chemin = [child.hash()] + chemin
            child = father[child.hash()]

        return chemin


    def A_star(self, src, dst):
        open_list = [(src, 0, src.manhattan_dist(dst), [])]  # içi la liste source n'a pas de père.
        closed_list = []
        path = []
        # On lance une première fois l'algorithme afin d'éviter une erreur au niveau de if neighbor != open_list[0][3].state:
        if src.state != dst.state:
            closed_list.append(open_list[0])
            neighbors = open_list[0][0].neighbors()
            for neighbor in neighbors:
                open_list.append((Grid(src.m, src.n, neighbor), open_list[0][1]+1, open_list[0][1]+1+Grid(src.m, src.n, neighbor).manhattan_dist(dst), open_list[0][0]))
            open_list.pop(0)
            open_list.sort(key=lambda x: x[2])
              
        while open_list:
            if open_list[0][0].state == dst.state:       
                path.append(dst.hash())
                father = open_list[0][3]
                while father:  # Permet de remonter jusqu'a la grille source qui est la seule à ne pas avoir de père.
                    
                    for acn in closed_list:  # acn pour already closed nodes.
                            
                        if (father != []) and (acn[0].state == father.state):
                            open_list[0] = acn
                            path = [acn[0].hash()] + path
                            father = open_list[0][3]
                open_list = []  # Permet de sortir de la première boucle while.
            else:
                icl = False  # icl pour in closed list.
                for i in range(0, len(closed_list)): 
                    if closed_list[i][0].state == open_list[0][0].state:
                        icl = True
                        if closed_list[i][2] > open_list[0][2]:  # Si  l'heuristique du noeud déjà visité est meilleure alors on le remplace  dans la liste afin d'obtenir le meilleur père possible. 
                            closed_list[i] = open_list[0]

                            neighbors = open_list[0][0].neighbors()
                            for neighbor in neighbors:
                                open_list.append((Grid(src.m, src.n, neighbor), open_list[0][1]+1, open_list[0][1]+1+Grid(src.m, src.n, neighbor).manhattan_dist(dst), open_list[0][0]))  
                                # on définit le nouveau coût de ses voisins ainsi que la nouvelle heuristique.
                        open_list.pop(0)
                        open_list.sort(key=lambda x: x[2])  # Permet de trier la grille selon les heuristiques.
                        
                if not icl:  # Si icl vaut True on a déjà effectué les opérations nécessaires.
                    closed_list.append(open_list[0])
                    neighbors = open_list[0][0].neighbors()
                    for neighbor in neighbors:
                         if neighbor != open_list[0][3].state: 
                            """
                            On n' implémente pas le père de la grille comme un fils afin d'éviter une boucle infinie
                            pour les petites grilles dans la création du chemin vers destination 
                            """
                            open_list.append((Grid(src.m, src.n, neighbor), open_list[0][1]+1, open_list[0][1]+1+Grid(src.m, src.n, neighbor).manhattan_dist(dst), open_list[0][0]))
                    open_list.pop(0)
                    open_list.sort(key=lambda x: x[2])
        return path

    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format:
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters:
        -----------
        file_name: str
            The name of the file

        Outputs:
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2)  # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

