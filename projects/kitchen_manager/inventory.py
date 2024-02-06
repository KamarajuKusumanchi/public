import pandas as pd

from constants import (
    ORANGE_JUICE,
    EGGS,
    WAFFLES,
    CEREAL,
    LETTUCE,
    BROCCOLI,
    FORTUNE_COOKIES,
)


def get_inventory():
    fridge = get_items_in_fridge()
    pantry = get_items_in_pantry()
    inventory = pd.concat([fridge, pantry], ignore_index=True)
    return inventory


def get_items_in_fridge():
    # Todo: hard coding for now. Make it generic later.
    df = pd.DataFrame({"items": [LETTUCE, BROCCOLI, EGGS, ORANGE_JUICE]})
    return df


def get_items_in_pantry():
    shelf_1 = pd.DataFrame({"items": [WAFFLES, CEREAL]})
    snacks = pd.DataFrame({"items": [FORTUNE_COOKIES]})
    pantry = pd.concat([shelf_1, snacks], ignore_index=True)
    return pantry
