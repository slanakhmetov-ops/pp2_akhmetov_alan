
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

screen.fill("white")

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

color = BLACK
radius = 5
drawing = False

# modes: brush, rectangle, circle, eraser
mode = "brush"

start_pos = None

# font for controls text
font = pygame.font.SysFont("Arial", 18)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()

            # brush draws instantly
            if mode == "brush":
                pygame.draw.circle(screen, color, start_pos, radius)

            # eraser draws white
            if mode == "eraser":
                pygame.draw.circle(screen, WHITE, start_pos, radius)

        # mouse released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()

            # rectangle mode
            if mode == "rectangle":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                width = abs(start_pos[0] - end_pos[0])
                height = abs(start_pos[1] - end_pos[1])

                pygame.draw.rect(screen, color, (x, y, width, height), 2)

            # circle mode
            if mode == "circle":
                center = start_pos
                radius_circle = int(
                    ((end_pos[0] - start_pos[0]) ** 2 +
                     (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                )

                pygame.draw.circle(screen, color, center, radius_circle, 2)

        # keyboard controls
        if event.type == pygame.KEYDOWN:

            # colors
            if event.key == pygame.K_r:
                color = RED

            if event.key == pygame.K_g:
                color = GREEN

            if event.key == pygame.K_b:
                color = BLUE

            if event.key == pygame.K_k:
                color = BLACK

            # clear canvas
            if event.key == pygame.K_c:
                screen.fill(WHITE)

            # size change
            if event.key == pygame.K_UP:
                radius = min(radius + 2, 50)

            if event.key == pygame.K_DOWN:
                radius = max(radius - 2, 1)

            # modes
            if event.key == pygame.K_p:
                mode = "brush"

            if event.key == pygame.K_t:
                mode = "rectangle"

            if event.key == pygame.K_o:
                mode = "circle"

            if event.key == pygame.K_e:
                mode = "eraser"

    # brush + eraser while holding mouse
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        if mode == "brush":
            pygame.draw.circle(screen, color, mouse_pos, radius)

        if mode == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, radius)

    # controls text on screen
    controls = [
        "R - Red",
        "G - Green",
        "B - Blue",
        "K - Black",
        "P - Brush",
        "T - Rectangle",
        "O - Circle",
        "E - Eraser",
        "C - Clear",
        "UP / DOWN - Size",
        "Current mode: " + mode
    ]

    # white box for text so it stays readable
    pygame.draw.rect(screen, WHITE, (0, 0, 250, 230))

    y = 10
    for line in controls:
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, y))
        y += 20

    pygame.display.flip()
    clock.tick(60)

pygame.quit()