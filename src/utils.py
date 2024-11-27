import pygame
import os

def load_sprites(folder):
    return [pygame.image.load(os.path.join(folder, f"{i}.png")) for i in range(1, 7)]
