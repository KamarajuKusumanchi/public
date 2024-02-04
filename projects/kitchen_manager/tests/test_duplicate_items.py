import pytest
from universe import get_item_universe
from inventory import get_inventory


def test_duplicate_items_in_universe():
    univ = get_item_universe()
    assert univ['items'].is_unique, 'Universe of items must be unique.'

def test_duplicate_items_in_inventory():
    inventory = get_inventory()
    assert inventory['items'].is_unique, 'Inventory should not have duplicates.'