import pygame
import sys

from ui import draw_menu
from persistence import load_settings, save_settings, load_scores, save_score
from racer import RacerGame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("assets/background.wav")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS3 Racer")

font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

state = "menu"
settings = load_settings()

if "difficulty" not in settings:
    settings["difficulty"] = "medium"

pygame.mixer.music.set_volume(1 if settings["sound"] else 0)

game = None
username = ""
error_msg = ""

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== MENU =====
        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = draw_menu(screen)

                if buttons["play"].collidepoint(event.pos):
                    username = ""
                    error_msg = ""
                    state = "username"

                elif buttons["leader"].collidepoint(event.pos):
                    state = "leaderboard"

                elif buttons["settings"].collidepoint(event.pos):
                    state = "settings"

                elif buttons["quit"].collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # ===== USERNAME =====
        elif state == "username":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    if username.strip() == "":
                        error_msg = "Enter your name!"
                    else:
                        game = RacerGame(settings["difficulty"])
                        state = "game"

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    if len(username) < 12:
                        username += event.unicode

        # ===== SETTINGS =====
        elif state == "settings":
            if event.type == pygame.KEYDOWN:

                # звук
                if event.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]
                    pygame.mixer.music.set_volume(1 if settings["sound"] else 0)

                # сложность
                if event.key == pygame.K_d:
                    if settings["difficulty"] == "easy":
                        settings["difficulty"] = "medium"
                    elif settings["difficulty"] == "medium":
                        settings["difficulty"] = "hard"
                    else:
                        settings["difficulty"] = "easy"

                # сохранить
                if event.key == pygame.K_RETURN:
                    save_settings(settings)
                    state = "menu"

    # ===== DRAW =====

    if state == "menu":
        draw_menu(screen)

    elif state == "username":
        screen.fill((255,255,255))
        screen.blit(font.render("Enter name:", True, (0,0,0)), (120,230))
        screen.blit(font.render(username, True, (0,0,0)), (120,270))

        if error_msg:
            screen.blit(font.render(error_msg, True, (255,0,0)), (120,310))

    elif state == "game":
        game.update()
        game.draw(screen)
        game.draw_ui(screen, font)

        # GAME OVER 
        if game.lives <= 0:
            save_score(username, game.score, game.distance)
            state = "gameover"

        # FINISH 
        elif game.distance >= 500:
            save_score(username, game.score, game.distance)
            state = "finish"

    elif state == "gameover":
        screen.fill((255,255,255))

        screen.blit(font.render("GAME OVER", True, (255,0,0)), (130,230))
        screen.blit(font.render(f"Score: {game.score}", True, (0,0,0)), (140,270))
        screen.blit(font.render(f"Distance: {int(game.distance)}", True, (0,0,0)), (120,300))
        screen.blit(font.render(f"Coins: {game.coins}", True, (0,0,0)), (140,330))

        screen.blit(font.render("R - Retry", True, (0,0,0)), (140,380))
        screen.blit(font.render("M - Menu", True, (0,0,0)), (140,410))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game = RacerGame(settings["difficulty"])
            state = "game"
        if keys[pygame.K_m]:
            state = "menu"

    elif state == "finish":
        screen.fill((255,255,255))

        screen.blit(font.render("FINISH!", True, (0,200,0)), (150,230))
        screen.blit(font.render("You completed the race!", True, (0,0,0)), (70,270))

        screen.blit(font.render(f"Score: {game.score}", True, (0,0,0)), (140,300))
        screen.blit(font.render(f"Distance: {int(game.distance)}", True, (0,0,0)), (120,330))

        screen.blit(font.render("M - Menu", True, (0,0,0)), (150,380))

        if pygame.key.get_pressed()[pygame.K_m]:
            state = "menu"

    elif state == "leaderboard":
        screen.fill((255,255,255))
        scores = load_scores()

        y = 100
        for i, s in enumerate(scores):
            txt = f"{i+1}. {s['name']} - {s['score']} ({s['distance']})"
            screen.blit(font.render(txt, True, (0,0,0)), (40,y))
            y += 30

        screen.blit(font.render("Press M", True, (0,0,0)), (140,500))

        if pygame.key.get_pressed()[pygame.K_m]:
            state = "menu"

    elif state == "settings":
        screen.fill((255,255,255))

        screen.blit(font.render(f"Sound: {settings['sound']}", True, (0,0,0)), (80,200))
        screen.blit(font.render(f"Difficulty: {settings['difficulty']}", True, (0,0,0)), (80,240))

        screen.blit(font.render("S - toggle sound", True, (0,0,0)), (80,300))
        screen.blit(font.render("D - change difficulty", True, (0,0,0)), (80,340))
        screen.blit(font.render("ENTER - save", True, (0,0,0)), (80,380))

    pygame.display.update()
    clock.tick(60)