"""
This module defines the Graph class for undirected graphs represented by adjacency lists.
"""

from grid import Grid


class Graph:
    """
    Represents an undirected graph using adjacency lists.

    Attributes:
    -----------
    nodes : list
        A list of nodes, which can be any immutable type (e.g., integer, string).
    graph : dict
        A dictionary storing adjacency lists, where graph[node] = [neighbor1, neighbor2, ...].
    nb_nodes : int
        The number of nodes in the graph.
    nb_edges : int
        The number of edges in the graph.
    edges : list[tuple]
        A list of all edges in the graph.
    """

    def __init__(self, nodes=None):
        """
        Initializes the graph with a set of nodes and no edges.

        Parameters:
        -----------
        nodes : list, optional
            A list of nodes. Default is an empty list.
        """
        self.nodes = nodes if nodes is not None else []
        self.graph = {node: [] for node in self.nodes}
        self.nb_nodes = len(self.nodes)
        self.nb_edges = 0
        self.edges = []

    def __str__(self):
        """
        Returns a string representation of the graph with each node and its neighbors.
        """
        if not self.graph:
            return "The graph is empty"
        output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
        for node, neighbors in self.graph.items():
            output += f"{node} --> {neighbors}\n"
        return output

    def __repr__(self):
        """
        Returns a summary of the graph showing the number of nodes and edges.
        """
        return f"<Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an undirected edge between two nodes. If a node does not exist, it is added.

        Parameters:
        -----------
        node1, node2 : Any immutable type
            The two nodes to connect by an edge.
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
        Finds the shortest path from src to dst using Breadth-First Search (BFS).

        Parameters:
        -----------
        src : Grid
            The source grid configuration.
        dst : Grid
            The destination grid configuration.

        Returns:
        --------
        list[tuple] | None
            A list representing the shortest path from src to dst, or None if no path exists.
        """
        queue = [src]
        parent_map = {src.to_tuple(): None}
        found_path = False

        while queue and not found_path:
            current = queue.pop(0)
            if current.to_tuple() == dst.to_tuple():
                found_path = True
            else:
                for neighbor in self.graph[current.to_tuple()]:
                    if neighbor.to_tuple() not in parent_map:
                        queue.append(neighbor)
                        parent_map[neighbor.to_tuple()] = current

        if not found_path:
            return None

        path = []
        step = dst
        while step:
            path.insert(0, step.to_tuple())
            step = parent_map[step.to_tuple()]

        return path

    def bfs_improved(self, src, dst):
        """
        An optimized BFS that dynamically generates neighbors.

        Parameters:
        -----------
        src : Grid
            The source grid configuration.
        dst : Grid
            The destination grid configuration.

        Returns:
        --------
        list[tuple] | None
            A list representing the shortest path from src to dst, or None if no path exists.
        """
        queue = [src]
        parent_map = {src.to_tuple(): None}
        found_path = False

        while queue and not found_path:
            current = queue.pop(0)
            if current.to_tuple() == dst.to_tuple():
                found_path = True
            else:
                for neighbor_state in current.neighbors():
                    neighbor = Grid(src.m, src.n, neighbor_state)
                    if neighbor.to_tuple() not in parent_map:
                        queue.append(neighbor)
                        parent_map[neighbor.to_tuple()] = current

        if not found_path:
            return None

        path = []
        step = dst
        while step:
            path.insert(0, step.to_tuple())
            step = parent_map[step.to_tuple()]

        return path

    def a_star(self, src, dst):
        """
        Finds the shortest path from src to dst using the A* algorithm with Manhattan distance.

        Parameters:
        -----------
        src : Grid
            The source grid configuration.
        dst : Grid
            The destination grid configuration.

        Returns:
        --------
        list[tuple]
            A list representing the optimal path from src to dst.
        """
        open_list = [(src, 0, src.manhattan_distance(dst), None)]
        closed_list = []
        path = []

        while open_list:
            current, g_cost, _, parent = open_list.pop(0)
            if current.to_tuple() == dst.to_tuple():
                while parent:
                    path.insert(0, current.to_tuple())
                    current = parent
                    parent = next((node[3] for node in closed_list if node[0] == current), None)
                return path

            closed_list.append((current, g_cost, g_cost + current.manhattan_distance(dst), parent))

            for neighbor_state in current.neighbors():
                neighbor = Grid(src.m, src.n, neighbor_state)
                neighbor_tuple = neighbor.to_tuple()
                if any(neighbor_tuple == n[0].to_tuple() and g_cost < n[1] for n in closed_list):
                    continue

                if not any(neighbor_tuple == n[0].to_tuple() for n in open_list):
                    open_list.append((neighbor, g_cost + 1, g_cost + 1 + neighbor.manhattan_distance(dst), current))
                    open_list.sort(key=lambda x: x[2])

        return path

    @classmethod
    def from_file(cls, file_name):
        """
        Reads a text file and returns a Graph object.

        The file format should be:
            - First line: "n m" where n is the number of nodes, m is the number of edges
            - Next m lines: "node1 node2" specifying each edge

        Parameters:
        -----------
        file_name : str
            Path to the file containing the graph.

        Returns:
        --------
        Graph : A Graph object initialized with the file data.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n + 1))
            for _ in range(m):
                node1, node2 = map(int, file.readline().split())
                graph.add_edge(node1, node2)
        return graph
