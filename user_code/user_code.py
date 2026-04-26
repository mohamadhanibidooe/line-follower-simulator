# user_code.py
# motor test
# comments in English

from simulator.api_stub import set_motors

time_passed = 0

def setup():
    print("Motor test started")

def loop(dt):
    global time_passed

    # accumulate time
    time_passed += dt

    # forward
    if time_passed < 3:
        set_motors(50, 50)

    # turn right
    elif time_passed < 6:
        set_motors(30, 70)

    # turn left
    elif time_passed < 9:
        set_motors(70, 30)

    # stop
    else:
        set_motors(0, 0)
