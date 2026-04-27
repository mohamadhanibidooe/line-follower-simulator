import pygame
import time
import math

from simulator.world import World
from simulator.robot import Robot
from simulator.api_stub import register_robot


class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Robot Simulator")
        self.clock = pygame.time.Clock()

        # Load world / track
        self.world = World(width, height)

        # Initial robot (will be overwritten by runner)
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
    # Handle window events (QUIT, etc.)
    # -------------------------------------------------------------
    def handle_events(self):
        events = pygame.event.get()

        for event in events:

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

            # Start simulation
                if event.key == pygame.K_s:
                    self.robot.active = True
                    self.timer_running = True
                    self.start_time = time.time()
                    print("START")

                # Stop simulation
                if event.key == pygame.K_p:
                    self.robot.active = False
                    self.timer_running = False
                    print("STOP")

                # Reset simulation
                if event.key == pygame.K_r:
                    # Position reset
                    if hasattr(self, "spawn_point"):
                        self.robot.x, self.robot.y = self.spawn_point
                    else:
                        self.robot.x, self.robot.y = self.world.start_point
                
                    # Angle reset
                    if hasattr(self, "spawn_angle"):
                        self.robot.angle = math.radians(self.spawn_angle)
                    else:
                        self.robot.angle = 0

                    # Timer + state reset
                    self.robot.active = False
                    self.timer_running = False
                    self.elapsed_time = 0
                    self.lap_times = []
                    self.last_lap_time = 0

                    print("RESET to user-chosen spawn")
        return True


    # -------------------------------------------------------------
    # Set the finish/start line rectangle around spawn point
    # -------------------------------------------------------------
    def set_finish_line(self, spawn_point):
        x, y = spawn_point
        size = 30

        self.finish_line = pygame.Rect(
            x - size // 2,
            y - size // 2,
            size,
            size
        )

    # -------------------------------------------------------------
    # Draw spawn selection screen (position + angle arrow)
    # -------------------------------------------------------------
    def draw_spawn_selection(self, spawn_point, angle_deg):
        # Fill background
        self.screen.fill((220, 220, 220))

        # Draw world
        self.world.draw(self.screen)

        # Draw spawn point (blue circle)
        if spawn_point is not None:
            pygame.draw.circle(self.screen, (0, 0, 255), spawn_point, 6)

        # Draw angle arrow (red)
        if spawn_point is not None and angle_deg is not None:
            rad = math.radians(angle_deg)
            length = 50
            end_x = spawn_point[0] + math.cos(rad) * length
            end_y = spawn_point[1] + math.sin(rad) * length

            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                spawn_point,
                (end_x, end_y),
                3
            )

        # UI text
        font = pygame.font.SysFont(None, 30)

        if angle_deg is None:
            msg = "Click to choose spawn point, then press ENTER"
        else:
            msg = "Use LEFT/RIGHT (or Q/E) to rotate, ENTER to confirm"

        text = font.render(msg, True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()

    # -------------------------------------------------------------
    # Update engine (robot, world, lap timer)
    # -------------------------------------------------------------
    def update(self):
        dt = self.clock.tick(60) / 1000.0  # delta time in seconds

        # Update world
        self.world.update(dt)

        # Update timer
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time

        # Update robot physics
        if self.robot.active:
            self.robot.update(self.world)
        else:
            self.robot.set_motors(0, 0)

        # Lap detection
        if self.finish_line and self.timer_running:

            # robot hitbox (small square around center)
            robot_hitbox = pygame.Rect(
                self.robot.x - 5,
                self.robot.y - 5,
                10,
                10
            )

            in_line = self.finish_line.colliderect(robot_hitbox)

            if in_line and not self.robot_prev_in_line:
                lap_time = self.elapsed_time - self.last_lap_time
                self.last_lap_time = self.elapsed_time

                if lap_time > 0.5:  # ignore instant hits
                    self.lap_times.append(lap_time)
                    print(f"Lap {len(self.lap_times)}: {lap_time:.2f}s")

            self.robot_prev_in_line = in_line

        return dt

    # -------------------------------------------------------------
    # Draw everything
    # -------------------------------------------------------------
    def draw(self):
        self.screen.fill((220, 220, 220))

        # Draw world
        self.world.draw(self.screen)

        # Draw robot
        self.robot.draw(self.screen)

        # Draw finish line
        if self.finish_line:
            pygame.draw.rect(self.screen, (255, 0, 0), self.finish_line, 2)

        # Timer text
        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f"Time: {self.elapsed_time:.2f}", True, (0, 0, 0))
        self.screen.blit(time_text, (10, 10))

        # Lap times
        font_lap = pygame.font.SysFont(None, 26)
        y = 50

        for i, lap in enumerate(self.lap_times[-5:], start=1):
            lap_text = font_lap.render(f"Lap {i}: {lap:.2f}s", True, (0, 0, 0))
            self.screen.blit(lap_text, (10, y))
            y += 25

        pygame.display.flip()
