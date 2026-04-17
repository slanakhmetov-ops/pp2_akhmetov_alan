import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)

        # center of the screen (clock center)
        self.center = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        
        # get path to images folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "images")

        # load and scale background (clock face)
        self.bg = pygame.image.load(os.path.join(img_dir, "cipherblat.png"))
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # load and scale Mickey body
        self.mickey_body = pygame.image.load(os.path.join(img_dir, "mickey.png")).convert_alpha()
        self.mickey_body = pygame.transform.scale(self.mickey_body, (380, 500)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)
        
        # load and scale minute hand (right hand)
        self.min_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_right_centered.png")).convert_alpha()
        self.min_hand_orig = pygame.transform.scale(self.min_hand_orig, (200, 300))
        
        # load and scale second hand (left hand)
        self.sec_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_left_centered.png")).convert_alpha()
        self.sec_hand_orig = pygame.transform.scale(self.sec_hand_orig, (190, 280))

    def blit_rotate_pivot(self, surface, image, pos, originPos, angle):
        # place image so that pivot point is at the center
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        
        # vector from center of image to pivot
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
        
        # rotate this offset
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        
        # calculate new center after rotation
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        
        # rotate image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
        
        # draw rotated image
        surface.blit(rotated_image, rotated_image_rect)

    def render(self, surface):
        # draw background and Mickey body
        surface.blit(self.bg, (0, 0))
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        # get current time
        now = datetime.datetime.now()
        
        # calculate angles (6 degrees per unit)
        min_angle = -(now.minute * 6)
        sec_angle = -(now.second * 6)

        # pivot for minute hand (shoulder point)
        min_pivot_x = self.min_hand_orig.get_width() // 2
        min_pivot_y = int(self.min_hand_orig.get_height() * 0.85)

        # pivot for second hand (shoulder point)
        sec_pivot_x = self.sec_hand_orig.get_width() // 2
        sec_pivot_y = int(self.sec_hand_orig.get_height() * 0.85)

        # draw hands
        self.blit_rotate_pivot(surface, self.min_hand_orig, self.center, (min_pivot_x, min_pivot_y), min_angle)
        self.blit_rotate_pivot(surface, self.sec_hand_orig, self.center, (sec_pivot_x, sec_pivot_y), sec_angle)