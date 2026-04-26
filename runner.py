import importlib
import time
import pygame

from simulator.engine import Engine
import config


def load_user_code():
    return importlib.import_module("user_code.user_code")


def ask_spawn_point(default_point):
    print("\n=== Robot Spawn Setup ===")
    print("Press Enter to use default start_point:", default_point)

    try:
        sx = input("Enter spawn X (or Enter): ").strip()
        sy = input("Enter spawn Y (or Enter): ").strip()

        if sx == "" or sy == "":
            return default_point

        return (int(sx), int(sy))
    except:
        print("Invalid input — using default start point.")
        return default_point


def main():
    engine = Engine(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    user = load_user_code()

    # --------------------------------------------------------
    # Ask user where to spawn the robot
    # --------------------------------------------------------
    if hasattr(engine, "world") and hasattr(engine.world, "start_point"):
        chosen_spawn = ask_spawn_point(engine.world.start_point)
    else:
        chosen_spawn = (100, 100)  # fallback

    # --------------------------------------------------------
    # Apply spawn point to robot
    # --------------------------------------------------------
    if hasattr(engine, "robot"):
        engine.robot.x, engine.robot.y = chosen_spawn

    # Now call user setup
    if hasattr(user, "setup"):
        user.setup()

    last_time = time.time()
    running = True

    while running:
        running = engine.handle_events()

        dt = time.time() - last_time
        last_time = time.time()

        engine.update()

        if hasattr(user, "loop"):
            user.loop(dt)

        engine.draw()
        engine.clock.tick(config.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
