from simulator.api_stub import read_line_sensors, set_motors

def setup():
    print("Line follower started")

def loop(dt):

    s = read_line_sensors()

    L2 = s[0]
    L1 = s[1]
    C  = s[2]
    R1 = s[3]
    R2 = s[4]

    base = 45

    # strong left
    if L2:
        set_motors(base + 40, base - 40)

    # slight left
    elif L1:
        set_motors(base +25, base - 25)

    # strong right
    elif R2:
        set_motors(base - 40, base + 40)

    # slight right
    elif R1:
        set_motors(base - 25, base + 25)

    
    # line lost
    else:
        set_motors(base, base)
