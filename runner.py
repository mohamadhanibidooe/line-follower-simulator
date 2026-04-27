import importlib
import pygame
import math

from simulator.engine import Engine
import config


def load_user_code():
    # Dynamically import user code
    return importlib.import_module("user_code.user_code")


def main():
    # Create engine
    engine = Engine(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    # Load user loop
    user = load_user_code()

    # Default spawn from track (if exists)
    if hasattr(engine, "world") and hasattr(engine.world, "start_point"):
        chosen_spawn = engine.world.start_point
    else:
        chosen_spawn = (100, 100)

    chosen_angle_deg = 0.0

    # -----------------------------------------------------
    # Phase 1: Choose spawn position by clicking
    # -----------------------------------------------------
    spawn_point_selected = False
    angle_confirmed = False
    selected_spawn = None
    selected_angle_deg = 0.0

    while not spawn_point_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Mouse left-click selects spawn point
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected_spawn = event.pos

            # Enter confirms spawn point
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if selected_spawn is not None:
                    spawn_point_selected = True
                else:
                    print("Please click somewhere to select spawn point.")

        # Draw only the spawn point, not angle
        engine.draw_spawn_selection(selected_spawn, None)

    # If user quit early
    if not spawn_point_selected:
        pygame.quit()
        return

    # -----------------------------------------------------
    # Phase 2: Choose rotation angle
    # -----------------------------------------------------
    selected_angle_deg = 0.0

    while not angle_confirmed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                # Rotate left/right
                if event.key == pygame.K_LEFT:
                    selected_angle_deg -= 5.0
                elif event.key == pygame.K_RIGHT:
                    selected_angle_deg += 5.0

                # Fine adjustments
                elif event.key == pygame.K_q:
                    selected_angle_deg -= 1.0
                elif event.key == pygame.K_e:
                    selected_angle_deg += 1.0

                # Confirm angle
                elif event.key == pygame.K_RETURN:
                    angle_confirmed = True

        # Keep degree in range [0-360)
        selected_angle_deg %= 360.0

        # Draw spawn + angle arrow
        engine.draw_spawn_selection(selected_spawn, selected_angle_deg)

    chosen_spawn = selected_spawn
    chosen_angle_deg = selected_angle_deg

    # Store chosen spawn inside engine so RESET can use it
    engine.spawn_point = chosen_spawn
    engine.spawn_angle = chosen_angle_deg

    # -----------------------------------------------------
    # Apply selected spawn & angle to robot
    # -----------------------------------------------------
    if hasattr(engine, "robot"):
        engine.robot.x, engine.robot.y = chosen_spawn
        engine.robot.spawn_x, engine.robot.spawn_y = chosen_spawn

        # Robot uses radians internally → convert here
        engine.robot.angle = math.radians(chosen_angle_deg)

        # Set finish line marker
        engine.set_finish_line(chosen_spawn)

    running = True

    # -----------------------------------------------------
    # Main simulation loop
    # -----------------------------------------------------
    while running:
        running = engine.handle_events()
        dt = engine.update()

        if hasattr(user, "loop"):
            user.loop(dt)

        engine.draw()

if __name__ == "__main__":
    main()