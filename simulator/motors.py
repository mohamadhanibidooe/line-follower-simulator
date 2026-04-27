import random
from config import MOTOR_COMMAND_NOISE, MOTOR_BIAS, MOTOR_GAIN_ERROR


class DifferentialDriveMotors:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.left_speed = 0.0
        self.right_speed = 0.0

    def set_speeds(self, left, right):
        # Add constant motor bias
        left = left + MOTOR_BIAS["left"]
        right = right + MOTOR_BIAS["right"]

        # Add command noise
        left += random.uniform(-MOTOR_COMMAND_NOISE, MOTOR_COMMAND_NOISE)
        right += random.uniform(-MOTOR_COMMAND_NOISE, MOTOR_COMMAND_NOISE)

        # Add multiplicative gain error
        left *= (1.0 + random.uniform(-MOTOR_GAIN_ERROR, MOTOR_GAIN_ERROR))
        right *= (1.0 + random.uniform(-MOTOR_GAIN_ERROR, MOTOR_GAIN_ERROR))

        # Clamp speeds to motor limits
        left = max(-self.max_speed, min(self.max_speed, left))
        right = max(-self.max_speed, min(self.max_speed, right))

        self.left_speed = left
        self.right_speed = right

    def get_speeds(self):
        return self.left_speed, self.right_speed
