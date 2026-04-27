import importlib
import pygame

from simulator.engine import Engine
import config


# Load user code module
def load_user_code():
    return importlib.import_module("user_code.user_code")


# Ask user to set robot spawn point (optional)
def ask_spawn_point(default_point):
    print("\n=== Robot Spawn Setup ===")
    print("Press Enter to use default start_point:", default_point)

    try:
        sx = input("Enter spawn X (or Enter): ").strip()
        sy = input("Enter spawn Y (or Enter): ").strip()

        # if empty → use default spawn
        if sx == "" or sy == "":
            return default_point

        return (int(sx), int(sy))

    except:
        print("Invalid input — using default start point.")
        return default_point


def main():
    # Create engine
    engine = Engine(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    # Load user script (user_code/user_code.py)
    user = load_user_code()

    # --------------------------------------------------------
    # Ask user where to spawn the robot
    # --------------------------------------------------------
    if hasattr(engine, "world") and hasattr(engine.world, "start_point"):
        chosen_spawn = ask_spawn_point(engine.world.start_point)
    else:
        chosen_spawn = (100, 100)  # fallback

    # --------------------------------------------------------
    # Apply spawn point to the robot
    # --------------------------------------------------------
    if hasattr(engine, "robot"):
        engine.robot.x, engine.robot.y = chosen_spawn

        engine.robot.spawn_x, engine.robot.spawn_y = chosen_spawn
        
    # Run optional user setup()
    if hasattr(user, "setup"):
        user.setup()

    running = True

    # ---------------- MAIN LOOP ----------------
    while running:
        # handle quit or window events
        running = engine.handle_events()

        # engine.update calculates dt internally and returns it
        dt = engine.update()

        # run user loop(dt)
        if hasattr(user, "loop"):
            user.loop(dt)

        # draw everything
        engine.draw()

    pygame.quit()


if __name__ == "__main__":
    main()
