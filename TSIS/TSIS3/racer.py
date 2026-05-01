import pygame
import random

WIDTH, HEIGHT = 400, 600
FINISH_DISTANCE = 500

class RacerGame:
    def __init__(self, difficulty="medium"):

        # ===== DIFFICULTY =====
        if difficulty == "easy":
            self.base_speed = 4
            enemy_count = 2
        elif difficulty == "hard":
            self.base_speed = 7
            enemy_count = 5
        else:
            self.base_speed = 5
            enemy_count = 3

        self.speed = self.base_speed
        self.score = 0
        self.coins = 0
        self.distance = 0

        self.lives = 1
        self.shield = False
        self.active_power = None
        self.power_time = 0

        self.finished = False

        # PLAYER
        self.player_img = pygame.transform.scale(
            pygame.image.load("assets/Player.png"), (50, 90)
        )
        self.player_rect = self.player_img.get_rect(center=(200, 520))

        # BG
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/AnimatedStreet.png"),
            (WIDTH, HEIGHT)
        )

        # ENEMIES
        self.enemy_imgs = [
            "assets/enemy1.png",
            "assets/enemy2.png",
            "assets/enemy3.png",
            "assets/enemy4.jpg"
        ]
        self.enemies = [self.spawn_enemy() for _ in range(enemy_count)]

        # COINS (разные)
        self.coins_list = [self.spawn_coin()]

        # OBSTACLES
        self.obstacles = [self.spawn_obstacle()]

        # POWERUPS
        self.powerups = [self.spawn_powerup()]

    # ---------- SPAWN ----------
    def spawn_enemy(self):
        img = pygame.transform.scale(
            pygame.image.load(random.choice(self.enemy_imgs)), (50, 90)
        )
        rect = img.get_rect(center=(
            random.randint(40, WIDTH - 40),
            random.randint(-200, -100)
        ))
        return {"img": img, "rect": rect}

    def spawn_coin(self):
        surface = pygame.Surface((30, 30), pygame.SRCALPHA)

        value = random.choice([1, 3, 5])

        if value == 1:
            color = (255, 215, 0)   # yellow
        elif value == 3:
            color = (255, 0, 0)     # red
        else:
            color = (0, 255, 0)     # green

        pygame.draw.circle(surface, color, (15,15), 15)

        rect = surface.get_rect(center=(
            random.randint(40, WIDTH - 40),
            random.randint(-300, -100)
        ))

        return {"img": surface, "rect": rect, "value": value}

    def spawn_obstacle(self):
        img = pygame.transform.scale(
            pygame.image.load("assets/obstacle.png"), (40, 40)
        )
        rect = img.get_rect(center=(
            random.randint(40, WIDTH - 40),
            random.randint(-300, -100)
        ))
        return {"img": img, "rect": rect}

    def spawn_powerup(self):
        types = ["nitro", "shield", "repair"]
        t = random.choice(types)

        img = pygame.image.load(f"assets/{t}.png")
        img = pygame.transform.scale(img, (30, 30))

        rect = img.get_rect(center=(
            random.randint(40, WIDTH - 40),
            random.randint(-400, -150)
        ))

        return {"type": t, "img": img, "rect": rect}

    # ---------- UPDATE ----------
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.player_rect.left > 0:
            self.player_rect.x -= 8
        if keys[pygame.K_RIGHT] and self.player_rect.right < WIDTH:
            self.player_rect.x += 8

        # enemies
        for e in self.enemies:
            e["rect"].y += self.speed

            if e["rect"].top > HEIGHT:
                self.score += 1
                e.update(self.spawn_enemy())

            if self.player_rect.colliderect(e["rect"]):
                self.handle_hit()
                e.update(self.spawn_enemy())

        # coins
        for c in self.coins_list:
            c["rect"].y += self.speed

            if c["rect"].top > HEIGHT:
                c.update(self.spawn_coin())

            if self.player_rect.colliderect(c["rect"]):
                self.coins += c["value"]
                self.score += c["value"] * 5
                c.update(self.spawn_coin())

        # powerups
        for p in self.powerups:
            p["rect"].y += self.speed

            if p["rect"].top > HEIGHT:
                p.update(self.spawn_powerup())

            if self.player_rect.colliderect(p["rect"]):
                self.activate_power(p["type"])
                p.update(self.spawn_powerup())

        # nitro
        if self.active_power == "nitro":
            self.speed = self.base_speed + 5
            if pygame.time.get_ticks() - self.power_time > 4000:
                self.speed = self.base_speed
                self.active_power = None

        # distance
        self.distance += 0.1
        if self.distance >= FINISH_DISTANCE:
            self.finished = True

    def handle_hit(self):
        if self.shield:
            self.shield = False
        elif self.lives > 0:
            self.lives -= 1
        else:
            self.finished = True

        self.player_rect.center = (200, 520)

    def activate_power(self, power):
        if power == "shield":
            self.shield = True
        elif power == "repair":
            self.lives += 1
        elif power == "nitro":
            self.active_power = "nitro"
            self.power_time = pygame.time.get_ticks()

    # ---------- DRAW ----------
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        for e in self.enemies:
            screen.blit(e["img"], e["rect"])

        for c in self.coins_list:
            screen.blit(c["img"], c["rect"])

        for p in self.powerups:
            screen.blit(p["img"], p["rect"])

        screen.blit(self.player_img, self.player_rect)

    def draw_ui(self, screen, font):
        shield = "ON" if self.shield else "OFF"

        screen.blit(font.render(f"Score: {self.score}", True, (0,0,0)), (10,10))
        screen.blit(font.render(f"Coins: {self.coins}", True, (0,0,0)), (10,40))
        screen.blit(font.render(f"Distance: {int(self.distance)} / {FINISH_DISTANCE}", True, (0,0,0)), (10,70))

        screen.blit(font.render(f"Lives: {self.lives}", True, (0,0,0)), (10,100))
        screen.blit(font.render(f"Shield: {shield}", True, (0,0,0)), (10,130))
        screen.blit(font.render(f"Power: {self.active_power}", True, (0,0,0)), (10,160))