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

    import pygame
import math

class Robot:
    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0
        self.size = 25

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
        #tri point degry
        front = (
            self.x + math.cos(self.angle) * self.size,
            self.y + math.sin(self.angle) * self.size
        )

        left = (
            self.x + math.cos(self.angle + 2.5) * self.size,
            self.y + math.sin(self.angle + 2.5) * self.size
        )

        right = (
            self.x + math.cos(self.angle - 2.5) * self.size,
            self.y + math.sin(self.angle - 2.5) * self.size
        )

        #draw body
        pygame.draw.polygon(screen, (0, 100, 255), [front, left, right])

        #draw wils    
        wheel_offset = 15
        wheel_left = (
            self.x + math.cos(self.angle + 1.57) * wheel_offset,
            self.y + math.sin(self.angle + 1.57) * wheel_offset
        )
        wheel_right = (
            self.x + math.cos(self.angle - 1.57) * wheel_offset,
            self.y + math.sin(self.angle - 1.57) * wheel_offset
        )

        pygame.draw.circle(screen, (50, 50, 50), wheel_left, 5)
        pygame.draw.circle(screen, (50, 50, 50), wheel_right, 5)

