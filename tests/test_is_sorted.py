# This test should be run from the root folder (e.g., ensae-prog24)
import sys
sys.path.append("src/")

import unittest
from grid import Grid

class TestIsSorted(unittest.TestCase):
    """
    Unit test for checking if a grid is sorted.
    """

    def test_grid_sorted_status(self):
        """
        Tests the is_sorted method on an unsorted grid loaded from 'input/grid1.in',
        then performs a swap to verify the sorted state.
        """
        grid = Grid.grid_from_file("input/grid1.in")
        self.assertFalse(grid.is_sorted(), "Grid should initially be unsorted.")
        
        # Perform a swap to achieve the sorted configuration
        grid.swap((3, 0), (3, 1))
        self.assertTrue(grid.is_sorted(), "Grid should be sorted after swap.")

if __name__ == '__main__':
    unittest.main()
