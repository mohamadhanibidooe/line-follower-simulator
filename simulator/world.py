import pygame

class World:
    def __init__(self):
        self.walls = [
            pygame.Rect(50, 50, 700, 10),
            pygame.Rect(50, 540, 700, 10),
            pygame.Rect(50, 50, 10, 500),
            pygame.Rect(740, 50, 10, 500)
        ]

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, (0, 0, 0), wall)
