import pandas as pd


def get_inventory():
    fridge = get_items_in_fridge()
    pantry = get_items_in_pantry()
    inventory = pd.concat([fridge, pantry], ignore_index=True)
    return inventory


def get_items_in_fridge():
    # Todo: hard coding for now. Make it generic later.
    df = pd.DataFrame({'items': ['Lettuce', 'Broccoli', 'Eggs']})
    return df


def get_items_in_pantry():
    df = pd.DataFrame({'items': ['Waffles', 'Cereal']})
    return df
