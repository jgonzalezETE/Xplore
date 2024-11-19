import json
import math
import os
import sys
import num2words

from generators.scripts import formulae


def fill_ability_scores(name='', tier=0, difficulty=0):
    name = input("Enemy Name: ") if name == '' else name
    tier = int(input("Enemy Tier: ")) if tier == 0 else tier
    difficulty = int(input("Enemy Difficulty: ")) if difficulty == 0 else difficulty

    # Define the ability scores to prompt
    ability_scores = ["Strength (STR)", "Dexterity (DEX)", "Constitution (CON)",
                      "Intelligence (INT)", "Wisdom (WIS)", "Charisma (CHA)"]

    # File path to stats.json
    file_path = "C:\\Users\\innoc\\Documents\\Xplore\\enemies\\" + f"{num2words.num2words(tier)}\\{name}\\stats.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: stats.json file not found.")
        return

    # Load existing stats
    with open(file_path, 'r') as file:
        stats = json.load(file)

    # Prompt for each ability score
    for score in ability_scores:
        while True:
            try:
                value = int(input(f"Enter the value for {score}: "))
                stats["Ability Scores"][score]["Score"] = value
                stats["Ability Scores"][score]["Modifier"] = 0
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            except KeyError:
                print(f"Error: {score} not found in stats.json.")
                break

    # Save updated stats back to the file
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)

    print("Ability scores updated successfully.")

    fill_stat_scores(name, tier, difficulty)


def fill_stat_scores(name, tier, difficulty):
    print('stats')

    stat_scores = {
        "hp": "Health Points",
        "mana": "Mana",
        "exp": "Experience",
        "atk": "Damage",
        "acc": "Accuracy",
        "defn": "Defense",
        "phys_ev": "Physical Evasion",
        "mag_ev": "Magical Evasion"
    }

    # File path to stats.json
    file_path = "C:\\Users\\innoc\\Documents\\Xplore\\enemies\\" + f"{num2words.num2words(tier)}\\{name}\\stats.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: stats.json file not found.")
        return

    # Load existing stats
    with open(file_path, 'r') as file:
        stats = json.load(file)

    strength = stats["Ability Scores"]["Strength (STR)"]["Score"]
    dex = stats["Ability Scores"]["Dexterity (DEX)"]["Score"]
    const = stats["Ability Scores"]["Constitution (CON)"]["Score"]
    intel = stats["Ability Scores"]["Intelligence (INT)"]["Score"]
    wis = stats["Ability Scores"]["Wisdom (WIS)"]["Score"]
    cha = stats["Ability Scores"]["Charisma (CHA)"]["Score"]

    stat_values = {
        "hp": formulae.gen_hp(rank=tier, con=const, diff=difficulty),
        "mana": formulae.gen_mana(rank=tier, wis=wis, diff=difficulty),
        "exp": formulae.gen_exp(rank=tier, diff=difficulty),
        "atk": formulae.gen_atk(base=5, modifier=0, pwr=math.floor((strength // 2) * (1 + ((20 * difficulty) / 100)))),
        "defn": formulae.gen_def(rank=tier, con=const, wis=wis),
        "acc": formulae.gen_acc(dex=dex),
        "phys_ev": formulae.gen_phys_evade(dex=dex),
        "mag_ev": formulae.gen_mag_evade(dex=dex, wis=wis)
    }

    for stat, val in stat_values.items():
        stats["Stat Scores"][stat_scores[stat]] = val
    stats["Stat Scores"]["Difficulty"] = difficulty

    # Save updated stats back to the file
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)

    print("Stat scores updated successfully.")

fill_ability_scores()