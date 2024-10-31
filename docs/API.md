<h1>API Documentation</h1>

<h2>Overview</h2>
<p>This document provides an in-depth overview of the classes, methods, and functions used in the Tile Arrangement Solver project. The project includes core modules to manage grid states, execute pathfinding algorithms, and support an interactive tile puzzle game. Each module’s functionality is described in detail below.</p>

<h2>Grid Class (from grid.py)</h2>
<p>Represents the grid in the tile puzzle.</p>

<ul>
  <li><strong>Attributes</strong>
    <ul>
      <li><code>m</code> (int): Number of rows in the grid.</li>
      <li><code>n</code> (int): Number of columns in the grid.</li>
      <li><code>state</code> (list[list[int]]): Current state of the grid, where <code>state[i][j]</code> holds the tile at row <code>i</code>, column <code>j</code>.</li>
    </ul>
  </li>
  <li><strong>Methods</strong>
    <ul>
      <li><code>__init__(self, m, n, initial_state=None)</code>: Initializes a grid of size <code>m x n</code>. Optionally accepts an <code>initial_state</code> list to define the grid’s starting configuration.</li>
      <li><code>__str__(self)</code>: Returns a formatted string representation of the grid state.</li>
      <li><code>__repr__(self)</code>: Provides a concise string summary with grid dimensions.</li>
      <li><code>display(self)</code>: Renders the grid state in a graphical window using Pygame.</li>
      <li><code>to_tuple(self)</code>: Converts the grid state to a tuple format, making it suitable for hashing in graph traversal.</li>
      <li><code>generate(self)</code>: Generates all unique grid configurations for a given dimension.</li>
      <li><code>neighbors(self)</code>: Returns a list of neighboring grids, each one move away from the current configuration.</li>
      <li><code>is_sorted(self)</code>: Checks if the current grid state is sorted in ascending order.</li>
      <li><code>is_adjacent(self, cell1, cell2)</code>: Verifies if two cells are adjacent, allowing or disallowing swaps.</li>
      <li><code>swap(self, cell1, cell2)</code>: Swaps two cells if valid, raising an exception if the swap is not permitted.</li>
      <li><code>swap_seq(self, cell_pairs)</code>: Performs a sequence of swaps on the grid.</li>
      <li><code>manhattan_distance(self, other)</code>: Calculates the Manhattan distance from the current grid to another grid, used for heuristic calculation in pathfinding.</li>
      <li><code>from_file(cls, file_name)</code>: Class method to initialize a grid from a file.</li>
    </ul>
  </li>
</ul>

<h2>Graph Class (from graph.py)</h2>
<p>Represents the graph structure used to solve tile configurations via pathfinding algorithms.</p>

<ul>
  <li><strong>Attributes</strong>
    <ul>
      <li><code>nodes</code> (list): List of nodes representing unique grid configurations.</li>
      <li><code>graph</code> (dict): Adjacency list dictionary where each entry <code>graph[node]</code> holds a list of neighbors.</li>
      <li><code>nb_nodes</code> (int): Total count of nodes in the graph.</li>
      <li><code>nb_edges</code> (int): Total count of edges in the graph.</li>
      <li><code>edges</code> (list[tuple]): List of all edges in the graph.</li>
    </ul>
  </li>
  <li><strong>Methods</strong>
    <ul>
      <li><code>__init__(self, nodes=None)</code>: Initializes the graph with an optional list of nodes.</li>
      <li><code>__str__(self)</code>: Returns a formatted string representation of the adjacency list for each node.</li>
      <li><code>__repr__(self)</code>: Provides a summary of the graph, including node and edge counts.</li>
      <li><code>add_edge(self, node1, node2)</code>: Adds an undirected edge between two nodes, creating nodes if they do not exist.</li>
      <li><code>bfs(self, src, dst)</code>: Performs a Breadth-First Search (BFS) to find the shortest path from the source grid to the target grid.</li>
      <li><code>bfs_improved(self, src, dst)</code>: Optimized BFS that generates nodes dynamically to save memory.</li>
      <li><code>a_star(self, src, dst)</code>: Executes the A* algorithm, using Manhattan distance as the heuristic for finding the optimal path.</li>
      <li><code>from_file(cls, file_name)</code>: Loads a graph from a file formatted with node and edge information.</li>
    </ul>
  </li>
