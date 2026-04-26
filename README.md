# Line Follower Robot Simulator

A simple **Python + Pygame** simulator for experimenting with **line follower robot algorithms**.

Instead of needing a physical robot, you can write your control algorithm and test it inside a virtual environment with simulated sensors and motors.

This project is useful for:

- Learning robotics fundamentals
- Practicing line‑following algorithms
- Testing logic before deploying to real robots
- Teaching programming and robotics

---

# Features

- Differential drive robot simulation
- 5 line sensors
- Custom robot control code
- Adjustable spawn position
- Real‑time simulation using pygame
- Simple API for motor and sensor control

---

# Requirements

- Python **3.9+**
- **pygame**

Install pygame:

```bash
pip install pygame
```

---

# Running the Simulator

Run the main program:

```bash
python runner.py
```

When the program starts it may ask for:

```text
Enter robot start X:
Enter robot start Y:
```

If you press **Enter**, the default spawn position defined in `world.py` will be used.

---

# Project Structure

```text
line-follower-simulator/
│
├── config.py
├── runner.py
├── user_code
    ├── user_code.py
├── track.png
│
└── simulator/
    ├── engine.py
    ├── robot.py
    ├── world.py
    ├── __init__.py
    ├── sensors.py
    ├── track.png
    └── api_stub.py
```

### runner.py
Main entry point that starts the simulator.

### user_code.py
Where you write your **robot algorithm**.

### track.png
Image of the track that the robot follows.

### simulator/
Core simulation engine.

---

# How the Simulator Works

The simulator runs a continuous loop:

1. Handle window events
2. Calculate delta time (`dt`)
3. Update world state
4. Update robot physics
5. Update sensors
6. Run your algorithm (`user_code.py`)
7. Render everything

Your control logic runs every frame inside `loop(dt)`.

---

# Writing Robot Code

All robot logic is written in:

```
user_code.py
```

The simulator automatically loads and runs this file.

---

# user_code.py Structure

```python
from simulator.api_stub import read_line_sensors, set_motors


def setup():
    print("Robot started")


def loop(dt):
    sensors = read_line_sensors()

    if sensors[2]:
        set_motors(50, 50)
    else:
        set_motors(0, 0)
```

---

# setup()

Runs **once** when the simulator starts.

Example:

```python
def setup():
    print("Algorithm initialized")
```

---

# loop(dt)

Runs **every frame**.

Parameter:

```
dt = time passed since previous frame (seconds)
```

Example:

```python
def loop(dt):
    sensors = read_line_sensors()

    if sensors[2] == 1:
        set_motors(60, 60)
    else:
        set_motors(30, 60)
```

---

# API Reference

Import the API:

```python
from simulator.api_stub import read_line_sensors, set_motors
```

---

# read_line_sensors()

Reads the five line sensors.

```python
sensors = read_line_sensors()
```

Output example:

```text
[0, 1, 1, 0, 0]
```

Sensor order:

```text
[L2, L1, C, R1, R2]
```

Meaning:

- L2 = far left
- L1 = left
- C  = center
- R1 = right
- R2 = far right

Values:

```
1 = line detected
0 = no line
```

---

# set_motors(left, right)

Controls the robot motors.

```python
set_motors(left_speed, right_speed)
```

Speed range:

```
0 → 100
```

Examples:

```python
set_motors(50, 50)   # move forward
set_motors(30, 70)   # turn left
set_motors(70, 30)   # turn right
set_motors(0, 0)     # stop
```

---

# Example Line Follower Algorithm

```python
from simulator.api_stub import read_line_sensors, set_motors


def setup():
    print("Line follower ready")


def loop(dt):
    s = read_line_sensors()

    if s[2]:
        set_motors(60, 60)

    elif s[1]:
        set_motors(30, 60)

    elif s[3]:
        set_motors(60, 30)

    else:
        set_motors(20, 20)
```

---

# Troubleshooting

### pygame not installed

```bash
pip install pygame
```

### simulator does not start

Make sure you run:

```bash
python runner.py
```

inside the project folder.

---

# Future Improvements

Possible upgrades:

- PID controller example
- Sensor visualization
- Multiple tracks
- Robot parameter tuning
- Competition mode

---


