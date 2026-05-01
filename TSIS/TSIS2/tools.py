import pygame

# FLOOD FILL
def flood_fill(surface, x, y, new_color, width, height):
    target_color = surface.get_at((x,y))
    if target_color == new_color:
        return

    stack = [(x,y)]

    while stack:
        px, py = stack.pop()

        if px < 0 or py < 0 or px >= width or py >= height:
            continue

        if surface.get_at((px,py)) != target_color:
            continue

        surface.set_at((px,py), new_color)

        stack.append((px+1,py))
        stack.append((px-1,py))
        stack.append((px,py+1))
        stack.append((px,py-1))


# PENCIL / ERASER
def draw_pencil(surface, color, start, end, radius):
    pygame.draw.line(surface, color, start, end, radius)


def draw_eraser(surface, start, end, radius, bg_color):
    pygame.draw.line(surface, bg_color, start, end, radius)


# BASIC SHAPES
def draw_line(surface, color, start, end, radius):
    pygame.draw.line(surface, color, start, end, radius)


def draw_rectangle(surface, color, start, end, radius):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.rect(surface, color,
        (min(x1,x2), min(y1,y2),
         abs(x2-x1), abs(y2-y1)), radius)


def draw_circle(surface, color, start, end, radius):
    import math
    r = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    pygame.draw.circle(surface, color, start, r, radius)


# ADVANCED SHAPES
def draw_square(surface, color, start, end, radius):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2-x1), abs(y2-y1))
    pygame.draw.rect(surface, color, (x1,y1,side,side), radius)


def draw_right_triangle(surface, color, start, end, radius):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surface, color,
        [(x1,y1),(x2,y2),(x1,y2)], radius)


def draw_equilateral_triangle(surface, color, start, end, radius):
    import math
    x1, y1 = start
    x2, y2 = end

    side = abs(x2-x1)
    h = side * math.sqrt(3) / 2

    points = [
        (x1,y1),
        (x1+side,y1),
        (x1+side/2,y1-h)
    ]

    pygame.draw.polygon(surface, color, points, radius)


def draw_rhombus(surface, color, start, end, radius):
    x1, y1 = start
    x2, y2 = end

    cx = (x1+x2)//2
    cy = (y1+y2)//2

    dx = abs(x2-x1)//2
    dy = abs(y2-y1)//2

    points = [
        (cx,cy-dy),
        (cx+dx,cy),
        (cx,cy+dy),
        (cx-dx,cy)
    ]

    pygame.draw.polygon(surface, color, points, radius)