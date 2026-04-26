# Global robot reference
_robot = None


def register_robot(robot):
    """Register robot instance so user code can access it."""
    global _robot
    _robot = robot


def get_robot():
    """Return the registered robot instance."""
    return _robot


# ---------------------------
# Helper API functions
# ---------------------------

def read_line_sensors():
    """Return line sensor readings (L, C, R)."""
    if _robot:
        readings, _ = _robot.read_line_sensors()
        return readings
    return [0, 0, 0]


def set_speed(speed):
    """Set robot forward speed."""
    if _robot:
        _robot.speed = speed


def set_turn(turn_speed):
    """Set robot turning speed."""
    if _robot:
        _robot.angle += turn_speed
