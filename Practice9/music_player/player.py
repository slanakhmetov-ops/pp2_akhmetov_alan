import pygame

class Player:
    def __init__(self, playlist):
        self.playlist = playlist  # list of songs
        self.index = 0            # current track index
        self.paused = False       # pause state

    def load(self):
        # load current track
        pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        # resume if paused
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            # otherwise start playing
            self.load()
            pygame.mixer.music.play()

    def pause(self):
        # pause playback
        pygame.mixer.music.pause()
        self.paused = True

    def stop(self):
        # stop playback completely
        pygame.mixer.music.stop()
        self.paused = False

    def next(self):
        # go to next track (loop)
        self.index = (self.index + 1) % len(self.playlist)
        self.paused = False
        self.play()

    def prev(self):
        # go to previous track (loop)
        self.index = (self.index - 1) % len(self.playlist)
        self.paused = False
        self.play()