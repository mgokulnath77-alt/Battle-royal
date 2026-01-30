import pygame
from player import Player
from bot import Bot
from zone import Zone

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Royale - Python")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GROUND = (34, 139, 34)

# Player
player = Player()

# Bots (19 bots + player = 20)
bots = [Bot() for _ in range(19)]

# Zone
zone = Zone()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- UPDATE ---
    player.update(zone)
    for bot in bots:
        bot.update(player, zone)
    zone.update()

    alive_bots = sum(bot.alive for bot in bots)
    pygame.display.set_caption(
        f"Players Left: {alive_bots + 1}"
    )

    # --- DRAW ---
    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GROUND, (0, HEIGHT//2, WIDTH, HEIGHT//2))

    zone.draw(screen)
    player.draw(screen)

    for bot in bots:
        bot.draw(screen)

    pygame.display.flip()

pygame.quit()
