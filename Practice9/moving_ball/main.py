import pygame
from ball import Ball

pygame.init()

# window size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# create ball in center
ball = Ball(WIDTH // 2, HEIGHT // 2)

running = True

while running:
    # background color
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            running = False

        # keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-20, 0, WIDTH, HEIGHT)   # move left
            elif event.key == pygame.K_RIGHT:
                ball.move(20, 0, WIDTH, HEIGHT)    # move right
            elif event.key == pygame.K_UP:
                ball.move(0, -20, WIDTH, HEIGHT)   # move up
            elif event.key == pygame.K_DOWN:
                ball.move(0, 20, WIDTH, HEIGHT)    # move down

    # draw ball
    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()