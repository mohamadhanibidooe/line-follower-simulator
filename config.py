WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

ROBOT_SIZE = 25
ROBOT_SPEED = 2.0
ROBOT_TURN_SPEED = 2.0  # degrees per frame

# Noise level for each analog line sensor (0 = no noise)
# S1 = left-most sensor ... S5 = right-most sensor
SENSOR_ANALOG_NOISE = [
    800,   # S1 (left)
    50,   # S2
    30,   # S3 (center - usually most stable)
    50,   # S4
    80    # S5 (right)
]

