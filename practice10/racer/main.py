import pygame
import sys
from pygame.locals import *
import random

pygame.init()

# music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# crash sound
crash_sound = pygame.mixer.Sound("crash.wav")

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# game values
SPEED = 5
SCORE = 0
COINS = 0
game_over_state = False

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
restart_font = pygame.font.SysFont("Verdana", 18)

game_over_text = font.render("Game Over", True, BLACK)

# background
background = pygame.image.load("AnimatedStreet.png")

# screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("space_racer.png")
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect(center=(160, 520))

    def reset(self):
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-10, 0)

        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(10, 0)


# ================= ENEMY =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = [
            "Enemy.png",
            "conquest.jpg",
            "homelander.png",
            "invincible.jpg"
        ]

        self.reset()

    def reset(self):
        img = pygame.image.load(random.choice(self.images))
        self.image = pygame.transform.scale(img, (50, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-200, -100)
        )

    def move(self):
        global SCORE

        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset()


# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.generate()

    def generate(self):
        # random value
        self.value = random.choice([1, 2, 3])

        # color by value
        if self.value == 1:
            color = (255, 215, 0)
        elif self.value == 2:
            color = (0, 255, 255)
        else:
            color = (255, 0, 255)

        # redraw coin
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (15, 15), 15)

        # position
        while True:
            self.rect.center = (
                random.randint(50, SCREEN_WIDTH - 50),
                random.randint(-300, -100)
            )

            if not self.rect.colliderect(E1.rect):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.generate()


# ================= RESET =================
def reset_game():
    global SCORE, COINS, SPEED, game_over_state

    SCORE = 0
    COINS = 0
    SPEED = 5
    game_over_state = False

    P1.reset()
    E1.reset()
    C1.generate()


# ================= OBJECTS =================
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# speed timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # restart
        if event.type == KEYDOWN:
            if event.key == K_r and game_over_state:
                reset_game()

        # slow speed growth
        if event.type == INC_SPEED and not game_over_state:
            SPEED += 0.2

    DISPLAYSURF.blit(background, (0, 0))

    # UI
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_text, (260, 10))

    if not game_over_state:

        P1.move()
        E1.move()
        C1.move()

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)

        # crash
        if pygame.sprite.spritecollideany(P1, enemies):
            crash_sound.play()
            game_over_state = True

        # coin pickup
        if pygame.sprite.spritecollideany(P1, coins):
            COINS += C1.value
            C1.generate()

            # increase difficulty every 5 coins
            if COINS % 5 == 0:
                SPEED += 1

    else:
        # game over screen
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)

        DISPLAYSURF.blit(game_over_text, (30, 230))

        restart_text = restart_font.render("Press R to restart", True, WHITE)
        DISPLAYSURF.blit(restart_text, (110, 320))

    pygame.display.update()
    FramePerSec.tick(FPS)