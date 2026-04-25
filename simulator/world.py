import pygame

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 255, 255))

        self.draw_track()
    def get_width(self):
        return self.surface.get_width()

    def get_height(self):
        return self.surface.get_height()


    def draw_track(self):
        pygame.draw.line(
            self.surface,
            (0, 0, 0),
            (100, 300),
            (700, 300),
            8
        )

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
