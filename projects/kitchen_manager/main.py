#! /usr/bin/env python3

import pandas as pd

from inventory import get_inventory
from universe import get_breakfast_items, what_to_cook_for_dinner


def what_to_eat():
    inventory = get_inventory()
    to_eat = inventory["items"].sample()
    return to_eat


def what_to_eat_for_breakfast():
    inventory = get_inventory()
    univ = get_breakfast_items()
    available = pd.merge(inventory, univ, on=["items"], how="inner")
    to_eat = available["items"].sample()
    return to_eat


def main():
    # to_eat = what_to_eat()
    eat_for_breakfast = what_to_eat_for_breakfast()
    cook_for_dinner = what_to_cook_for_dinner()
    print("breakfast:")
    print(eat_for_breakfast)
    print("dinner:")
    print(cook_for_dinner)


if __name__ == "__main__":
    main()
