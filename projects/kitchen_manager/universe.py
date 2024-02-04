import pandas as pd

from constants import (
    APPLE_JUICE,
    MANGO_JUICE,
    ORANGE_JUICE,
    EGGS,
    WAFFLES,
    CEREAL,
    LETTUCE,
    BROCCOLI,
    MILK,
)


def get_breakfast_items():
    items = [WAFFLES, CEREAL, EGGS, ORANGE_JUICE]
    df = pd.DataFrame({"items": items})
    return df


def get_item_universe():
    # list of possible items
    veggies = pd.DataFrame({"items": [LETTUCE, BROCCOLI]})
    diary = pd.DataFrame({"items": [EGGS, MILK]})
    juice = pd.DataFrame({"items": [APPLE_JUICE, MANGO_JUICE, ORANGE_JUICE]})
    breakfast = get_breakfast_items()

    df = pd.concat([veggies, diary, juice, breakfast], ignore_index=False)
    df.drop_duplicates(inplace=True)
    return df
