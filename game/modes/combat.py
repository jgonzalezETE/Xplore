import math
import random
import sys
import time

import pygame
from calculators import calc_dmg, calc_exp

current_round = 0


def handle_combat(manager, data_manager):
    was_defeat = start_combat(manager, data_manager)
    # print(was_defeat)
    if not was_defeat:
        print('in victory')
        manager.stop_music()
        manager.start_victory_music()

        time.sleep(5)

        manager.set_state("class")
        # manager.award_experience(enemy.experience)
        # manager.state = "victory"
    else:
        pass
        # manager.state = "defeat"

    pass


def start_combat(manager, data_manager):
    manager.stop_music()
    manager.start_combat_music()
    enemy = manager.load_enemy("Gobbo", "one", 1)
    player = data_manager.player
    manager.screen.fill((0, 0, 0))
    enemy_splash = pygame.transform.smoothscale(pygame.image.load(enemy.image), (1200, 800))
    manager.screen.blit(enemy_splash, enemy_splash.get_rect())
    pygame.display.flip()

    load_ui_elements(manager)

    end_combat = False
    while not end_combat:
        end_combat = combat_round(manager, player, enemy)

    result = finish_combat(manager, player, enemy)
    return result


def combat_round(manager, player, enemy):
    end_combat = False

    incr_round()
    end_combat = examine_combat(manager, player, enemy, True)
    if not end_combat:
        player_turn(manager, player, enemy)
        end_combat = examine_combat(manager, player, enemy, False)
    if not end_combat:
        enemy_turn(manager, player, enemy)
        end_combat = examine_combat(manager, player, enemy, False)

    return end_combat


def examine_combat(manager, player, enemy, display_status):
    health_states = {
        75: "Healthy",
        50: "Injured",
        25: "Waning",
        10: "Critical",
        0: "Dead"
    }
    end_combat = False
    global current_round
    player_status = "Unknown"
    enemy_status = "Unknown"

    if player.health <= 0 or enemy.health <= 0:
        end_combat = True

    for val, state in health_states.items():
        if (math.floor((player.health / player.max_health) * 100)) >= val:
            player_status = state
            break

    for val, state in health_states.items():
        if (math.floor((enemy.health / enemy.max_health) * 100)) >= val:
            enemy_status = state
            break

    if display_status:
        print(f"It is currently round {current_round} of this encounter.")
        print(f"You have {player.health} left, your status is {player_status}")
        print(f"{enemy.name} has {enemy.health} left, their status is {enemy_status}")

    print(end_combat)
    return end_combat


def incr_round():
    global current_round
    current_round += 1


def player_turn(manager, player, enemy):
    player.is_defending = False
    # manager.notify_turn()
    action = ""
    was_hit = False
    damage = 0

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_a:
                    action = "a"
                    wait = False

                elif event.key == pygame.K_d:
                    action = "d"
                    wait = False

    if action == "a":
        # TODO add attack animations
        # play_attack_animation(data_manager)
        # manager.play_sound(player.get_attack_sound())
        print(calc_dmg.deal_phys_damage(player, enemy, enemy.is_defending))
        was_hit, damage = calc_dmg.deal_phys_damage(player, enemy, enemy.is_defending)
        print(f"You attacked {enemy.name}... the attack was a {was_hit}! You deal {damage} damage.")
        if was_hit and damage > 0:
            enemy.take_damage(damage)

    elif action == "d":
        # play_defend_animation(data_manager)
        player.defend()
        print(f"You brace yourself for an attack")


def enemy_turn(manager, player, enemy):
    # TODO - Not for a while lol - invent/introduce enemy intelligence
    enemy.is_defending = False
    manager.notify_turn()

    action_weight = {
        "attack": 6,
        "defend": 9,
        "pass": 10
    }

    action_val = random.randint(1, 10)

    if action_val <= action_weight["attack"]:
        was_hit, damage = calc_dmg.deal_phys_damage(enemy, player, player.is_defending)
        print(f"{enemy.name} attacks you... the attack was a {was_hit}! You take {damage} damage.")

        if was_hit and damage > 0:
            player.take_damage(damage)

    elif action_val <= action_weight["defend"]:
        enemy.defend()
        print(f"{enemy.name} braces themself for an attack")

    else:  # randint must be 10 to hit this
        print(f"{enemy.name} appears distracted and takes no action")


def finish_combat(manager, player, enemy):
    print('finishing combat')
    return player.health <= 0


def load_ui_elements(manager):
    pass
