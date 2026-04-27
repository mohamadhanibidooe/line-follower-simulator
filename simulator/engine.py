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

        # Robot spawn (will be overwritten by runner)
        self.robot = Robot(100, 100, angle=0)
        register_robot(self.robot)

        # Timer system
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Lap system
        self.finish_line = None
        self.lap_times = []
        self.last_lap_time = 0
        self.robot_prev_in_line = False

    # -------------------------------------------------------------
    # Set finish/start line based on spawn point from runner
    # -------------------------------------------------------------
    def set_finish_line(self, spawn_point):
        # spawn_point = (x, y)
        x, y = spawn_point
        size = 30  # finish line square size

        # Create rectangle centered at spawn
        self.finish_line = pygame.Rect(
            x - size // 2,
            y - size // 2,
            size,
            size
        )

    # -------------------------------------------------------------
    # Update Loop
    # -------------------------------------------------------------
    def update(self):
        dt = self.clock.tick(60) / 1000.0

        # UPDATE WORLD
        self.world.update(dt)

        # UPDATE TIMER
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time

        # UPDATE ROBOT
        if self.robot.active:
            self.robot.update(self.world)
        else:
            self.robot.set_motors(0, 0)

        # -------------------------------------------------------------
        # LAP DETECTION
        # -------------------------------------------------------------
        if self.finish_line and self.timer_running:

            # Small detection rectangle around robot
            robot_hitbox = pygame.Rect(
                self.robot.x - 5,
                self.robot.y - 5,
                10,
                10
            )

            in_line = self.finish_line.colliderect(robot_hitbox)

            # Only count when robot ENTERS the finish area
            if in_line and not self.robot_prev_in_line:

                lap_time = self.elapsed_time - self.last_lap_time
                self.last_lap_time = self.elapsed_time

                # Prevent instant false lap at the start
                if lap_time > 0.5:
                    self.lap_times.append(lap_time)
                    print(f"Lap {len(self.lap_times)}: {lap_time:.2f}s")

            self.robot_prev_in_line = in_line

        return dt

    # -------------------------------------------------------------
    # Draw Everything
    # -------------------------------------------------------------
    def draw(self):
        self.screen.fill((220, 220, 220))
        self.world.draw(self.screen)
        self.robot.draw(self.screen)

        # draw finish line
        if self.finish_line:
            pygame.draw.rect(self.screen, (255, 0, 0), self.finish_line, 2)

        # draw timer
        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f"Time: {self.elapsed_time:.2f}", True, (0, 0, 0))
        self.screen.blit(time_text, (10, 10))

        # draw lap times
        font_lap = pygame.font.SysFont(None, 26)
        y = 50
        for i, lap in enumerate(self.lap_times[-5:], start=1):
            lap_text = font_lap.render(f"Lap {i}: {lap:.2f}s", True, (0, 0, 0))
            self.screen.blit(lap_text, (10, y))
            y += 25

        pygame.display.flip()

    # -------------------------------------------------------------
    # Event Handler
    # -------------------------------------------------------------
    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            # KEYBOARD
            if event.type == pygame.KEYDOWN:

                # START (S)
                if event.key == pygame.K_s:
                    self.timer_running = True
                    self.start_time = time.time() - self.elapsed_time
                    self.robot.active = True
                    print("START pressed")

                # STOP (P)
                if event.key == pygame.K_p:
                    self.timer_running = False
                    self.robot.active = False
                    self.robot.set_motors(0, 0)
                    print("STOP pressed")

                # RESET (R)
                if event.key == pygame.K_r:
                    self.timer_running = False
                    self.elapsed_time = 0
                    self.last_lap_time = 0
                    self.lap_times.clear()

                    self.robot.active = False
                    self.robot.set_motors(0, 0)
                    self.robot.reset_position()

                    print("RESET pressed")

        return True
