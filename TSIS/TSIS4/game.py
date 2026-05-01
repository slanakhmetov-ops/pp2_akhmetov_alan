import pygame
import random
from config import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10,10), Point(9,10), Point(8,10)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self, screen, color):
        for i, seg in enumerate(self.body):
            c = color if i == 0 else (255,255,0)
            pygame.draw.rect(screen, c, (seg.x*CELL, seg.y*CELL, CELL, CELL))

    def collision(self, obstacles):
        head = self.body[0]

        if head.x < 0 or head.x >= WIDTH//CELL or head.y < 0 or head.y >= HEIGHT//CELL:
            return True

        for seg in self.body[1:]:
            if head.x == seg.x and head.y == seg.y:
                return True

        for o in obstacles:
            if head.x == o.x and head.y == o.y:
                return True

        return False


def safe_spawn(snake, obstacles):
    while True:
        x = random.randint(0, WIDTH//CELL - 1)
        y = random.randint(0, HEIGHT//CELL - 1)

        if any(s.x == x and s.y == y for s in snake.body):
            continue

        if any(o.x == x and o.y == y for o in obstacles):
            continue

        return Point(x, y)


class Food:
    def __init__(self):
        self.pos = Point(0,0)
        self.value = 1

    def generate(self, snake, obstacles):
        self.pos = safe_spawn(snake, obstacles)
        self.value = random.choice([1,2,3])

    def draw(self, screen):
        colors = [(0,255,0),(0,255,255),(255,0,255)]
        pygame.draw.rect(screen, colors[self.value-1],
                         (self.pos.x*CELL, self.pos.y*CELL, CELL, CELL))


class Poison:
    def __init__(self):
        self.pos = Point(0,0)

    def generate(self, snake, obstacles):
        self.pos = safe_spawn(snake, obstacles)

    def draw(self, screen):
        pygame.draw.rect(screen, (139,0,0),
                         (self.pos.x*CELL, self.pos.y*CELL, CELL, CELL))


class PowerUp:
    def __init__(self):
        self.type = random.choice(["speed","slow","life"])
        self.pos = Point(0,0)
        self.spawn_time = pygame.time.get_ticks()

    def generate(self, snake, obstacles):
        self.pos = safe_spawn(snake, obstacles)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, screen):
        colors = {
            "speed": (255,255,0),
            "slow": (0,0,255),
            "life": (255,165,0)
        }
        pygame.draw.rect(screen, colors[self.type],
                         (self.pos.x*CELL, self.pos.y*CELL, CELL, CELL))

    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 8000


def generate_obstacles(level, snake):
    if level < 3:
        return []

    obstacles = []
    for _ in range(level * 2):
        obstacles.append(safe_spawn(snake, obstacles))

    return obstacles