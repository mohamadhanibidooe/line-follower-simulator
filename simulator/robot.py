import pygame
import math

class Robot:
    def __init__(self, x, y,angle=0):
        self.x = x
        self.y = y
        self.angle = angle

        self.speed = 0
        self.turn_speed = 0

        self.max_speed = 3
        self.acc = 0.2
        self.turn_rate = 0.05

        # distance of sensors from robot center
        self.sensor_offset = 35
        self.sensor_spacing = 20

    # ---------------------------------------------------------
    # Handle keyboard input
    # ---------------------------------------------------------
    def handle_input(self, keys):

        # rotate robot
        if keys[pygame.K_LEFT]:
            self.angle -= self.turn_rate
        if keys[pygame.K_RIGHT]:
            self.angle += self.turn_rate

        # move forward / backward
        if keys[pygame.K_UP]:
            self.speed += self.acc
        elif keys[pygame.K_DOWN]:
            self.speed -= self.acc
        else:
            # natural friction
            self.speed *= 0.92

        # clamp speed
        self.speed = max(-self.max_speed, min(self.speed, self.max_speed))

    # ---------------------------------------------------------
    # Update robot position
    # ---------------------------------------------------------
    def update(self, world):

        # move in direction of angle
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        # keep world reference for sensor reading
        self.world = world

    # ---------------------------------------------------------
    # Read line sensors (Left, Center, Right)
    # ---------------------------------------------------------
    def read_line_sensors(self):

        # sensor positions relative to robot
        points_local = [
            (self.sensor_offset, -self.sensor_spacing),  # left
            (self.sensor_offset, 0),                     # center
            (self.sensor_offset, self.sensor_spacing),   # right
        ]

        readings = []
        positions = []

        for px, py in points_local:

            # convert local coordinates to world coordinates
            wx = self.x + px * math.cos(self.angle) - py * math.sin(self.angle)
            wy = self.y + px * math.sin(self.angle) + py * math.cos(self.angle)

            ix, iy = int(wx), int(wy)
            positions.append((ix, iy))

            # check if sensor is inside world
            if 0 <= ix < self.world.surface.get_width() and 0 <= iy < self.world.surface.get_height():

                color = self.world.surface.get_at((ix, iy))

                # detect black line
                readings.append(1 if color == (0, 0, 0, 255) else 0)

            else:
                readings.append(0)

        return readings, positions

    # ---------------------------------------------------------
    # Draw robot
    # ---------------------------------------------------------
    def draw(self, screen):

        body_w, body_h = 80, 50
        wheel_w, wheel_h = 20, 10

        # create a surface for the robot
        surf_w = body_w + 50
        surf_h = body_h + 50
        robot_surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)

        cx, cy = surf_w // 2, surf_h // 2

        # draw robot body (rounded rectangle)
        body = pygame.Rect(0, 0, body_w, body_h)
        body.center = (cx, cy)
        pygame.draw.rect(robot_surf, (0,120,255), body, border_radius=12)
        pygame.draw.rect(robot_surf, (0,0,0), body, 2, border_radius=12)

        # draw top wheel
        wt = pygame.Rect(0,0,wheel_w,wheel_h)
        wt.center = (cx, cy - body_h//2 - wheel_h//2)
        pygame.draw.rect(robot_surf, (0,0,0), wt, border_radius=4)

        # draw bottom wheel
        wb = pygame.Rect(0,0,wheel_w,wheel_h)
        wb.center = (cx, cy + body_h//2 + wheel_h//2)
        pygame.draw.rect(robot_surf, (0,0,0), wb, border_radius=4)

        # 🚫 removed: front red sensor area
        # (The following 4 lines were deleted)
        #
        # sensor_w, sensor_h = 40, 20
        # sensor_rect = pygame.Rect(cx + body_w//2 - 2, cy - sensor_h//2, sensor_w, sensor_h)
        # pygame.draw.ellipse(robot_surf, (200,0,0), sensor_rect)

        # rotate whole robot surface
        rotated = pygame.transform.rotate(robot_surf, -math.degrees(self.angle))

        rect = rotated.get_rect(center=(self.x, self.y))

        screen.blit(rotated, rect)

        # draw sensor points for debugging
        readings, positions = self.read_line_sensors()

        for (ix, iy), r in zip(positions, readings):
            color = (0,255,0) if r else (255,0,0)
            pygame.draw.circle(screen, color, (ix, iy), 4)
