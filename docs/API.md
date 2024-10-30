<h1>API Documentation</h1>

<h2>Overview</h2>
<p>This document provides a detailed description of the classes and methods used in the PY-Tile-Arrangement-Solver project. This project solves a tile arrangement puzzle on a grid, implementing multiple algorithms (BFS, Improved BFS, A*) to find the optimal arrangement. Each class and method are outlined below, along with parameters and return values.</p>

<h2>Classes and Methods</h2>

<h3>1. <code>Grid</code> Class</h3>
<p>Represents the tile grid used in the puzzle.</p>

<ul>
  <li><strong>Attributes</strong>:
    <ul>
      <li><code>m</code> (int): Number of rows in the grid.</li>
      <li><code>n</code> (int): Number of columns in the grid.</li>
      <li><code>state</code> (list of lists): Current arrangement of tiles in the grid, represented as a list of lists.</li>
    </ul>
  </li>
  <li><strong>Methods</strong>:
    <ul>
      <li><code>__init__(self, m, n)</code>: Initializes a new grid of size <code>m x n</code>.
        <ul>
          <li><strong>Parameters</strong>: <code>m</code> (int), <code>n</code> (int)</li>
        </ul>
      </li>
      <li><code>__str__(self)</code>: Returns the grid state as a formatted string.
      </li>
      <li><code>__repr__(self)</code>: Returns a concise representation of the grid dimensions.
      </li>
      <li><code>display(self)</code>: Graphically displays the grid state using Matplotlib.
      </li>
      <li><code>to_tuple(self)</code>: Converts the grid state to an immutable tuple format.
        <ul>
          <li><strong>Parameters</strong>: <code>cell1</code>, <code>cell2</code> (tuple): Coordinates <code>(i, j)</code> of the cells to swap.</li>
          <li><strong>Returns</strong>: None</li>
        </ul>
      </li>
      <li><code>swap(self, cell1, cell2)</code>: Swaps the tiles at the specified cells if valid.
        <ul>
          <li><strong>Parameters</strong>: <code>cell1</code>, <code>cell2</code> (tuple): Coordinates <code>(i, j)</code> of the cells to swap.</li>
          <li><strong>Returns</strong>: None</li>
        </ul>
      </li>
      <li><code>swap_seq(self, swap_list)</code>: Performs a sequence of swaps on the grid.
        <ul>
          <li><strong>Parameters</strong>: <code>swap_list</code> (list of tuples): List of tuples representing swaps to perform.</li>
          <li><strong>Returns</strong>: None</li>
        </ul>
      </li>
      <li><code>is_sorted(self)</code>: Checks if the tiles in the grid are in the target order.
        <ul>
          <li><strong>Returns</strong>: Boolean indicating whether the grid is sorted.</li>
        </ul>
      </li>
      <li><code>grid_from_file(cls, file_name)</code>: Loads a grid from a specified file.
        <ul>
          <li><strong>Parameters</strong>: <code>file_name</code> (str): Path to the file containing grid layout.</li>
          <li><strong>Returns</strong>: Instance of <code>Grid</code> class.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h3>2. <code>Graph</code> Class</h3>
<p>Represents the graph structure for grid traversal algorithms.</p>

<ul>
  <li><strong>Attributes</strong>:
    <ul>
      <li><code>graph</code> (dict): Adjacency list representing the connections between grid states.</li>
      <li><code>nodes</code> (set): Set of nodes in the graph.</li>
    </ul>
  </li>
  <li><strong>Methods</strong>:
    <ul>
      <li><code>__init__(self, nodes)</code>: Initializes a graph with given nodes.
        <ul>
          <li><strong>Parameters</strong>: <code>nodes</code> (list): List of nodes to initialize the graph.</li>
        </ul>
      </li>
      <li><code>add_edge(self, node1, node2)</code>: Adds an edge between two nodes.
        <ul>
          <li><strong>Parameters</strong>: <code>node1</code>, <code>node2</code>: Nodes to connect.</li>
        </ul>
      </li>
      <li><code>bfs(self, src, dst)</code>: Performs Breadth-First Search from source to destination nodes.
        <ul>
          <li><strong>Parameters</strong>: <code>src</code>, <code>dst</code>: Start and end nodes for BFS.</li>
          <li><strong>Returns</strong>: List of moves or <code>None</code> if no path exists.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h3>3. <code>Solver</code> Class</h3>
<p>Implements the core algorithms for solving the tile arrangement puzzle.</p>

<ul>
  <li><code>bfs(self, graph, src, dst)</code>: Basic BFS traversal to find the shortest path.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>graph</code> (<code>Graph</code>): Graph object for traversal.</li>
          <li><code>src</code> (<code>Grid</code>): Starting grid configuration.</li>
          <li><code>dst</code> (<code>Grid</code>): Target grid configuration.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: List of moves to reach <code>dst</code> from <code>src</code> or <code>None</code> if no path exists.</li>
    </ul>
  </li>
  
  <li><code>bfs_improved(self, src, dst)</code>: An optimized BFS that dynamically generates nodes.
    <ul>
      <li><strong>Parameters</strong>: <code>src</code>, <code>dst</code> (<code>Grid</code>): Starting and target grid configurations.</li>
      <li><strong>Returns</strong>: List of moves for the optimal path or <code>None</code> if no path exists.</li>
    </ul>
  </li>
  
  <li><code>a_star(self, src, dst)</code>: A* search algorithm using Manhattan distance heuristic.
    <ul>
      <li><strong>Parameters</strong>: <code>src</code>, <code>dst</code> (<code>Grid</code>): Starting and target grid configurations.</li>
      <li><strong>Returns</strong>: List of moves along the optimal path or <code>None</code> if no path exists.</li>
    </ul>
  </li>
</ul>

<h2>Example Usage</h2>

<pre><code># Initialize a 3x3 grid
grid = Grid(3, 3)

# Perform a swap between cells (0, 0) and (0, 1)
grid.swap((0, 0), (0, 1))

# Load a grid from file
grid_from_file = Grid.grid_from_file("input/grid0.in")

# Solve using BFS
solver = Solver()
solution_path = solver.bfs(graph, grid, target_grid)
</code></pre>

<p>This <code>API.md</code> document provides a concise yet thorough overview of the functionality, parameters, and outputs of each component in the project, facilitating ease of use and reference for developers and collaborators.</p>
