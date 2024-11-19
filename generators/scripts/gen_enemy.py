import os
from generators.scripts import gen_statblock as stats


def create_enemy_structure():
    # Prompt for the name and tier
    name = input("Enter the enemy name: ").strip()
    tier = input("Enter the tier: ").strip()
    difficulty = input("Enter enemy difficulty: ").strip()
    current = os.getcwd()

    # Define the base directory
    base_dir = os.path.join(os.path.dirname(current), "enemies")

    # Create 'enemies' directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create tier directory inside 'enemies'
    tier_dir = os.path.join(base_dir, tier)
    if not os.path.exists(tier_dir):
        os.makedirs(tier_dir)

    # Create the enemy directory inside the tier directory
    enemy_dir = os.path.join(tier_dir, name)
    os.makedirs(enemy_dir, exist_ok=True)

    # Create 'art' and 'sounds' sub-directories
    os.makedirs(os.path.join(enemy_dir, "art"), exist_ok=True)
    os.makedirs(os.path.join(enemy_dir, "sounds"), exist_ok=True)

    # Create 'scripts.py' file
    with open(os.path.join(enemy_dir, "scripts.py"), "w") as script_file:
        script_file.write("# Scripts for enemy: {}\n".format(name))

    # Create 'stats.json' file
    with open(os.path.join(enemy_dir, "stats.json"), "w") as stats_file:
        stats_file.write("Enemy Name: {}\nTier: {}\n".format(name, tier))

    print(f"Directory structure for '{name}({difficulty})' in tier '{tier}' created successfully.")
    return name


# Run the function
enemy_name = create_enemy_structure()
stats.write_stat_block(name=enemy_name)

if __name__ == '__main__':
    pass
