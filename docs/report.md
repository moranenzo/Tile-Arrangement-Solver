<h1>Programming Project Report</h1>

<p><strong>Authors</strong>: Enzo Moran and Alexis Dahlen<br>
<strong>Course</strong>: Algorithms and Programming | ENSAE Paris | Institut Polytechnique de Paris<br>
<strong>Year</strong>: 2024</p>

<h2>Introduction</h2>
<p>This project addresses the problem of reorganizing a grid of dimensions <code>m x n</code>, in which it is required to align numbered tiles in a specific order. The objective is to find the shortest sequence of moves to arrange the tiles so that each row contains a consecutive sequence of numbers. The project focuses on the implementation and evaluation of several graph traversal algorithms to efficiently solve this puzzle, while also offering an interactive user interface to experiment with the solution.</p>

<h2>Algorithm Analysis</h2>

<h3>1. BFS Algorithm (Breadth-First Search)</h3>
<p>The BFS algorithm enables a breadth-first traversal of a graph, ideal for exploring solutions level by level. Each grid state is modeled as a node in the graph, and a valid move constitutes an edge connecting two nodes.</p>
<ul>
  <li><strong>Description</strong>: The algorithm uses a queue to examine each neighbor of a node before progressing to farther nodes. For each grid state, BFS checks whether the state has already been visited.</li>
  <li><strong>Optimization</strong>: Visited nodes are managed through a dictionary (<code>father</code>), where each node is mapped with its previous state.</li>
  <li><strong>Complexity</strong>: In the worst case, BFS has a complexity of <code>O(m * n * (m * n)!)</code>, which includes visiting all possible grid states.</li>
</ul>

<h3>2. Improved BFS Algorithm</h3>
<p>The improved BFS optimizes the search by dynamically generating nodes to be explored. This means that only accessible nodes are generated in real-time, reducing memory usage compared to the classic BFS.</p>
<ul>
  <li><strong>Description</strong>: This algorithm uses a <code>neighbors</code> function to generate only states accessible from the current state. This allows memory to hold only relevant states at each search step.</li>
  <li><strong>Complexity</strong>: Although the theoretical worst-case complexity remains equivalent to that of classic BFS, this algorithm is faster in practice as it reduces the number of nodes explored.</li>
</ul>

<h3>3. A* Algorithm</h3>
<p>The A* (A-Star) algorithm combines informed search techniques to prioritize promising nodes and optimize the traversal.</p>
<ul>
  <li><strong>Heuristic</strong>: Manhattan distance is used as a heuristic, quickly estimating the distance between two states.</li>
  <li><strong>Optimization</strong>: Unlike BFS, each node is processed according to its total cost, which is the sum of the cost to reach the node and the estimated cost to reach the destination.</li>
  <li><strong>Complexity</strong>: The complexity is dominated by sorting and accessing the open list, yielding an asymptotic complexity of <code>O(m * n * log((m * n)!))</code>.</li>
</ul>

<h2>User Interface with Pygame</h2>
<p>To facilitate interaction and experimentation, a graphical interface was developed using Pygame. This interface allows the user to play directly by swapping tiles to try to solve the puzzle manually. A state variable (<code>running</code>) determines whether the game is in progress or the player has finished.</p>

<ul>
  <li><strong>Features</strong>: 
    <ul>
      <li>The user can swap tiles by clicking on adjacent squares.</li>
      <li>The game displays a victory screen when the puzzle is solved.</li>
    </ul>
  </li>
  <li><strong>Difficulty Levels</strong>: Difficulty is modulated by grid size, increasing the number of tiles and game complexity.</li>
</ul>

<h2>Conclusion and Future Directions</h2>
<p>This project enabled the analysis of different graph traversal algorithms to solve a tile rearrangement problem, with a particular focus on memory optimization and execution time. While BFS and improved BFS are effective, A* proves to be the best compromise in terms of speed due to its informed approach.</p>

<p><strong>Future Directions</strong>: Several areas for improvement are possible, including exploring new heuristics for A*, adding score-tracking features, or adding customizable grids to vary difficulty levels.</p>
