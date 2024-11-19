import math


def calc_exp(player, enemy):
    curr_level = player.Level
    enemy_rank = enemy.Rank
    curr_exp = enemy.Experience

    if curr_level > enemy_rank:
        curr_exp = math.floor(curr_exp * 0.75)
    elif curr_level > enemy_rank + 1:
        curr_exp = math.floor(curr_exp * 0.50)
    elif curr_level > enemy_rank + 2:
        curr_exp = math.floor(curr_exp * 0.25)

    return curr_exp
