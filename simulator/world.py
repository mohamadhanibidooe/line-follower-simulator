import pygame
import os


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # create world surface
        self.surface = pygame.Surface((self.width, self.height))

        # load track image
        track_path = os.path.join(os.path.dirname(__file__), "track.png")
        self.track_image = pygame.image.load(track_path).convert()

        # scale image to world size
        self.track_image = pygame.transform.smoothscale(
            self.track_image,
            (self.width, self.height)
        )

        # draw track to world
        self.surface.blit(self.track_image, (0, 0))

        # -------------------------------
        # Start point (Robot spawn point)
        # Example: (100, 200)
        # Change this to whatever point you want
        # -------------------------------
        self.start_point = (150, 320)  # <-- EDIT THIS VALUE

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))

    def get_color(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return (255, 255, 255)

        return self.surface.get_at((int(x), int(y)))
