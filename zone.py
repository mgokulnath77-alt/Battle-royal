import math

class Zone:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.radius = 300

    def update(self):
        if self.radius > 60:
            self.radius -= 0.05

    def is_inside(self, x, y):
        return math.hypot(x - self.x, y - self.y) < self.radius

    def draw(self, screen):
        import pygame
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y),
            int(self.radius),
            2
        )
