import pygame
import math

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

# modes
mode = "brush"

start_pos = None

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

            if mode == "brush":
                pygame.draw.circle(screen, color, start_pos, radius)

            if mode == "eraser":
                pygame.draw.circle(screen, WHITE, start_pos, radius)

        # mouse released - draw shapes
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()

            x1, y1 = start_pos
            x2, y2 = end_pos

            # RECTANGLE
            if mode == "rectangle":
                pygame.draw.rect(
                    screen,
                    color,
                    (min(x1, x2), min(y1, y2),
                     abs(x2 - x1), abs(y2 - y1)),
                    2
                )

            # SQUARE
            if mode == "square":
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(
                    screen,
                    color,
                    (x1, y1, side, side),
                    2
                )

            # RIGHT TRIANGLE
            if mode == "right_triangle":
                pygame.draw.polygon(
                    screen,
                    color,
                    [(x1, y1), (x2, y2), (x1, y2)],
                    2
                )

            # EQUILATERAL TRIANGLE
            if mode == "eq_triangle":
                side = abs(x2 - x1)

                # height of equilateral triangle
                h = side * math.sqrt(3) / 2

                points = [
                    (x1, y1),
                    (x1 + side, y1),
                    (x1 + side / 2, y1 - h)
                ]

                pygame.draw.polygon(screen, color, points, 2)

            #RHOMBUS
            if mode == "rhombus":
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2

                points = [
                    (cx, cy - dy),
                    (cx + dx, cy),
                    (cx, cy + dy),
                    (cx - dx, cy)
                ]

                pygame.draw.polygon(screen, color, points, 2)

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

            # clear screen
            if event.key == pygame.K_c:
                screen.fill(WHITE)

            # brush size
            if event.key == pygame.K_UP:
                radius = min(radius + 2, 50)
            if event.key == pygame.K_DOWN:
                radius = max(radius - 2, 1)

            # modes
            if event.key == pygame.K_p:
                mode = "brush"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_t:
                mode = "rectangle"
            if event.key == pygame.K_s:
                mode = "square"
            if event.key == pygame.K_1:
                mode = "right_triangle"
            if event.key == pygame.K_2:
                mode = "eq_triangle"
            if event.key == pygame.K_3:
                mode = "rhombus"

    # brush / eraser drawing
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        if mode == "brush":
            pygame.draw.circle(screen, color, mouse_pos, radius)

        if mode == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, radius)

    # UI controls
    controls = [
        "R/G/B/K - Colors",
        "P - Brush",
        "E - Eraser",
        "T - Rectangle",
        "S - Square",
        "1 - Right Triangle",
        "2 - Equilateral Triangle",
        "3 - Rhombus",
        "C - Clear",
        "UP/DOWN - Size",
        "Mode: " + mode
    ]

    pygame.draw.rect(screen, WHITE, (0, 0, 300, 260))

    y = 10
    for line in controls:
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, y))
        y += 20

    pygame.display.flip()
    clock.tick(60)

pygame.quit()