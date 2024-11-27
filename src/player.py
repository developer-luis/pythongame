import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, y, width, height, left_sprites, right_sprites):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left_sprites = left_sprites
        self.right_sprites = right_sprites
        self.direction = "right"  # Dirección inicial
        self.animation_index = 0
        self.image = self.right_sprites[self.animation_index]
        self.is_moving = False
        self.bullets = []  # Lista de balas disparadas

    def move(self, keys, speed, screen_width):
        self.is_moving = False
        if keys[pygame.K_LEFT]:
            self.x -= speed
            self.direction = "left"
            self.is_moving = True
        elif keys[pygame.K_RIGHT]:
            self.x += speed
            self.direction = "right"
            self.is_moving = True

        # Limitar movimiento dentro de la pantalla
        self.x = max(0, min(screen_width - self.width, self.x))

    def shoot(self):
        # Crear una bala en la dirección actual
        if self.direction == "right":
            bullet = Bullet(self.x + self.width, self.y + (self.height - 12) // 2, "right")
        else:
            bullet = Bullet(self.x, self.y + (self.height - 12) // 2, "left")
        self.bullets.append(bullet)

    def update_bullets(self, screen_width):
        # Mover balas y eliminarlas si salen de la pantalla
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.x < 0 or bullet.x > screen_width:
                self.bullets.remove(bullet)

    def update_animation(self):
        if self.is_moving:
            self.animation_index += 0.2
            if self.animation_index >= len(self.left_sprites):
                self.animation_index = 0
            if self.direction == "left":
                self.image = self.left_sprites[int(self.animation_index)]
            elif self.direction == "right":
                self.image = self.right_sprites[int(self.animation_index)]
        else:
            self.animation_index = 0
            self.image = self.left_sprites[0] if self.direction == "left" else self.right_sprites[0]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(surface)
