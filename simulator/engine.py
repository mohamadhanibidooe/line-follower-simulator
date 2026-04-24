import pygame
from simulator.world import World
from simulator.robot import Robot

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Robot Simulator")
        self.clock = pygame.time.Clock()

        self.world = World()
        self.robot = Robot(100, 100, angle=0)

    def update(self):
        self.robot.update(self.world)

    def draw(self):
        self.screen.fill((220, 220, 220))
        self.world.draw(self.screen)
        self.robot.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
