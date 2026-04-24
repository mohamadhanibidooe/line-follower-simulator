import importlib
import time
import pygame

from simulator.engine import Engine
import config

def load_user_code():
    return importlib.import_module("user_code.user_code")

def main():
    engine = Engine(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    user = load_user_code()

    if hasattr(user, "setup"):
        user.setup()

    last_time = time.time()

    running = True
    while running:
        running = engine.handle_events()

        if hasattr(user, "loop"):
            dt = time.time() - last_time
            last_time = time.time()
            user.loop(dt)

        engine.update()
        engine.draw()
        engine.clock.tick(config.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
