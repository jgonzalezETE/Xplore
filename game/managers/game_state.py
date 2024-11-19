import pygame
import enemy


class GameStateManager:
    splash_path = "C:\\Users\\innoc\\Documents\\Xplore\\assets\\gui\\Title.png"

    def __init__(self):
        self.state = "menu"  # Initial state
        self.screen = None
        self.is_player_turn = False
        self.action = None
        self.sounds = {}
        self.mixer_active = False

    def set_screen(self, screen):
        self.screen = screen
        print(f"Screen set to {self.screen}")

    def set_state(self, new_state):
        self.state = new_state
        print(f"Game state changed to: {self.state}")

    def get_state(self):
        return self.state

    def notify_turn(self):
        self.is_player_turn = not self.is_player_turn

    def take_action(self, action):
        self.action = action

    def load_menu(self):
        menu = pygame.transform.smoothscale(pygame.image.load(self.splash_path), (1200, 800))
        menu_center = menu.get_rect().center = (0, 0)
        self.screen.fill((255, 255, 255))
        self.screen.blit(menu, menu_center)


    def load_enemy(self, name, tier, difficulty):
        #  only loading gobbo atm
        enemy_path = f"C:\\Users\\innoc\\Documents\\Xplore\\enemies\\{tier}\\{name}\\"
        return enemy.Enemy(name, enemy_path + "stats.json")


    def stop_music(self):
        pygame.mixer.music.stop()
        self.mixer_active = False

    def start_title_music(self):
        if not self.mixer_active:
            pygame.mixer.music.load("C:\\Users\\innoc\\Documents\\Xplore\\assets\\music\\Title.mp3")
            pygame.mixer.music.play(-1)
            self.mixer_active = True

    def start_class_selection_music(self):
        if not self.mixer_active:
            pygame.mixer.music.load("C:\\Users\\innoc\\Documents\\Xplore\\assets\\music\\Goofy Class.mp3")
            pygame.mixer.music.play(-1)
            self.mixer_active = True

    def start_combat_music(self):
        if not self.mixer_active:
            pygame.mixer.music.load("C:\\Users\\innoc\\Documents\\Xplore\\assets\\music\\Fighting.mp3")
            pygame.mixer.music.play(-1)
            self.mixer_active = True

    def start_victory_music(self):
        if not self.mixer_active:
            pygame.mixer.music.load("C:\\Users\\innoc\\Documents\\Xplore\\assets\\music\\Victory.mp3")
            pygame.mixer.music.play(1)
            self.mixer_active = True

    def start_final_boss_music(self):
        if not self.mixer_active:
            pygame.mixer.music.load("C:\\Users\\innoc\\Documents\\Xplore\\assets\\music\\Gregorius.mp3")
            pygame.mixer.music.play(-1)
            self.mixer_active = True

    def play_sound(self, sound):
        if sound not in self.sounds:
            self.sounds[sound] = pygame.mixer.Sound(sound)
        self.sounds[sound].play()
