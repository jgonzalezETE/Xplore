import json

from populators.scripts import fill_player_statblock


class Player:
    def __init__(self, name, stats_file):
        self.name = name
        self.char_class = None
        self.stats_path = stats_file
        self.stats = None
        self.max_health = None
        self.health = None
        self.mana = None
        self.experience = None
        self.damage = None
        self.defense = None
        self.accuracy = None
        self.phys_evade = None
        self.mag_evade = None
        self.ability_scores = None
        self.spells = None
        self.is_defending = False

    def init_player(self):
        self.stats = self.load_stats(self.stats_path)
        self.max_health = int(self.stats['Stat Scores']['Health Points'])
        self.health = int(self.stats['Stat Scores']['Health Points'])
        self.mana = int(self.stats['Stat Scores']['Mana'])
        self.experience = int(self.stats['Stat Scores']['Experience'])
        self.damage = int(self.stats['Stat Scores']['Damage'])
        self.defense = int(self.stats['Stat Scores']['Defense'])
        self.accuracy = int(self.stats['Stat Scores']['Accuracy'])
        self.phys_evade = int(self.stats['Stat Scores']['Physical Evasion'])
        self.mag_evade = int(self.stats['Stat Scores']['Magical Evasion'])
        self.ability_scores = self.stats['Ability Scores']
        self.spells = self.stats['Spells']
        self.is_defending = False

    def load_stats(self, stats_file):
        with open(stats_file, 'r') as file:
            return json.load(file)

    def assign_class(self, name):
        self.char_class = name
        fill_player_statblock.fill_ability_scores()
        self.init_player()

    def take_damage(self, amount):
        self.health -= amount
        print(f"You take {amount} damage! Your health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been slain! Game Over")

    def attack(self):
        return self.damage

    def defend(self):
        self.is_defending = True

    def get_sounds(self):
        pass

    def __repr__(self):
        return f"Player({self.name}, HP: {self.health}, Damage: {self.damage})"
