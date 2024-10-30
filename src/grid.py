"""
This module defines the Grid class, used to represent the tile arrangement puzzle grid
and its associated methods.
"""

import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from itertools import permutations


class Grid:
    """
    Represents a grid for the tile swap puzzle, supporting any rectangular dimensions.

    Attributes:
    -----------
    m : int
        Number of rows in the grid.
    n : int
        Number of columns in the grid.
    state : list[list[int]]
        Current grid state as a list of lists, where state[i][j] contains the value at row i, column j.
        Rows are indexed from 0 to m-1 and columns from 0 to n-1.
    """

    def __init__(self, m, n, initial_state=None):
        """
        Initializes the grid with dimensions m x n. By default, creates a sorted grid.

        Parameters:
        -----------
        m : int
            Number of rows in the grid.
        n : int
            Number of columns in the grid.
        initial_state : list[list[int]], optional
            Initial configuration of the grid. If not provided, a sorted grid is generated.
        """
        self.m = m
        self.n = n
        if initial_state is None:
            initial_state = [list(range(i * n + 1, (i + 1) * n + 1)) for i in range(m)]
        self.state = initial_state

    def __str__(self):
        """
        Returns the grid state as a formatted string.
        """
        output = "Current grid state:\n"
        for row in self.state:
            output += f"{row}\n"
        return output

    def __repr__(self):
        """
        Returns a concise representation of the grid dimensions.
        """
        return f"<Grid: m={self.m}, n={self.n}>"

    def display(self):
        """
        Graphically displays the grid state using Matplotlib.
        """
        matrix = np.flipud(np.array(self.state))
        fig, ax = plt.subplots()

        ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
        ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                ax.text(j, i, str(matrix[i, j]), ha='center', va='center', color='black')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Grid Display')

        plt.show()

    def to_tuple(self):
        """
        Converts the grid state to an immutable tuple format.
        """
        return tuple(tuple(row) for row in self.state)

    def generate_permutations(self):
        """
        Generates all possible unique grid states by permutating the sorted list of numbers.

        Returns:
        --------
        list of tuple : List of all possible unique grid configurations.
        """
        sorted_numbers = list(range(1, self.m * self.n + 1))
        permutations_list = permutations(sorted_numbers)
        return [tuple([perm[i * self.n:(i + 1) * self.n] for i in range(self.m)]) for perm in permutations_list]

    def neighbors(self):
        """
        Generates all neighboring grid states that are one horizontal or vertical swap away.

        Returns:
        --------
        list of list : List of neighboring grid states.
        """
        neighbors = []

        # Horizontal swaps
        for i in range(self.m):
            for j in range(self.n - 1):
                neighbor = deepcopy(self)
                neighbor.swap((i, j), (i, j + 1))
                neighbors.append(neighbor.state)

        # Vertical swaps
        for j in range(self.n):
            for i in range(self.m - 1):
                neighbor = deepcopy(self)
                neighbor.swap((i, j), (i + 1, j))
                neighbors.append(neighbor.state)

        return neighbors

    def is_sorted(self):
        """
        Checks if the current grid state is sorted in ascending order.

        Returns:
        --------
        bool : True if the grid is sorted, False otherwise.
        """
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j] != i * self.n + j + 1:
                    return False
        return True

    def is_adjacent(self, cell1, cell2):
        """
        Checks if two cells are adjacent and within grid bounds.

        Parameters:
        -----------
        cell1, cell2 : tuple[int]
            Coordinates of the two cells as (row, column).

        Returns:
        --------
        bool : True if cells are adjacent and valid, False otherwise.
        """
        if not (0 <= cell1[0] < self.m and 0 <= cell1[1] < self.n):
            return False
        if not (0 <= cell2[0] < self.m and 0 <= cell2[1] < self.n):
            return False

        row_diff = abs(cell1[0] - cell2[0])
        col_diff = abs(cell1[1] - cell2[1])
        return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

    def swap(self, cell1, cell2):
        """
        Swaps two cells in the grid if the swap is allowed.

        Parameters:
        -----------
        cell1, cell2 : tuple[int]
            Coordinates of the two cells as (row, column).

        Raises:
        -------
        ValueError : If the cells are not adjacent or within grid bounds.
        """
        if not self.is_adjacent(cell1, cell2):
            raise ValueError("The specified cells cannot be swapped.")

        self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]] = (
            self.state[cell2[0]][cell2[1]],
            self.state[cell1[0]][cell1[1]]
        )

    def swap_sequence(self, cell_pairs):
        """
        Performs a sequence of swaps on the grid.

        Parameters:
        -----------
        cell_pairs : list[tuple]
            List of tuples representing pairs of cells to swap.
        """
        for cell1, cell2 in cell_pairs:
            self.swap(cell1, cell2)

    def manhattan_distance(self, other):
        """
        Calculates the Manhattan distance between two grid states.

        Parameters:
        -----------
        other : Grid
            The target grid state.

        Returns:
        --------
        int : Manhattan distance between the current and target grid states.
        """
        distance = 0
        for i in range(self.m):
            for j in range(self.n):
                distance += abs(self.state[i][j] - other.state[i][j])
        return distance

    def from_file(cls, file_name):
        """
        Loads a grid from a specified file.

        Parameters:
        -----------
        file_name : str
            Path to the file containing grid data.

        Returns:
        --------
        Grid : Grid initialized with the file data.
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            state = [list(map(int, file.readline().split())) for _ in range(m)]
            return cls(m, n, state)
