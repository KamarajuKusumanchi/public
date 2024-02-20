from dishes import convert_to_item_map
from constants import EGGS, EGG_SCRAMBLE, EGG_CURRY, ONIONS, OATS_DOSA, OATS


def test_convert_to_item_map():
    dish_map = {}
    dish_map[EGG_SCRAMBLE] = [EGGS]
    dish_map[EGG_CURRY] = [EGGS, ONIONS]
    dish_map[OATS_DOSA] = [OATS, ONIONS]

    item_map_got = convert_to_item_map(dish_map)

    item_map_expected = {}
    item_map_expected[EGGS] = [EGG_SCRAMBLE, EGG_CURRY]
    item_map_expected[ONIONS] = [EGG_CURRY, OATS_DOSA]
    item_map_expected[OATS] = [OATS_DOSA]
    assert (
        item_map_got == item_map_expected
    ), "Logic to convert dish map to item map is broken."
