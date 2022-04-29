import random
barrels_list = []
for digits_count in range(1, 92, 1):
    barrels_list.append(digits_count)


def barrel_generation():
    barrel = random.choice(barrels_list)
    barrels_list.remove(barrel)
    return barrel


