import pygame

menu_options = [
    "start",
    "quit"
]


def handle_main_menu(manager):
    manager.load_menu()
    manager.start_title_music()

    opt_first = [475, 400, 300, 125, "START", (64, 64, 64), "white"]
    opt_second = [475, 550, 300, 125, "QUIT", (64, 64, 64), "white"]
    options = [opt_first, opt_second]

    for option in range(len(menu_options)):
        opt = options[option]
        text, banner = draw_menu_option(manager.screen, opt[0], opt[1], opt[2], opt[3], opt[4], opt[5], opt[6])
        manager.screen.blit(text, banner)


def draw_menu_option(screen, x, y, width, height, text, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))

    menu_font = pygame.font.Font("C:\\Users\\innoc\\Documents\\Xplore\\assets\\fonts\\serpentine.ttf", 100)
    text_surface = menu_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    return text_surface, text_rect
