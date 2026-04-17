import pygame
import os
from player import Player

pygame.init()
pygame.mixer.init()

# window size
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# font for text
font = pygame.font.SysFont("Arial", 24)

# folder with music files
music_folder = "music"

# create playlist from mp3 and wav files
playlist = [
    os.path.join(music_folder, f)
    for f in os.listdir(music_folder)
    if f.endswith((".mp3", ".wav"))
]

# exit if no music found
if not playlist:
    print("No music files found")
    exit()

# create player object
player = Player(playlist)

running = True
clock = pygame.time.Clock()

while running:
    # background color
    screen.fill((30, 30, 30))

    # current track name
    track_name = os.path.basename(playlist[player.index])

    # track position info
    track_position = player.index + 1
    total_tracks = len(playlist)

    # text rendering
    text1 = font.render(f"Track: {track_name}", True, (255, 255, 255))
    text2 = font.render(f"Position: {track_position} / {total_tracks}", True, (255, 255, 255))
    text3 = font.render("P Play  B Pause  S Stop  N Next  V Prev  Q Quit", True, (200, 200, 200))

    # draw text on screen
    screen.blit(text1, (20, 80))
    screen.blit(text2, (20, 130))
    screen.blit(text3, (20, 180))

    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            running = False

        # key controls
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()   # play music

            elif event.key == pygame.K_b:
                player.pause()  # pause music

            elif event.key == pygame.K_s:
                player.stop()   # stop music

            elif event.key == pygame.K_n:
                player.next()   # next track

            elif event.key == pygame.K_v:
                player.prev()   # previous track

            elif event.key == pygame.K_q:
                running = False # quit program

    pygame.display.update()
    clock.tick(30)

pygame.quit()