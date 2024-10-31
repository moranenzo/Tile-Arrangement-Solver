<h1>PY-Tile-Arrangement-Solver</h1>

<h2>Overview</h2>
<p>PY-Tile-Arrangement-Solver is a Python project designed to solve a tile rearrangement puzzle on a grid of dimensions <code>m x n</code>. The objective is to find the shortest sequence of moves to arrange tiles in a specified order, with the final arrangement showing sequential numbers across each row. This project implements multiple graph traversal algorithms, including BFS, an improved BFS, and A*, to optimize the solution. A graphical interface created with Pygame allows users to interact with the puzzle and experiment with different configurations.</p>

<h2>Features</h2>
<ul>
  <li><strong>Algorithms</strong>: The project explores multiple algorithms for finding the optimal solution:
    <ul>
      <li><strong>Breadth-First Search (BFS)</strong> for a basic breadth-first search through grid states.</li>
      <li><strong>Improved BFS</strong> which dynamically generates nodes, reducing memory usage.</li>
      <li><strong>A*</strong> with Manhattan distance heuristic for faster and more informed searches.</li>
    </ul>
  </li>
  <li><strong>User Interface</strong>: An interactive graphical interface built with Pygame enables users to manually solve the puzzle or observe the automated solution.</li>
  <li><strong>Difficulty Levels</strong>: Puzzle difficulty can be scaled by grid size, which influences the number of tiles and complexity.</li>
</ul>

<h2>Project Structure</h2>
<pre>
PY-Tile-Arrangement-Solver/  
├── docs/                        # Project documentation
│   ├── API.md                   # API documentation of classes and methods
│   └── report.md                # Detailed report on algorithms and complexity analysis
│  
├── input/                       # Test input files for different grid configurations
│   ├── grid0.in
│   ├── grid1.in
│   └── ...                      # Additional test files
│
├── src/                         # Contains the main source code
│   ├── game.py
│   ├── graph.py                 # Graph class for BFS and A*
│   ├── grid.py                  # Grid class for tile manipulations
│   └── solver.py                # Solver class implementing BFS, Improved BFS, and A*
│
├── tests/                       # Unit tests for each module
│   ├── test_A_star.py           # Tests for A*
│   ├── test_bfs.py              # Tests for BFS
│   ├── test_bfs_improved.py     # Tests for Improved BFS
│   ├── test_grid_from_file.py   # Tests for Grid functions
│   ├── test_is_sorted.py        # Tests for sorted state detection
│   └── test_swap.py             # Tests for swap operations in the grid
│
├── main.py                      # Script to run algorithms for solving and testing solutions
├── run_game.py                  # Main script to launch the interactive game
├── README.md                    # Project overview and instructions (this file)
└── requirements.txt             # Python packages necessary for the proper functioning of the project.
</pre>

<h2>Algorithms</h2>

<h3>Breadth-First Search (BFS)</h3>
<ul>
  <li><strong>Description</strong>: A standard BFS algorithm that explores all neighbors of a node before moving on. Each grid state is considered a node, and valid moves form edges between nodes.</li>
  <li><strong>Complexity</strong>: <code>O(m * n * (m * n)!)</code>, as BFS explores all possible configurations of the grid.</li>
</ul>

<h3>Improved BFS</h3>
<ul>
  <li><strong>Description</strong>: Optimized to generate only necessary nodes, significantly reducing memory usage.</li>
  <li><strong>Complexity</strong>: Equivalent to BFS in worst-case scenarios, but faster in practice due to reduced nodes.</li>
</ul>

<h3>A* Search</h3>
<ul>
  <li><strong>Description</strong>: Uses Manhattan distance as a heuristic for faster and informed traversal.</li>
  <li><strong>Complexity</strong>: <code>O(m * n * log((m * n)!))</code>, dominated by sorting and list operations.</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/moranenzo/PY-Tile-Arrangement-Solver.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd PY-Tile-Arrangement-Solver</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<h3>Run the Interactive Game</h3>
<p>To start the interactive puzzle game with a graphical interface:</p>
<pre><code>python run_game.py</code></pre>
<p>This will launch the game interface where you can choose a difficulty level and interact with the puzzle.</p>

<h3>Run the Solver Algorithms</h3>
<p>To execute the script focused on algorithm testing and pathfinding solutions:</p>
<pre><code>python main.py</code></pre>
<p>This script loads a grid from an input file, applies different solving algorithms (BFS, Improved BFS, A*), and displays the paths found for each algorithm in the console.</p>

<h2>Testing</h2>
<p>Run unit tests for each module with:</p>
<pre><code>python -m unittest discover -s tests</code></pre>

<h2>Future Improvements</h2>
<ul>
  <li>Experiment with additional heuristics for A*.</li>
  <li>Add scoring to track user performance.</li>
  <li>Integrate custom grid options for varied gameplay.</li>
</ul>
