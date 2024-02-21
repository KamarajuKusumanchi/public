from constants import (
    EGGS,
    EGG_SCRAMBLE,
    EGG_CURRY,
    ONIONS,
    OATS_DOSA,
    OATS,
    EGG_NOODLES,
    MAGGI,
    BREAK_FAST,
    LUNCH,
    DINNER,
    ORANGE_JUICE,
    BOILED_EGGS,
    APPLE,
)


def get_dish_map():
    # dish_map a dictionary that maps string to an array of strings.
    dish_map = {}
    dish_map[EGG_SCRAMBLE] = [EGGS]
    dish_map[EGG_CURRY] = [EGGS, ONIONS]
    dish_map[OATS_DOSA] = [OATS, ONIONS]
    dish_map[EGG_NOODLES] = [EGGS, MAGGI]
    return dish_map


def convert_to_item_map(dish_map):
    # Convert dish_map to item_map.
    # Both dish_map and item_map are dictionaries that map string to an
    # array of strings.
    #
    # For example, given
    # dish_map = {
    #     'egg scramble': ['Eggs'],
    #     'egg curry': ['Eggs', 'onions'],
    #     'oats dosa': ['oats', 'onions']}
    # this function will return
    # item_map = {
    #     'Eggs': ['egg scramble', 'egg curry'],
    #     'onions': ['egg curry', 'oats dosa'],
    #     'oats': ['oats dosa']}
    item_map = {}
    for k, vec in dish_map.items():
        for elem in vec:
            if elem in item_map:
                item_map[elem].append(k)
            else:
                item_map[elem] = [k]
    return item_map


def get_item_map():
    # Get item_map from dish_map
    # Both dish_map and item_map are dictionaries that map string to an
    # array of strings.
    dish_map = get_dish_map()
    item_map = convert_to_item_map(dish_map)
    return item_map


def get_dish_to_meal_map():
    dish_to_meal = {}
    dish_to_meal[OATS_DOSA] = [BREAK_FAST, DINNER]
    dish_to_meal[EGG_CURRY] = [LUNCH, DINNER]
    dish_to_meal[ORANGE_JUICE] = [BREAK_FAST]
    dish_to_meal[BOILED_EGGS] = [BREAK_FAST]
    dish_to_meal[APPLE] = [BREAK_FAST]


if __name__ == "__main__":
    dish = get_dish_map()
    print(dish)
    item = get_item_map()
    print(item)
