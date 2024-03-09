import pygame
import random
import sys

# initialisation de Pygame
pygame.init()

# Taille de la fenêtre Pygame
WINDOW_SIZE = 800

# Taille de la fenêtre de victoire
WIN_WINDOW_SIZE = 400

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Fonction pour "mélanger" la grille
def shuffle_grid(size):
    # Génération des nombres
    numbers = [i for i in range(1, size * size + 1)]
    # Mélanger les nombres
    random.shuffle(numbers)
    # Création de la grille
    grid = [numbers[i:i+size] for i in range(0, size*size, size)]
    return grid

# Fonction pour dessiner la Grille
def draw_grid(grid, cell_size, font):
    # Remplir la grille en blanc
    screen.fill(WHITE)
    # Mise en place de l'itération
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Dessiner le rectangle de chaque grille
            pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size), 2)
            # Remplir le rectangle du nombre de façon centré
            number = font.render(str(grid[y][x]), True, BLACK)
            text_rect = number.get_rect(center=(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2))
            screen.blit(number, text_rect)


# Definition d'une fonction pour échanger 2 éléments de la grille
def swap_cells(grid, y1, x1, y2, x2):
    # Échanger les deux valeurs
    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]


# Definition de la fonction principale
def main(size, cell_size):
    # Choix de la police
    font = pygame.font.Font(None, 50)
    # Mélange de la grille
    grid = shuffle_grid(size)
    # Initialisation des variables du jeu
    running = True
    selected_cell = None
    moves = 0

    # Mise en place de la boucle du jeu
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
                        # Vérification du tri de la Grille
                        if all(grid[i][j] == i * size + j + 1 for i in range(size) for j in range(size)):
                            running = False
                    selected_cell = None

        # Mise à jour de la grille et projection de la grille
        draw_grid(grid, cell_size, font)
        pygame.display.flip()

    # Afficher l'écran de vVictoire du jeu
    win_screen = pygame.Surface((WIN_WINDOW_SIZE, WIN_WINDOW_SIZE))
    win_screen.fill(WHITE)
    win_font = pygame.font.Font(None, 25)

    win_message = "Félication! Vous avez réussi. Nombre de swap total: {}".format(moves)
    win_text = win_font.render(win_message, True, BLACK)
    win_rect = win_text.get_rect(center=(WIN_WINDOW_SIZE // 2, WIN_WINDOW_SIZE // 2))
    win_screen.blit(win_text, win_rect)

    win_window = pygame.display.set_mode((WIN_WINDOW_SIZE, WIN_WINDOW_SIZE))
    pygame.display.set_caption("Félicitation!")
    win_window.blit(win_screen, (0, 0))
    pygame.display.flip()

    # Temps d'attente avant l'arrêt
    pygame.time.wait(5000)
    pygame.quit()

# Mise en place d'un choix de niveau de difficulté
def start_game(difficulty):
    if difficulty == "Easy":
        main(3, WINDOW_SIZE // 3)
    elif difficulty == "Medium":
        main(4, WINDOW_SIZE // 4)
    elif difficulty == "Hard":
        main(5, WINDOW_SIZE // 5)

# Fonction d'affichage du niveau de difficulté
def show_difficulty_select():
    # Remplir l'écran
    screen.fill(WHITE)
    # Choix de la police
    font = pygame.font.Font(None, 50)

    # Affichage centré du niveau Facile
    easy_text = font.render("Easy", True, BLACK)
    easy_rect = easy_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 4))
    screen.blit(easy_text, easy_rect)

    # Affichage centré du niveau Moyen
    medium_text = font.render("Medium", True, BLACK)
    medium_rect = medium_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
    screen.blit(medium_text, medium_rect)

    # Affichage centré du niveau Difficile
    hard_text = font.render("Hard", True, BLACK)
    hard_rect = hard_text.get_rect(center=(WINDOW_SIZE // 2, 3 * WINDOW_SIZE // 4))
    screen.blit(hard_text, hard_rect)

    pygame.display.flip()

    # Attente du choix du joueur
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

# Lancement de la partie
if __name__ == "__main__":
    # Mise en place du jeu
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Puzzle Game")

    # Affichage du niveau de difficulté
    difficulty = show_difficulty_select()
    # Lancement du jeu avec le niveau de difficulté choisi.
    start_game(difficulty)