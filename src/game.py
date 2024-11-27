import pygame
import sys
import random
from player import Player
from enemy import Enemy
from utils import load_sprites

# Configuración básica
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shoot Game")

# Carga la imagen de fondo
game_background = pygame.image.load("assets/images/background.png")
game_background = pygame.transform.scale(game_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fuente para texto
pygame.font.init()
font = pygame.font.Font(None, 50)
large_font = pygame.font.Font(None, 100)


def game_window():
    clock = pygame.time.Clock()

    # Cargar sprites
    player_sprites_left = load_sprites("assets/animations/player/left")
    player_sprites_right = load_sprites("assets/animations/player/right")
    enemy_sprites_left = load_sprites("assets/animations/enemy/left")
    enemy_sprites_right = load_sprites("assets/animations/enemy/right")

    # Variables del estado del juego
    player = None
    enemies = []
    enemies_killed = 0
    enemy_speed = 3
    speed_increase_time = pygame.time.get_ticks()
    game_over = False

    def reset_game():
        """Reinicia el estado del juego."""
        nonlocal player, enemies, enemies_killed, enemy_speed, speed_increase_time, game_over
        player = Player(400, 500, 50, 50, player_sprites_left, player_sprites_right)
        enemies.clear()
        enemies_killed = 0
        enemy_speed = 3
        speed_increase_time = pygame.time.get_ticks()
        game_over = False

    # Inicializar estado del juego
    reset_game()

    # Temporizador para generar enemigos
    enemy_spawn_timer = 0

    def spawn_enemy():
        """Genera un enemigo en los extremos izquierdo o derecho."""
        side = random.choice(["left", "right"])
        x = 0 if side == "left" else SCREEN_WIDTH - 50
        y = 500
        enemy = Enemy(x, y, side, enemy_sprites_left, enemy_sprites_right, enemy_speed)
        enemies.append(enemy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not game_over and event.key == pygame.K_z:
                    player.shoot()
                elif game_over:
                    if event.key == pygame.K_r:
                        reset_game()  # Reinicia el juego
                    elif event.key == pygame.K_ESCAPE:
                        from menu import main_menu
                        main_menu()  # Regresa al menú principal

        if not game_over:
            keys = pygame.key.get_pressed()
            player.move(keys, 5, SCREEN_WIDTH)
            player.update_bullets(SCREEN_WIDTH)
            player.update_animation()

            # Incrementar la velocidad de los enemigos cada 10 segundos
            if pygame.time.get_ticks() - speed_increase_time > 10000:
                enemy_speed += 1
                speed_increase_time = pygame.time.get_ticks()

            # Actualizar enemigos
            if enemy_spawn_timer == 0:
                spawn_enemy()
                enemy_spawn_timer = 100
            enemy_spawn_timer = max(0, enemy_spawn_timer - 1)

            for enemy in enemies[:]:
                enemy.move()
                enemy.update_animation()

                if (enemy.x < 0 and enemy.direction == "left") or (enemy.x > SCREEN_WIDTH and enemy.direction == "right"):
                    enemies.remove(enemy)

                if enemy.check_collision_with_bullet(player.bullets):
                    enemies.remove(enemy)
                    enemies_killed += 1

                if enemy.check_collision_with_player(player):
                    game_over = True

        # Dibujar todo
        screen.blit(game_background, (0, 0))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Mostrar contador
        counter_text = font.render(f"Enemigos eliminados: {enemies_killed}", True, (255, 255, 255))
        screen.blit(counter_text, (SCREEN_WIDTH // 2 - counter_text.get_width() // 2, 130))

        if game_over:
            game_over_text = large_font.render(f"GAME OVER", True, (255, 0, 0))
            score_text = font.render(f"Puntuación: {enemies_killed}", True, (255, 255, 255))
            restart_text = font.render("Presiona R para reiniciar o ESC para salir", True, (255, 255, 255))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()
        clock.tick(60)