</ul>

<h2>Solver Class (from solver.py)</h2>
<p>Provides methods for finding the solution path for the tile arrangement puzzle.</p>

<ul>
  <li><strong>Methods</strong>
    <ul>
      <li><code>get_solution(self)</code>: Computes the sequence of moves required to arrange the tiles into the target configuration, returning a list of swap operations in the format <code>[ ((i1, j1), (i2, j2)), ... ]</code>.</li>
    </ul>
  </li>
</ul>

<h2>Game Functions (from game.py)</h2>
<p>Functions to manage the graphical interface of the tile puzzle game, implemented using Pygame.</p>

<ul>
  <li><strong>Functions</strong>
    <ul>
      <li><code>shuffle_grid(size)</code>: Generates a shuffled grid of tiles for a given size.</li>
      <li><code>draw_grid(grid, cell_size, font)</code>: Draws the current grid on the Pygame screen, filling each cell with the appropriate tile number.</li>
      <li><code>swap_cells(grid, y1, x1, y2, x2)</code>: Swaps the values between two cells in the grid.</li>
      <li><code>main(size, cell_size)</code>: Main function handling gameplay loop and user interaction in the Pygame window.</li>
      <li><code>show_win_screen(moves)</code>: Displays a win screen upon puzzle completion, including the total number of moves made.</li>
      <li><code>start_game(difficulty)</code>: Starts the game with a selected difficulty level (e.g., Easy, Medium, Hard).</li>
      <li><code>show_difficulty_select()</code>: Displays a screen allowing the player to select the difficulty level and returns the chosen level.</li>
    </ul>
  </li>
</ul>

<h2>Solver Script (from main.py)</h2>
<p>The <code>main.py</code> script runs the algorithms (BFS, Improved BFS, A*) on a loaded grid to test and display their effectiveness in finding the shortest solution path. <strong>This script is intended for algorithm testing and pathfinding solutions rather than game interaction</strong>.</p>

<ul>
  <li><strong>Function</strong>
    <ul>
      <li><code>main()</code>: Loads a grid from an input file, defines the target grid configuration, and initializes a graph based on the grid's permutations. It executes three algorithms—BFS, Improved BFS, and A*—to find the path from the initial to the target configuration. The paths found are displayed in the console for analysis and comparison.</li>
    </ul>
  </li>
</ul>

<p><strong>Execution</strong>:</p>
<p>To execute the <code>main.py</code> script:</p>
<pre><code>python main.py</code></pre>

<h2>Game Launch Script (from run_game.py)</h2>
<p>The <code>run_game.py</code> script is the primary entry point for launching the interactive tile puzzle game. It initializes Pygame, prompts the user to choose a difficulty level, and then starts the puzzle game with the chosen difficulty.</p>

<ul>
  <li><strong>Function</strong>
    <ul>
      <li><code>main()</code>: The main function of <code>run_game.py</code> initializes Pygame, displays the difficulty selection screen, and begins the game based on the user’s selection.</li>
    </ul>
  </li>
</ul>

<p><strong>Execution</strong>:</p>
<p>To start the interactive game:</p>
<pre><code>python run_game.py</code></pre>

<h2>Example Usage</h2>

<p><strong>Run Interactive Game</strong>: Use <code>run_game.py</code> to start the game with a GUI where users can manually solve the puzzle or try different configurations.</p>
<pre><code>python run_game.py</code></pre>

<p><strong>Run Solver Algorithms</strong>: Use <code>main.py</code> to test and evaluate the BFS, Improved BFS, and A* algorithms on preconfigured grids.</p>
<pre><code>python main.py</code></pre>

<h2>Notes for Developers</h2>
<p>Both <code>main.py</code> and <code>run_game.py</code> scripts serve distinct purposes within the project:</p>
<ul>
  <li><strong><code>main.py</code></strong> is for testing and comparing algorithm efficiency in solving the puzzle.</li>
  <li><strong><code>run_game.py</code></strong> provides the interactive puzzle game, where users can manually engage with the puzzle using Pygame’s interface.</li>
</ul>
