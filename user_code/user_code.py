from simulator.api_stub import read_line_sensors, set_motors

def setup():
    print("Line follower started (analog sensors)")

def loop(dt):
    # Read 5 analog sensors (0..4095)
    s = read_line_sensors()

    L2 = s[0]
    L1 = s[1]
    C  = s[2]
    R1 = s[3]
    R2 = s[4]

    base_speed = 45

    # Threshold for detecting black line
    # You may need to tune this value based on your track colors
    threshold = 1500

    # Strong left
    if L2 > threshold:
        set_motors(base_speed + 40, base_speed - 40)

    # Slight left
    elif L1 > threshold:
        set_motors(base_speed + 25, base_speed - 25)

    # Strong right
    elif R2 > threshold:
        set_motors(base_speed - 40, base_speed + 40)

    # Slight right
    elif R1 > threshold:
        set_motors(base_speed - 25, base_speed + 25)

    # Line centered or lost -> go straight
    else:
        set_motors(base_speed, base_speed)
