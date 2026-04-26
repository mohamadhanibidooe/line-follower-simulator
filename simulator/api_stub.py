# api_stub.py

_robot = None

def register_robot(robot):
    global _robot
    _robot = robot

def get_robot():
    return _robot

def read_line_sensors():
    # return list of sensor values
    if _robot is None:
        return [0, 0, 0, 0, 0]
    return _robot.read_line_sensors()

def set_speed(speed):
    # old function (you can keep it if needed)
    if _robot is not None:
        _robot.left_motor = speed
        _robot.right_motor = speed

def set_turn(turn):
    # old function (optional)
    if _robot is not None:
        _robot.left_motor = 50 - turn
        _robot.right_motor = 50 + turn


def set_motors(left, right):
    # Sets differential motor speeds
    # comments in English as user requested
    if _robot is not None:
        _robot.left_motor = left
        _robot.right_motor = right
