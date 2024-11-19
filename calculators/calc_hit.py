import math
import random


def calc_hit(dealer, receiver, is_magic=False):
    attack_roll = random.randint(1, 100)

    if is_magic:
        hit_chance = math.floor(100 - (100 - (receiver.mag_evade/100)))
    else:
        hit_chance = math.floor(dealer.accuracy - (dealer.accuracy * (receiver.phys_evade/100)))

    if hit_chance < 10:
        hit_chance = 10
    return True if hit_chance > 100 else attack_roll <= hit_chance
