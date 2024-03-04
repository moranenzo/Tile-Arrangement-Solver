"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import random
import numpy as np
import matplotlib as plt
from itertools import permutations  # we are going to use this feature in the function generate to create all the grids


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids.

    Attributes:
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column.
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """

    def __init__(self, m, n, initial_state=[]):
        """
        Initializes the grid.

        Parameters:
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The initial state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        self.state = initial_state

    def __str__(self):
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m):
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self):
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def graphic_repr(self):
        matrice = self.state

        matrice = np.flipud(matrice)  # Inversion de la matrice pour mettre la première ligne en haut
        fig, ax = plt.subplots()

        ax.set_xticks(np.arange(-0.5, matrice.shape[1], 1), minor=True)
        ax.set_yticks(np.arange(-0.5, matrice.shape[0], 1), minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

        for i in range(matrice.shape[0]):
            for j in range(matrice.shape[1]):
                ax.text(j, i, str(matrice[i, j]), ha='center', va='center', color='black')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Tableau représentant la grille')

        plt.show()

    def hash(self):
        """
        Returns the tuple associated to the list self.state
        """
        initial_state = self.state
        return tuple(tuple(ligne) for ligne in initial_state)

    def generate(self):
        m = self.m
        n = self.n
        sorted = [i for i in range(1, m*n+1)]  # Creating the list sorted
        output = list(permutations(sorted, m*n))  # Generating all possible permutations of the sorted list
        return output

    def neighbors(self):
        n = self.n
        m = self.m
        matrice = self.state
        output = []
        for i in range(m):
            for j in range(n-1):
                output.append(Grid(m, n, matrice).swap((i,j),(i,j+1)))
        for j in range(n):
            for i in range(m-1):
                output.append(Grid(m, n, matrice).swap((i,j),(i+1,j)))
        return output

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        n = self.n
        m = self.m
        state = self.state
        for i in range(m):
            for j in range(n):
                if state[i][j] != i*n + j + 1:
                    return False
        return True

    def authorized_swap(self, cell1, cell2):

        m = len(self.state)

        n = len(self.state[0])

        diff_h = abs(cell1[0]-cell2[0])

        diff_l = abs(cell1[1]-cell2[1])
        
        z = [o for o in range(0, n)]

        z_2 = [k for k in range(0, m)]

        if (cell1[0] not in z_2) or (cell2[0] not in z_2):

            return False

        elif (cell1[1] not in z) or (cell2[1] not in z):

            return False

        elif (diff_h == 1 and diff_l == 1):

            return False

        else:

            return True


    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not
        allowed.

        Parameters:
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the
            column number of the cell.
        """
        diff_h = abs(cell1[0]-cell2[0])
        diff_l = abs(cell1[1]-cell2[1])
        if (diff_h == 1 and diff_l == 0) or (diff_h == 0 and diff_l == 1):
            v1 = self.state[cell1[0]][cell1[1]]
            v2 = self.state[cell2[0]][cell2[1]]
            self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]] = v2, v1

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters:
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of
            integers).
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for tuple in cell_pair_list:
            self.swap(tuple[0], tuple[1])

    @classmethod
    def grid_from_file(cls, file_name):
        """
        Creates a grid object from class Grid, initialized with the information from the file
        file_name.

        Parameters:
        -----------
        file_name: str
            Name of the file to load. The file must be of the format:
            - first line contains "m n"
            - next m lines contain n integers that represent the state of the corresponding cell

        Output:
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n:
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
