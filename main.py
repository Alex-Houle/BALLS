import pygame
import sys
import random
from ball import Ball 

pygame.init()

WIDTH, HEIGHT = 640, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balls")

colors = [
    (255, 179, 186),  # Pink
    (255, 223, 186),  # Peach
    (255, 255, 186),  # Yellow
    (186, 255, 201),  # Mint
    (186, 225, 255),  # Blue
    (218, 186, 255),  # Purple
    (255, 204, 229),  # Rose
    (204, 255, 229),  # Seafoam
    (204, 229, 255),  # Light Sky
    (229, 204, 255),  # Lavender
    (255, 204, 204),  # Soft Red
    (255, 255, 204),  # Light Lemon
    (204, 255, 204),  # Spring Green
    (204, 255, 255),  # Pale Cyan
    (255, 204, 255),  # Bubblegum
]
circol = random.choice(colors)

balls = list()

clock = pygame.time.Clock()


running = True
while running:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                balls.append(Ball(WIDTH//2, HEIGHT//2, 10, random.choice(colors)))
                print(f"Ball added\nBall Number: {len(balls)}")
            elif event.key == pygame.K_RSHIFT and len(balls) != 0:
                balls.pop()
                print("Ball Removed")

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, circol, (WIDTH // 2, HEIGHT // 2 ), 300, width = 1)
    for ball in balls: 
        ball.draw(screen)
        ball.update()

    pygame.display.flip()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].collide_with(balls[j])
    

pygame.quit()
sys.exit()

