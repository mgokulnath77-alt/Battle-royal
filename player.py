class Player:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.health = 100
        self.radius = 10

    def update(self, zone):
        if not zone.is_inside(self.x, self.y):
            self.health -= 0.05

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), self.radius)
