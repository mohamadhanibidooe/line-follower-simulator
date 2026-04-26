# user_code.py
# DEBUG: print raw sensor values

from simulator.api_stub import get_robot
timer = 0

def setup():
    print("[Setup] Debug sensor reader")


def loop(dt):
    global timer
    robot = get_robot()
    if robot is None:
        return

    timer += dt
    if timer >= 0.1:   # print 10 times per second
        timer = 0
        sensors, _ = robot.read_line_sensors()
        print("Sensors:", sensors)
