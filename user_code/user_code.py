from simulator.api_stub import read_line_sensors, set_speed, set_turn


def setup():
    print("Line follower ready!")


def loop(dt):
    # Read sensors: [Left, Center, Right]
    left, center, right = read_line_sensors()

    base_speed = 2
    turn_strength = 0.05

    # Default forward movement
    set_speed(base_speed)

    # Line following logic
    if center == 1:
        # Go straight
        set_turn(0)

    elif left == 1:
        # Turn left
        set_turn(-turn_strength)

    elif right == 1:
        # Turn right
        set_turn(turn_strength)

    else:
        # If no line detected, slow down
        set_turn(0)
