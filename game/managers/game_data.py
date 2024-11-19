import player

classes = {
    "MKnight": "Knight",
    "FKnight": "Knight",
    "MWizard": "Knight",
    "FWizard": "Knight",
    "MRogue": "Knight",
    "FRogue": "Knight",
    "MCleric": "Knight",
    "FCleric": "Knight"
}


class GameDataManager:
    def __init__(self, new=True):
        # TODO introduce save/load struct
        # if new:
        #     self.player = Player(name="Hero", char_class="Knight", stats_file="C:\\Users\\innoc\\Documents\\Xplore\\player\\stats.json")
        self.player = player.Player(name="Jake", stats_file="C:\\Users\\innoc\\Documents\\Xplore\\player\\stats.json")
        self.current_level = 1
        self.settings = {"volume": 0.5, "difficulty": "normal"}


    def assign_player_class(self, class_name):
        self.player.assign_class(classes[class_name])
