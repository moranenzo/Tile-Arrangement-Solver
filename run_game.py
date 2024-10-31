import pygame
import sys
from src.game import show_difficulty_select, start_game

def main():
    """
    Main function to launch the interactive tile puzzle game.
    """
    # Initialize Pygame and set the window caption
    pygame.init()
    pygame.display.set_caption("Tile Puzzle Game")

    # Show the difficulty selection screen and get user's choice
    difficulty = show_difficulty_select()

    # Start the game with the selected difficulty
    start_game(difficulty)

    # Quit Pygame properly after the game ends
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
