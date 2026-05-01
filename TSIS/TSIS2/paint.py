import pygame
from datetime import datetime
import tools

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint TSIS 2")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255,255,255))

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

color = BLACK

# BRUSH
sizes = [2,5,10]
index = 1
radius = sizes[index]

mode = "pencil"
drawing = False

start_pos = None
prev_pos = None

font = pygame.font.SysFont("Arial", 18)

# TEXT
text_mode = False
text_input = ""
text_pos = (0,0)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # TEXT INPUT
        if text_mode and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                txt = font.render(text_input, True, color)
                canvas.blit(txt, text_pos)
                text_mode = False
                text_input = ""
            elif event.key == pygame.K_ESCAPE:
                text_mode = False
            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            prev_pos = event.pos

            if mode == "fill":
                tools.flood_fill(canvas, event.pos[0], event.pos[1], color, WIDTH, HEIGHT)

            if mode == "text":
                text_mode = True
                text_input = ""
                text_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "line":
                tools.draw_line(canvas, color, start_pos, end_pos, radius)

            elif mode == "rectangle":
                tools.draw_rectangle(canvas, color, start_pos, end_pos, radius)

            elif mode == "circle":
                tools.draw_circle(canvas, color, start_pos, end_pos, radius)

            elif mode == "square":
                tools.draw_square(canvas, color, start_pos, end_pos, radius)

            elif mode == "right_triangle":
                tools.draw_right_triangle(canvas, color, start_pos, end_pos, radius)

            elif mode == "eq_triangle":
                tools.draw_equilateral_triangle(canvas, color, start_pos, end_pos, radius)

            elif mode == "rhombus":
                tools.draw_rhombus(canvas, color, start_pos, end_pos, radius)

        elif event.type == pygame.KEYDOWN:

            # COLORS
            if event.key == pygame.K_r: color = RED
            if event.key == pygame.K_g: color = GREEN
            if event.key == pygame.K_b: color = BLUE
            if event.key == pygame.K_k: color = BLACK

            # MODES
            if event.key == pygame.K_p: mode = "pencil"
            if event.key == pygame.K_e: mode = "eraser"
            if event.key == pygame.K_l: mode = "line"
            if event.key == pygame.K_t: mode = "rectangle"
            if event.key == pygame.K_o: mode = "circle"
            if event.key == pygame.K_s: mode = "square"
            if event.key == pygame.K_4: mode = "right_triangle"
            if event.key == pygame.K_5: mode = "eq_triangle"
            if event.key == pygame.K_6: mode = "rhombus"
            if event.key == pygame.K_f: mode = "fill"
            if event.key == pygame.K_x: mode = "text"

            # SIZE
            if event.key == pygame.K_1: index = 0
            if event.key == pygame.K_2: index = 1
            if event.key == pygame.K_3: index = 2
            radius = sizes[index]

            # CLEAR
            if event.key == pygame.K_c:
                canvas.fill(WHITE)

            # SAVE
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

    # DRAWING
    if drawing:
        pos = pygame.mouse.get_pos()

        if mode == "pencil":
            tools.draw_pencil(canvas, color, prev_pos, pos, radius)
            prev_pos = pos

        elif mode == "eraser":
            tools.draw_eraser(canvas, prev_pos, pos, radius, WHITE)
            prev_pos = pos

    # PREVIEW LINE
    if drawing and mode == "line":
        pygame.draw.line(screen, color, start_pos, pygame.mouse.get_pos(), radius)

    # TEXT PREVIEW
    if text_mode:
        txt = font.render(text_input, True, color)
        screen.blit(txt, text_pos)

    # UI
    ui = [
        "R G B K - colors",
        "P pencil | E eraser",
        "L line | T rect | O circle",
        "S square | 4/5/6 triangles",
        "F fill | X text",
        "1/2/3 size",
        "C clear | Ctrl+S save",
        f"Mode: {mode}"
    ]

    pygame.draw.rect(screen, (230,230,230), (0,0,260,200))

    y = 10
    for line in ui:
        txt = font.render(line, True, BLACK)
        screen.blit(txt, (10,y))
        y += 18

    pygame.display.flip()
    clock.tick(60)

pygame.quit()