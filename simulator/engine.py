import pygame
import time
from simulator.world import World
from simulator.robot import Robot
from simulator.api_stub import register_robot

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Robot Simulator")
        self.clock = pygame.time.Clock()

        self.world = World(width, height)

        # Robot spawn point
        self.robot = Robot(100, 100, angle=0)
        register_robot(self.robot)

        # timer flags
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

    def update(self):
        dt = self.clock.tick(60) / 1000.0

        # UPDATE WORLD
        self.world.update(dt)

        # UPDATE TIMER
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            # print("Time:", round(self.elapsed_time, 2))

        # UPDATE ROBOT
        # robot only moves when active
        if self.robot.active:
            self.robot.update(self.world)
        else:
            self.robot.set_motors(0, 0)

        return dt

    def draw(self):
        self.screen.fill((220, 220, 220))
        self.world.draw(self.screen)
        self.robot.draw(self.screen)

        # draw timer text
        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f"Time: {self.elapsed_time:.2f}", True, (0, 0, 0))
        self.screen.blit(time_text, (10, 10))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            # ----- KEY EVENTS -----
            if event.type == pygame.KEYDOWN:

                # START
                if event.key == pygame.K_s:
                    self.timer_running = True
                    self.start_time = time.time()
                    self.robot.active = True
                    print("START pressed")

                # STOP
                if event.key == pygame.K_p:
                    self.timer_running = False
                    self.robot.active = False
                    self.robot.set_motors(0, 0)
                    print("STOP pressed")

                # RESET
                if event.key == pygame.K_r:
                    self.timer_running = False
                    self.elapsed_time = 0
                    self.robot.active = False
                    self.robot.set_motors(0, 0)
                    self.robot.reset_position()
                    print("RESET pressed")

        return True
