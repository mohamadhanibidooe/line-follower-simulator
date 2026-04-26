# Line Follower Robot Simulator

A simple Python + Pygame simulator for testing line follower robot algorithms.

This project allows you to write your own robot control logic and test it on a virtual track using line sensors and differential motors. The goal of the project is to make it easy to experiment with line‑following algorithms without needing a physical robot.

## Requirements
- Python 3.9+
- pygame

```bash
pip install pygame
```

## Running the Simulator
```bash
python runner.py
```

When the simulator starts, you will be prompted to enter the robot's spawn position (X and Y).

## Project Structure
```
line follower simulator/
├── runner.py
├── user_code.py
├── track.png
└── simulator/
    ├── engine.py
    ├── robot.py
    ├── world.py
    └── api_stub.py
```

## user_code.py
### setup()
```python
def setup():
    print("Robot algorithm started.")
```

### loop(dt)
```python
def loop(dt):
    sensors = read_line_sensors()
    if sensors[2]:
        set_motors(50, 50)
    else:
        set_motors(0, 0)
```

## API Functions
```python
from simulator.api_stub import read_line_sensors, set_motors
```

### read_line_sensors()
```python
sensors = read_line_sensors()
```

### set_motors(left, right)
```python
set_motors(50, 50)
```
