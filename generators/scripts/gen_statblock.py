import json
import os
import sys


def write_stat_block(name=None):
    if not name:
        # If no name is provided as a parameter, prompt for it
        name = input("Enter the character name: ").strip()

    base_dirs = ["enemies", "npc"]
    tier_dirs = ["one", "two", "three", "four", "five", "six"]
    stat_block = {
        "Character Information": {
            "Name": name,
            "Class": "[Enter Class]",
            "Background": "[Enter Background]",
            "Level": "[Enter Level]"
        },
        "Stat Scores": {
            "Health Points": "[Enter HP]",
            "Mana": "[Enter Mana]",
            "Experience": "[Enter XP]",
            "Damage": "[Enter Damage]",
            "Accuracy": "[Enter Damage]",
            "Defense": "[Enter Damage]",
            "Physical Evasion": "[Enter Damage]",
            "Magical Evasion": "[Enter Damage]",
            "Difficulty": "[Enter Damage]"
        },
        "Ability Scores": {
            "Strength (STR)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"},
            "Dexterity (DEX)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"},
            "Constitution (CON)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"},
            "Intelligence (INT)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"},
            "Wisdom (WIS)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"},
            "Charisma (CHA)": {"Score": "[Enter Score]", "Modifier": "[Enter Modifier]"}
        },
        "Spells": []
    }

    # Search for the directory
    for base_dir in base_dirs:
        target_dir = f"{os.path.dirname(os.getcwd())}\\{base_dir}"
        print(target_dir)
        if os.path.exists(target_dir):
            for tier_dir in tier_dirs:
                dest = os.path.join(target_dir, f"{tier_dir}\\{name}")
                print(dest)
                if os.path.exists(dest):
                    stats_file = os.path.join(dest, "stats.json")

                    # Write the stat block to stats.txt
                    with open(stats_file, "w") as file:
                        json.dump(stat_block, file, indent=4)

                    print(f"Stat block written to {stats_file}")
                    return
        else:
            print(f"Directory for '{name}' not found in either 'enemies' or 'npc' directories.")


# Entry point for command-line use
if __name__ == "__main__":
    pass
    # Check if a name was provided as a command-line argument
    # name_arg = sys.argv[1] if len(sys.argv) > 1 else None
    # write_stat_block(name_arg)
