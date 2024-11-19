import pygame
import sys

from managers.game_state import GameStateManager
from managers.game_data import GameDataManager
from modes.combat import handle_combat
from modes.class_selection import handle_class_selection
from modes.main_menu import handle_main_menu

# Initialize Pygame
pygame.init()

manager = GameStateManager()
data_manager = GameDataManager()

# Set up the game window
WIDTH, HEIGHT = 1200, 800  # Window dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window
manager.set_screen(screen)
pygame.display.set_caption("Xplore")  # Set the window title
clock = pygame.time.Clock()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit the game when the close button is clicked
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (e.g., white)
        screen.fill((255, 255, 255))  # RGB color

        if manager.get_state() == "menu":
            # print('in main menu')
            handle_main_menu(manager)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print("S key pressed, starting game")
                    manager.stop_music()
                    manager.set_state("class")
                elif event.key == pygame.K_q:
                    print("Q key pressed, quitting game")
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    print("escape pressed, quitting game")
                    pygame.quit()
                    sys.exit()

        elif manager.get_state() == "class":
            # print('in class selection')
            screen.fill((255, 255, 255))
            images = handle_class_selection(manager)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("escape pressed, quitting game")
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for name, image in images.items():
                    if image.image_rect.collidepoint(event.pos):
                        print(f"Clicked {name}")
                        data_manager.assign_player_class(name)
                        manager.set_state("combat")

        elif manager.get_state() == "creation":  # Skipping for now
            print('in character creation')

        elif manager.get_state() == "combat":
            print('in combat')
            handle_combat(manager, data_manager)
            # if manager.is_player_turn:
            #     wait = True
            #     while wait:
            #         for event in pygame.event.get():
            #             if event.type == pygame.KEYDOWN:
            #                 if event.key == pygame.K_a:
            #                     manager.take_action("a")
            #                     wait = False
            #                 elif event.key == pygame.K_d:
            #                     manager.take_action("d")
            #                     wait = False

        elif manager.get_state() == "stats":
            print('in stat screen')

        elif manager.get_state() == "victory":
            print('in victory screen')

        elif manager.get_state() == "epilogue":
            print('in epilogue')

    # Update the display
    pygame.display.flip()

    clock.tick(60)
