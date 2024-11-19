from collections import namedtuple

import pygame

image_points = {
    "top_left_a": (175, 200),
    "top_left_b": (450, 200),
    "top_right_a": (750, 200),
    "top_right_b": (1025, 200),
    "bottom_left_a": (175, 600),
    "bottom_left_b": (450, 600),
    "bottom_right_a": (750, 600),
    "bottom_right_b": (1025, 600)
}

name_points = {
    "Knight": [237, 25, 125, 50, "Knight", (234, 177, 93), "black"],
    "Wizard": [828, 25, 125, 50, "Wizard", (234, 177, 93), "black"],
    "Rogue": [237, 725, 125, 50, "Rogue", (234, 177, 93), "black"],
    "Cleric": [828, 725, 125, 50, "Cleric", (234, 177, 93), "black"],
}

class_icons = {
    "MKnight":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\M Knight.png",
    "FKnight":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\F Knight.png",
    "MWizard":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\M Wizard.png",
    "FWizard":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\F Wizard.png",
    "MRogue":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\M Rogue.png",
    "FRogue":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\F Rogue.png",
    "MCleric":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\M Cleric.png",
    "FCleric":"C:\\Users\innoc\Documents\Xplore\Assets\Player art\Characters\F Cleric.png"
}


def handle_class_selection(manager):
    manager.load_menu()
    manager.start_class_selection_music()

    i = 0
    images = {}
    point_list = list(image_points.values())
    ImageData = namedtuple("char_class", ["image", "image_rect"])

    for name, icon in class_icons.items():
        # Load an image
        image = pygame.transform.smoothscale(pygame.image.load(icon), (250, 300))
        image_rect = image.get_rect()

        # Center the image in the top-left quadrant
        image_rect.center = point_list[i]
        i += 1

        images[name] = ImageData(image, image_rect)
        # images[image]['name'] = name

        # Display the image
    for name, data in images.items():
        manager.screen.blit(data.image, data.image_rect)

    for pt in name_points.values():
        class_text, class_banner = draw_class_name(manager.screen, pt[0], pt[1], pt[2], pt[3], pt[4], pt[5], pt[6])
        manager.screen.blit(class_text, class_banner)

    text, banner = draw_class_name(manager.screen, 450, 363, 300, 75, "Choose your class", (234, 177, 93), "black")
    manager.screen.blit(text, banner)
    return images


def draw_class_name(screen, x, y, width, height, text, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))

    menu_font = pygame.font.Font("C:\\Users\innoc\Documents\Xplore\Assets\Fonts\serpentine.ttf", 30)
    text_surface = menu_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    return text_surface, text_rect

