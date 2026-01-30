import random
import math

class Bot:
    def __init__(self):
        self.x = random.randint(100, 1180)
        self.y = random.randint(100, 620)
        self.health = 100
        self.alive = True
        self.radius = 8

    def update(self, player, zone):
        if not self.alive:
            return

        # Move toward player
        self.x += (player.x - self.x) * 0.002
        self.y += (player.y - self.y) * 0.002

        if not zone.is_inside(self.x, self.y):
            self.health -= 0.1

        if self.health <= 0:
            self.alive = False

    def draw(self, screen):
        if not self.alive:
            return
        import pygame
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
