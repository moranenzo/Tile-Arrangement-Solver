from grid import Grid

class Solver:
    """
    Solver class for the tile arrangement puzzle.
    """

    def get_solution(self):
        """
        Solves the grid puzzle and returns a list of swap operations needed
        to reach the sorted state.

        Returns:
        --------
        list[tuple[tuple[int, int], tuple[int, int]]]
            List of swaps in the format [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...],
            where each tuple represents a pair of cells to swap.
        """
        solution_steps = []
        tile_number = 1
        m, n = self.m, self.n

        while tile_number <= m * n:
            swap_sequence = []
            current_pos = self.position(tile_number)
            target_pos = (tile_number // n, tile_number % n - 1)

            # Determine swap direction: 1 for right, -1 for left
            direction = 1 if target_pos[1] > current_pos[1] else -1

            # Horizontal swaps to align columns
            for col in range(current_pos[1], target_pos[1], direction):
                swap_sequence.append(((current_pos[0], col), (current_pos[0], col + direction)))

            # Vertical swaps to align rows
            for row in range(current_pos[0], target_pos[0], -1):
                swap_sequence.append(((row, target_pos[1]), (row + 1, target_pos[1])))

            # Apply swaps and add to solution list
            self.swap_seq(swap_sequence)
            solution_steps.extend(swap_sequence)

            tile_number += 1

        return solution_steps
