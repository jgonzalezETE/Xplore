import math
import os


def gen_hp(base=20, level=0, rank=0, con=0, diff=0):
    return math.floor((base + (5 * level) + (10 * rank) + con) * (1 + (15 * diff) / 100))


def gen_mana(base=5, level=0, rank=0, wis=0, diff=0):
    return math.floor((base + (3 * level) + (10 * rank) + wis) * (1 + (5 * diff) / 100))


def gen_exp(base=5, rank=0, diff=0):
    return base + (10 * rank) + (5 * diff)


def gen_atk(base=0, modifier=0, pwr=0):
    return base + modifier + pwr


def gen_def(base=0, modifier=0, level=0, rank=0, con=0, wis=0):
    return base + modifier + (1 * (level // 2)) + (4 * rank) + con + (wis // 3)


def gen_acc(base=60, modifier=0, dex=0):  # Modifier should cap at 20
    return base + modifier + (3 * (dex // 3))


def gen_phys_evade(base=0, dex=0):
    return base + (5 * (dex // 5))


def gen_mag_evade(base=0, dex=0, wis=0):
    return base + (5 * (dex // 8)) + (10 * wis // 10)
