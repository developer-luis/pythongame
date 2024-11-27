import pygame

class Bullet:
    def __init__(self, x, y, direction, speed=10, width=10, height=5):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Color rojo

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
