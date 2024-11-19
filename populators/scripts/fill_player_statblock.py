import json
import math
import os

from classes import knight
from generators.scripts import formulae


def fill_ability_scores():
    # Define the ability scores to prompt
    ability_scores = ["Strength (STR)", "Dexterity (DEX)", "Constitution (CON)",
                      "Intelligence (INT)", "Wisdom (WIS)", "Charisma (CHA)"]

    # File path to stats.json
    file_path = "C:\\Users\\innoc\\Documents\\Xplore\\player\\stats.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: stats.json file not found.")
        return

    # Load existing stats
    with open(file_path, 'r') as file:
        stats = json.load(file)

    char_class = stats["Character Information"]["Class"]
    class_modifiers = []
    if char_class == "MKnight" or char_class == "FKnight" or char_class == "Knight":
        class_modifiers = knight.knight_base_modifiers
    # if char_class == "MKnight" or char_class == "FKnight" or char_class == "Knight": Add other class structs
    #     pass
    # if char_class == "MKnight" or char_class == "FKnight" or char_class == "Knight":
    #     pass
    # if char_class == "MKnight" or char_class == "FKnight" or char_class == "Knight":
    #     pass
    # Prompt for each ability score
    for score in ability_scores:
        while True:
            try:
                stats["Ability Scores"][score]["Score"] = 10 + class_modifiers[score] if len(class_modifiers) > 0 else 0
                stats["Ability Scores"][score]["Modifier"] = 0 + class_modifiers[score] if len(class_modifiers) > 0 else 0
                break
            except KeyError:
                print(f"Error: {score} not found in stats.json.")
                break

    # Save updated stats back to the file
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)

    print("Ability scores updated successfully.")

    fill_stat_scores()


def fill_stat_scores():
    print('stats')

    stat_scores = {
        "hp": "Health Points",
        "mana": "Mana",
        "atk": "Damage",
        "acc": "Accuracy",
        "defn": "Defense",
        "phys_ev": "Physical Evasion",
        "mag_ev": "Magical Evasion"
    }

    # File path to stats.json
    file_path = "C:\\Users\\innoc\\Documents\\Xplore\\player\\stats.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: stats.json file not found.")
        return

    # Load existing stats
    with open(file_path, 'r') as file:
        stats = json.load(file)

    level = stats["Character Information"]["Level"] if stats["Character Information"]["Level"] >= 1 else 1
    strength = stats["Ability Scores"]["Strength (STR)"]["Score"]
    dex = stats["Ability Scores"]["Dexterity (DEX)"]["Score"]
    const = stats["Ability Scores"]["Constitution (CON)"]["Score"]
    intel = stats["Ability Scores"]["Intelligence (INT)"]["Score"]
    wis = stats["Ability Scores"]["Wisdom (WIS)"]["Score"]
    cha = stats["Ability Scores"]["Charisma (CHA)"]["Score"]

    stat_values = {
        "hp": formulae.gen_hp(level=level, con=const),
        "mana": formulae.gen_mana(level=level, wis=wis),
        "atk": formulae.gen_atk(base=14, modifier=0, pwr=math.floor((strength // 2))),  # Mod is 0 until items and inventory are done
        "defn": formulae.gen_def(base=0, level=level, con=const, wis=wis),
        "acc": formulae.gen_acc(base=65, modifier=0, dex=dex),
        "phys_ev": formulae.gen_phys_evade(base=5, dex=dex),
        "mag_ev": formulae.gen_mag_evade(base=5, dex=dex, wis=wis)
    }

    for stat, val in stat_values.items():
        stats["Stat Scores"][stat_scores[stat]] = val
    stats["Character Information"]["Level"] = level

    # Save updated stats back to the file
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)

    print("Stat scores updated successfully.")


# Call the method
fill_ability_scores()
