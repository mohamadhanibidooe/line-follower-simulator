# user_code.py
# simple smooth 5-sensor line follower
# comments in English

from simulator.api_stub import get_robot

BASE_SPEED = 3

def setup():
    print("Line follower running")


def loop(dt):
    robot = get_robot()
    if robot is None:
        return

    sensors, _ = robot.read_line_sensors()
    far_left, left, center, right, far_right = sensors

    # robot always moves forward
    robot.speed = BASE_SPEED

    turn = 0

    # calculate steering
    if far_left:
        turn = -2
    elif left:
        turn = -1
    elif right:
        turn = 1
    elif far_right:
        turn = 2
    else:
        turn = 0

    # apply smooth steering
    robot.angle += turn
