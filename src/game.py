import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window size for the Pygame display
WINDOW_SIZE = 900

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to shuffle the grid randomly
def shuffle_grid(size):
    """
    Generates a shuffled grid of numbers for the game.

    Parameters:
    -----------
    size : int
        The number of rows and columns in the grid.

    Returns:
    --------
    list of list : Shuffled grid.
    """
    numbers = [i for i in range(1, size * size + 1)]
    random.shuffle(numbers)
    grid = [numbers[i:i + size] for i in range(0, size * size, size)]
    return grid

# Function to draw the grid on the Pygame window
def draw_grid(grid, cell_size, font):
    """
    Draws the grid on the Pygame screen.

    Parameters:
    -----------
    grid : list of list
        The grid to draw.
    cell_size : int
        Size of each cell in the grid.
    font : pygame.font.Font
        Font to use for rendering numbers in cells.
    """
    screen.fill(WHITE)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size), 2)
            number = font.render(str(grid[y][x]), True, BLACK)
            text_rect = number.get_rect(center=(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2))
            screen.blit(number, text_rect)

# Function to swap two cells in the grid
def swap_cells(grid, y1, x1, y2, x2):
    """
    Swaps the values of two cells in the grid.

    Parameters:
    -----------
    grid : list of list
        The grid where the swap will be performed.
    y1, x1 : int
        Coordinates of the first cell.
    y2, x2 : int
        Coordinates of the second cell.
    """
    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

# Main function to run the game
def main(size, cell_size):
    """
    Main game loop for the tile puzzle.

    Parameters:
    -----------
    size : int
        Size of the grid (e.g., 3 for a 3x3 grid).
    cell_size : int
        Size of each cell in the grid.
    """
    font = pygame.font.Font(None, 50)
    grid = shuffle_grid(size)
    running = True
    selected_cell = None
    moves = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked_col = x // cell_size
                clicked_row = y // cell_size
                if selected_cell is None:
                    selected_cell = (clicked_row, clicked_col)
                else:
                    target_cell = (clicked_row, clicked_col)
                    if abs(selected_cell[0] - target_cell[0]) + abs(selected_cell[1] - target_cell[1]) == 1:
                        swap_cells(grid, selected_cell[0], selected_cell[1], target_cell[0], target_cell[1])
                        moves += 1
                        if all(grid[i][j] == i * size + j + 1 for i in range(size) for j in range(size)):
                            running = False
                    selected_cell = None

        draw_grid(grid, cell_size, font)
        pygame.display.flip()

    show_win_screen(moves)

def show_win_screen(moves):
    """
    Displays the win screen with the total number of moves.

    Parameters:
    -----------
    moves : int
        Total moves taken to solve the puzzle.
    """
    WIN_WINDOW_SIZE = 600
    win_screen = pygame.Surface((WIN_WINDOW_SIZE, WIN_WINDOW_SIZE))
    win_screen.fill(WHITE)
    win_font = pygame.font.Font(None, 25)

    win_message = f"Congratulations! Puzzle solved in {moves} moves."
    win_text = win_font.render(win_message, True, BLACK)
    win_rect = win_text.get_rect(center=(WIN_WINDOW_SIZE // 2, WIN_WINDOW_SIZE // 2))
    win_screen.blit(win_text, win_rect)

    win_window = pygame.display.set_mode((WIN_WINDOW_SIZE, WIN_WINDOW_SIZE))
    pygame.display.set_caption("Congratulations!")
    win_window.blit(win_screen, (0, 0))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

# Function to start the game at a chosen difficulty level
def start_game(difficulty):
    """
    Starts the game with a specified difficulty level.

    Parameters:
    -----------
    difficulty : str
        Difficulty level, can be "Easy", "Medium", or "Hard".
    """
    if difficulty == "Easy":
        main(3, WINDOW_SIZE // 3)
    elif difficulty == "Medium":
        main(4, WINDOW_SIZE // 4)
    elif difficulty == "Hard":
        main(5, WINDOW_SIZE // 5)

# Function to show the difficulty selection screen
def show_difficulty_select():
    """
    Displays the difficulty selection screen and returns the chosen difficulty level.

    Returns:
    --------
    str : Selected difficulty level ("Easy", "Medium", or "Hard").
    """
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)

    easy_text = font.render("Easy", True, BLACK)
    easy_rect = easy_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 4))
    screen.blit(easy_text, easy_rect)

    medium_text = font.render("Medium", True, BLACK)
    medium_rect = medium_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
    screen.blit(medium_text, medium_rect)

    hard_text = font.render("Hard", True, BLACK)
    hard_rect = hard_text.get_rect(center=(WINDOW_SIZE // 2, 3 * WINDOW_SIZE // 4))
    screen.blit(hard_text, hard_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < WINDOW_SIZE // 3:
                    return "Easy"
                elif y < 2 * WINDOW_SIZE // 3:
                    return "Medium"
                else:
                    return "Hard"

# Main entry point
if __name__ == "__main__":
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Puzzle Game")

    difficulty = show_difficulty_select()
    start_game(difficulty)
