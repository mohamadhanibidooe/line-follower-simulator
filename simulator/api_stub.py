# api_stub.py

_robot = None

def register_robot(robot):
    # store robot reference
    global _robot
    _robot = robot

def get_robot():
    return _robot

def read_line_sensors():
   # return list of 5 analog sensor values (0..4095)
    if _robot is None:
        return [0, 0, 0, 0, 0]

    readings, _ = _robot.read_line_sensors()
    return readings

def set_speed(speed):
    # legacy function (forward both motors)
    if _robot is not None:
        _robot.left_motor = speed
        _robot.right_motor = speed

def set_turn(turn):
    # legacy function (differential turn)
    if _robot is not None:
        _robot.left_motor = 50 - turn
        _robot.right_motor = 50 + turn

def set_motors(left, right):
    # Sets differential motor speeds
    if _robot is not None:
        _robot.left_motor = left
        _robot.right_motor = right
