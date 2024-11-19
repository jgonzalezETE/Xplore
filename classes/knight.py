import random

knight_base_modifiers = {
    "Strength (STR)": 3,
    "Dexterity (DEX)": 1,
    "Constitution (CON)": 2,
    "Intelligence (INT)": -2,
    "Wisdom (WIS)": 0,
    "Charisma (CHA)": 1
}

attribute_increase_ranges = {
    "Strength (STR)": [0, 3],
    "Dexterity (DEX)": [0, 1],
    "Constitution (CON)": [0, 2],
    "Intelligence (INT)": [0, 1],
    "Wisdom (WIS)": [0, 1],
    "Charisma (CHA)": [0, 2],
}


def level_up(player):
    max_atr_up = 3
    atr_indices = []

    while len(atr_indices) != max_atr_up:
        atr_index = random.randint(1, len(attribute_increase_ranges.keys()))
        if atr_index not in atr_indices:
            atr_indices.append(atr_index)


