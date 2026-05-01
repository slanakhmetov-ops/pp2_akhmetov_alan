import pygame, json
from config import *
from game import *
import db

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 32)

MAX_LIVES = 3

COLORS = [
    (255,0,0),
    (0,255,0),
    (0,0,255)
]

# ---------- SETTINGS ----------
def load_settings():
    try:
        with open("settings.json","r") as f:
            return json.load(f)
    except:
        return {"snake_color": list(COLORS[0]), "grid": True}

def save_settings(settings):
    with open("settings.json","w") as f:
        json.dump(settings, f)

settings = load_settings()

try:
    color_index = COLORS.index(tuple(settings["snake_color"]))
except:
    color_index = 0
    settings["snake_color"] = list(COLORS[0])

# ---------- GAME STATE ----------
state = "menu"
username = ""
player_id = None

best_score = 0

snake = Snake()
food = Food()
poison = Poison()
power = None
obstacles = []

score = 0
level = 1
FPS = FPS_START
lives = MAX_LIVES

# power timer
power_end_time = 0
current_effect = None

# ---------- RESET ----------
def reset():
    global snake, food, poison, power
    snake = Snake()
    food = Food()
    poison = Poison()
    power = None
    food.generate(snake, obstacles)
    poison.generate(snake, obstacles)

def full_reset():
    global score, level, FPS, lives, obstacles
    score = 0
    level = 1
    FPS = FPS_START
    lives = MAX_LIVES
    obstacles = []
    reset()

full_reset()

# ---------- BUTTON ----------
def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (70,70,70), rect)
    pygame.draw.rect(screen, (200,200,200), rect, 2)
    screen.blit(font.render(text, True, (255,255,255)), (x+10,y+10))
    return rect

# ---------- LOOP ----------
running = True
saved = False

while running:
    screen.fill((0,0,0))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        # ---- username input ----
        if state == "menu_input" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and username:
                player_id = db.get_or_create_player(username)
                best_score = db.get_best_score(player_id)
                state = "game"
            elif e.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += e.unicode

        # ---- movement ----
        if state == "game" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1,0
            elif e.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1,0
            elif e.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0,-1
            elif e.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0,1

        # ---- restart ----
        if state == "gameover" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                full_reset()
                state = "menu"

    # ================= MENU =================
    if state == "menu":
        b1 = draw_button("Play",220,220,160,40)
        b2 = draw_button("Leaderboard",220,280,160,40)
        b3 = draw_button("Settings",220,340,160,40)
        b4 = draw_button("Quit",220,400,160,40)

        if click:
            if b1.collidepoint(mouse): state="menu_input"
            elif b2.collidepoint(mouse): state="leaderboard"
            elif b3.collidepoint(mouse): state="settings"
            elif b4.collidepoint(mouse): running=False

    # ================= INPUT =================
    elif state == "menu_input":
        screen.blit(font.render("Enter username:",True,(255,255,255)),(200,250))
        screen.blit(font.render(username,True,(0,255,0)),(250,300))

    # ================= SETTINGS =================
    elif state == "settings":

        for i,c in enumerate(COLORS):
            rect = pygame.Rect(200+i*80,200,50,50)
            pygame.draw.rect(screen,c,rect)
            if i == color_index:
                pygame.draw.rect(screen,(255,255,255),rect,3)

        if click:
            for i in range(3):
                rect = pygame.Rect(200+i*80,200,50,50)
                if rect.collidepoint(mouse):
                    color_index = i
                    settings["snake_color"] = list(COLORS[i])
                    save_settings(settings)

        grid_btn = draw_button(f"Grid: {settings['grid']}",220,320,160,40)
        if click and grid_btn.collidepoint(mouse):
            settings["grid"] = not settings["grid"]
            save_settings(settings)

        back = draw_button("Back",220,380,160,40)
        if click and back.collidepoint(mouse):
            state="menu"

    # ================= GAME =================
    elif state == "game":

        # 🔥 effect reset
        if current_effect and pygame.time.get_ticks() > power_end_time:
            FPS = FPS_START + (level - 1)
            current_effect = None

        head = snake.body[0]
        next_x = head.x + snake.dx
        next_y = head.y + snake.dy

        # collision
        if next_x < 0 or next_x >= WIDTH//CELL or next_y < 0 or next_y >= HEIGHT//CELL:
            lives -= 1
            if lives > 0:
                reset()
                continue
            else:
                state = "gameover"
                continue

        for seg in snake.body:
            if seg.x == next_x and seg.y == next_y:
                lives -= 1
                if lives > 0:
                    reset()
                    continue
                else:
                    state = "gameover"
                    continue

        for o in obstacles:
            if o.x == next_x and o.y == next_y:
                lives -= 1
                if lives > 0:
                    reset()
                    continue
                else:
                    state = "gameover"
                    continue

        snake.move()
        head = snake.body[0]

        # food
        if head.x == food.pos.x and head.y == food.pos.y:
            old = score
            score += food.value
            snake.body.append(Point(head.x, head.y))
            food.generate(snake, obstacles)

            if score // 5 > old // 5:
                level += 1
                FPS += 1
                obstacles = generate_obstacles(level, snake)

        # power spawn
        if power is None:
            power = PowerUp()
            power.generate(snake, obstacles)

        if power and power.expired():
            power = None

        # power pickup
        if power and head.x == power.pos.x and head.y == power.pos.y:

            if power.type == "speed":
                FPS += 3
                current_effect = "speed"
                power_end_time = pygame.time.get_ticks() + 5000

            elif power.type == "slow":
                FPS = max(1, FPS - 2)
                current_effect = "slow"
                power_end_time = pygame.time.get_ticks() + 5000

            elif power.type == "life":
                if lives < MAX_LIVES:
                    lives += 1

            power = None

        # draw
        snake.draw(screen, tuple(settings["snake_color"]))
        food.draw(screen)
        poison.draw(screen)

        if power:
            power.draw(screen)

        for o in obstacles:
            pygame.draw.rect(screen,(120,120,120),(o.x*CELL,o.y*CELL,CELL,CELL))

        if settings["grid"]:
            for x in range(0, WIDTH, CELL):
                pygame.draw.line(screen,(50,50,50),(x,0),(x,HEIGHT))
            for y in range(0, HEIGHT, CELL):
                pygame.draw.line(screen,(50,50,50),(0,y),(WIDTH,y))

        # 🔥 UI
        screen.blit(font.render(f"Score: {score}",True,(255,255,255)),(10,10))
        screen.blit(font.render(f"Best: {best_score}",True,(0,255,255)),(10,30))
        screen.blit(font.render(f"Lives: {lives}",True,(255,0,0)),(450,10))
        screen.blit(font.render(f"Level: {level}",True,(255,255,0)),(450,40))

    # ================= LEADERBOARD =================
    elif state == "leaderboard":
        data = db.get_top10()
        y=120
        for i,row in enumerate(data):
            screen.blit(font.render(f"{i+1}. {row[0]} - {row[1]}",True,(255,255,255)),(100,y))
            y+=30

        back = draw_button("Back",220,500,160,40)
        if click and back.collidepoint(mouse):
            state="menu"

    # ================= GAMEOVER =================
    elif state == "gameover":

        if not saved:
            db.save_game(player_id, score, level)

            if score > best_score:
                best_score = score

            saved = True

        screen.blit(big_font.render("GAME OVER",True,(255,0,0)),(200,250))
        screen.blit(font.render("Press R",True,(255,255,255)),(260,300))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()