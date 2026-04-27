#robot.py
import pygame
import math
from simulator.sensors import LineSensorArray
from simulator.motors import DifferentialDriveMotors
from config import ROBOT_MAX_SPEED

class Robot:
    def __init__(self, x, y,angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.active = False
        self.spawn_x = x
        self.spawn_y = y
        self.spawn_angle = angle
        
        # max linear speed (pixels per frame)
        self.max_speed = ROBOT_MAX_SPEED

        self.motors = DifferentialDriveMotors(self.max_speed)

        self.line_sensors = LineSensorArray(self)

        # how strong turning effect is
        self.turn_factor = 0.04

        # distance of sensors from robot center
        self.sensor_offset = 35
        self.sensor_spacing = 8

    def set_motors(self, left_percent, right_percent):
        # clamp motor values between 0 and 100
        self.left_motor = max(0, min(100, left_percent))
        self.right_motor = max(0, min(100, right_percent))

   
    # ---------------------------------------------------------
    # Update robot position
    # ---------------------------------------------------------
    def update(self, world):

        # keep world reference for sensor reading
        self.world = world

        # convert motor percent to commanded speed
        cmd_left = (self.left_motor / 100.0) * self.max_speed
        cmd_right = (self.right_motor / 100.0) * self.max_speed

        # send command to motor model
        self.motors.set_speeds(cmd_left, cmd_right)

        # get real motor speeds (with noise / bias)
        left_speed, right_speed = self.motors.get_speeds()

        # forward speed = average of both motors
        forward = (left_speed + right_speed) / 2

        # rotation based on motor difference
        rotation = (right_speed - left_speed) * self.turn_factor

        # update angle
        self.angle += rotation

        # move robot
        self.x += math.cos(self.angle) * forward
        self.y += math.sin(self.angle) * forward



    # ---------------------------------------------------------
    # Read line sensors (5 sensors)
    # ---------------------------------------------------------
    def read_line_sensors(self):
        return self.line_sensors.read()



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
    def reset_position(self):
        self.x = self.spawn_x
        self.y = self.spawn_y
        self.angle = self.spawn_angle
