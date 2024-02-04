#! /usr/bin/env python3

import pandas as pd

def get_items_in_fridge():
    # Todo: hard coding for now. Make it generic later.
    df = pd.DataFrame({'items': ['Lettuce', 'Broccoli', 'Eggs']})
    return df

def get_items_in_pantry():
    df = pd.DataFrame({'items': ['Waffles', 'Cereal']})
    return df

def get_inventory():
    fridge = get_items_in_fridge()
    pantry = get_items_in_pantry()
    inventory = pd.concat([fridge, pantry], ignore_index=True)
    return inventory

def get_item_universe():
    # list of possible items
    veggies = ['Lettuce', 'Broccoli', 'Eggs']
    diary = ['Eggs', 'Milk']
    breakfast_items = ['Waffles', 'Cereal']

    df = pd.DataFrame({
        'items': veggies + diary + breakfast_items})
    df.drop_duplicates(inplace=True)
    return df

def what_to_eat():
    fridge = get_items_in_fridge()
    to_eat = fridge['items'].sample()
    return to_eat

def main():
    to_eat = what_to_eat()
    print(to_eat)

if __name__ == '__main__':
    main()
