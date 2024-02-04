import pytest
from main import get_item_universe

def test_duplicate_items_in_universe():
    univ = get_item_universe()
    assert univ['items'].is_unique, 'Universe of items must be unique.'