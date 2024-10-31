import sys
sys.path.append("src/")

import unittest
from grid import Grid

class TestGridLoading(unittest.TestCase):
    """
    Unit test for loading grids from file.
    """

    def test_grid1(self):
        """
        Tests loading grid dimensions and state from 'input/grid1.in'.
        """
        grid = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(grid.m, 4)
        self.assertEqual(grid.n, 2)
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [8, 7]])

if __name__ == '__main__':
    unittest.main()
