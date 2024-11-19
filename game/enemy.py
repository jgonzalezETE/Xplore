import json


class Enemy:
    def __init__(self, name, stats_file):
        self.name = name
        self.stats = self.load_stats(stats_file)
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
        self.path = f"C:\\Users\\innoc\\Documents\\Xplore\\enemies\\one\\{name}\\"
        self.image = self.path + f"art\\{name}.png"
        # self.script = __import__(self.path + "scripts.py")
        self.is_defending = False

    def load_stats(self, stats_file):
        with open(stats_file, 'r') as file:
            return json.load(file)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack(self):
        return self.damage

    def defend(self):
        self.is_defending = True

    def __repr__(self):
        return f"Enemy({self.name}, HP: {self.health}, Damage: {self.damage})"
