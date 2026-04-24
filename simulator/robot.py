import pygame
import math
from config import (
    ROBOT_SPEED,
    ROBOT_TURN_SPEED,
    ROBOT_SIZE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

class Robot:
    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.angle = angle  # degrees

    def update(self, world, dt=1.0):
        keys = pygame.key.get_pressed()

        # --- Rotation ---
        if keys[pygame.K_LEFT]:
            self.angle -= ROBOT_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.angle += ROBOT_TURN_SPEED * dt

        # --- Movement ---
        dx = 0
        dy = 0

        if keys[pygame.K_UP]:
            dx += ROBOT_SPEED * math.cos(math.radians(self.angle)) * dt
            dy += ROBOT_SPEED * math.sin(math.radians(self.angle)) * dt

        if keys[pygame.K_DOWN]:
            dx -= ROBOT_SPEED * math.cos(math.radians(self.angle)) * dt
            dy -= ROBOT_SPEED * math.sin(math.radians(self.angle)) * dt

        # Move
        self.x += dx
        self.y += dy

        # --- Prevent leaving screen ---
        half = ROBOT_SIZE / 2
        self.x = max(half, min(WINDOW_WIDTH - half, self.x))
        self.y = max(half, min(WINDOW_HEIGHT - half, self.y))

    def draw(self, screen):
        rect = pygame.Rect(0, 0, ROBOT_SIZE, ROBOT_SIZE)
        rect.center = (self.x, self.y)
        pygame.draw.rect(screen, (0, 100, 255), rect)
