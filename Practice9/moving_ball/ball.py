import pygame

class Ball:
    def __init__(self, x, y, radius=25):
        self.x = x            # x position of the ball
        self.y = y            # y position of the ball
        self.radius = radius  # ball size

    def move(self, dx, dy, width, height):
        # calculate new position
        new_x = self.x + dx
        new_y = self.y + dy

        # move horizontally only if inside screen
        if self.radius <= new_x <= width - self.radius:
            self.x = new_x

        # move vertically only if inside screen
        if self.radius <= new_y <= height - self.radius:
            self.y = new_y

    def draw(self, screen):
        # draw red circle
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)