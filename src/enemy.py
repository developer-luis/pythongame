import pygame

class Enemy:
    def __init__(self, x, y, direction, left_sprites, right_sprites, speed=3):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.left_sprites = left_sprites
        self.right_sprites = right_sprites
        self.direction = direction  # "left" o "right"
        self.speed = speed
        self.animation_index = 0
        # Determina el sprite inicial según la dirección
        self.image = self.left_sprites[self.animation_index] if self.direction == "left" else self.right_sprites[self.animation_index]

    def move(self):
        # Movimiento opuesto a la dirección de generación
        if self.direction == "left":
            self.x += self.speed  # Mover hacia la derecha
        elif self.direction == "right":
            self.x -= self.speed  # Mover hacia la izquierda

    def update_animation(self):
        self.animation_index += 0.2
        if self.animation_index >= len(self.left_sprites):
            self.animation_index = 0
        self.image = self.left_sprites[int(self.animation_index)] if self.direction == "right" else self.right_sprites[int(self.animation_index)]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def check_collision_with_player(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.width > player.x and
            self.y < player.y + player.height and
            self.y + self.height > player.y
        )

    def check_collision_with_bullet(self, bullets):
        for bullet in bullets:
            if (
                self.x < bullet.x + bullet.width and
                self.x + self.width > bullet.x and
                self.y < bullet.y + bullet.height and
                self.y + self.height > bullet.y
            ):
                bullets.remove(bullet)  # Eliminar bala
                return True
        return False
