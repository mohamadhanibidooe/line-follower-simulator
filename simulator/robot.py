import pygame
import math

class Robot:
    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0
        self.size = 20

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05
        if keys[pygame.K_UP]:
            self.speed = 2
        elif keys[pygame.K_DOWN]:
            self.speed = -2
        else:
            self.speed = 0

    def update(self, world):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0, 100, 255),
            pygame.Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)
        )
