import sys
sys.path.append("src/")

import unittest
from grid import Grid

class TestSwap(unittest.TestCase):
    """
    Unit tests for swap operations in the Grid class.
    """

    def test_single_swap(self):
        """
        Tests a single swap operation on a grid loaded from 'input/grid1.in'.
        """
        grid = Grid.grid_from_file("input/grid1.in")
        grid.swap((3, 0), (3, 1))
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [7, 8]], "Grid state should match after a single swap.")

    def test_swap_sequence(self):
        """
        Tests a sequence of swaps on a grid loaded from 'input/grid1.in'.
        """
        grid = Grid.grid_from_file("input/grid1.in")
        grid.swap_seq([((3, 0), (3, 1)), ((3, 0), (3, 1))])
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [8, 7]], "Grid state should match after swap sequence.")

if __name__ == '__main__':
    unittest.main()