import pygame

pygame.init()
font = pygame.font.SysFont("Verdana", 30)

def draw_menu(screen):
    screen.fill((255,255,255))

    def button(text, x, y):
        rect = pygame.Rect(x, y, 180, 50)
        pygame.draw.rect(screen, (200,200,200), rect)

        label = font.render(text, True, (0,0,0))
        screen.blit(label, (x+20, y+10))

        return rect

    return {
        "play": button("Play", 110, 150),
        "leader": button("Leaderboard", 110, 220),
        "settings": button("Settings", 110, 290),
        "quit": button("Quit", 110, 360)
    }