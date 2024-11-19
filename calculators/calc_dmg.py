import math
import os
import player
from calculators import calc_hit as attack


def deal_phys_damage(dealer, receiver, is_defending):
    was_hit = attack.calc_hit(dealer, receiver, False)

    if was_hit:
        receiver_defence = receiver.defense
        if is_defending:
            receiver_defence = math.floor(receiver_defence * 1.5)

        return "hit", 0 if receiver_defence > dealer.damage else dealer.damage - receiver_defence
    else:
        return "miss", 0


def deal_mag_damage(dealer, spell, receiver, is_defending):
    # TODO retrieve spell from db and calc dmg based on dealer int
    was_hit = attack.calc_hit(dealer, receiver, True)

    if was_hit:
        # TODO establish spell table and system
        temp_spell = 'Fireball'
        potency = 8
        dealer_dmg = 8 + (dealer.Intelligence//2)
        receiver_def = (math.floor(receiver.defense * 0.75))
        if is_defending:
            receiver_def = math.floor(math.floor(receiver_def * 1.5) * 0.75)

        return "hit", 0 if receiver_def > dealer_dmg else "hit", dealer_dmg - receiver_def
    else:
        return "miss", 0

