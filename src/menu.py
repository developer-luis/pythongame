import pygame
import sys
from game import game_window  # Importa la función del juego

# Inicializa PyGame
pygame.init()

# Configuración básica
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shoot Game Menu")

# Colores y fuentes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Carga la imagen de fondo del menú
menu_background = pygame.image.load("assets/images/background.png")
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Función para dibujar texto
def draw_text(text, font, color, surface, x, y, align="center"):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if align == "center":
        text_rect.center = (x, y)
    elif align == "left":
        text_rect.topleft = (x, y)
    elif align == "right":
        text_rect.topright = (x, y)
    surface.blit(text_obj, text_rect)

# Menú Principal
def main_menu():
    while True:
        # Dibuja la imagen de fondo
        screen.blit(menu_background, (0, 0))

        # Título
        draw_text("Shoot Game", title_font, WHITE, screen, SCREEN_WIDTH // 2, 50)

        # Botones
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Botón "Nuevo Juego"
        new_game_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, BLUE if new_game_button.collidepoint(mouse_pos) else GRAY, new_game_button)
        draw_text("Nuevo Juego", button_font, WHITE, screen, SCREEN_WIDTH // 2, 225)

        # Botón "Salir"
        quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, RED if quit_button.collidepoint(mouse_pos) else GRAY, quit_button)
        draw_text("Salir", button_font, WHITE, screen, SCREEN_WIDTH // 2, 325)

        # Eventos del mouse
        if mouse_click[0]:  # Detecta clic izquierdo
            if new_game_button.collidepoint(mouse_pos):
                print("Nuevo Juego seleccionado")
                game_window()  # Llama a la función del juego
            if quit_button.collidepoint(mouse_pos):
                print("Salir seleccionado")
                pygame.quit()
                sys.exit()

        # Eventos de salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()
