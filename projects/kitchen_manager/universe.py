import pandas as pd


def get_breakfast_items():
    items = ['Waffles', 'Cereal', 'Eggs']
    df = pd.DataFrame({'items': items})
    return df


def get_item_universe():
    # list of possible items
    veggies = pd.DataFrame({'items': ['Lettuce', 'Broccoli', 'Eggs']})
    diary = pd.DataFrame({'items': ['Eggs', 'Milk']})
    juice = pd.DataFrame({'items': ['Apple', 'Orange', 'Mango']})
    breakfast = get_breakfast_items()

    df = pd.concat([veggies, diary, juice, breakfast], ignore_index=False)
    df.drop_duplicates(inplace=True)
    return df
