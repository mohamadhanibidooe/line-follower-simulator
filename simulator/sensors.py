import math
import pygame
from config import ULTRASONIC_MAX_DISTANCE

def cast_ray(x, y, angle_deg, walls):
    angle = math.radians(angle_deg)
    dx = math.cos(angle)
    dy = math.sin(angle)

    for dist in range(0, ULTRASONIC_MAX_DISTANCE, 2):
        px = x + dx * dist
        py = y + dy * dist

        point = pygame.Rect(px, py, 2, 2)
        for wall in walls:
            if wall.colliderect(point):
                return dist
    return ULTRASONIC_MAX_DISTANCE
