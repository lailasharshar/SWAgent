import pytest
from src.sw_agent.models import PantryItem

def test_pantry_item_valid_creation():
    item = PantryItem("Flour", 2.5, "cups")
    assert str(item) == "Flour: 2.5cups"

def test_pantry_item_empty_name():
    with pytest.raises(ValueError) as e:
        PantryItem("", 1, "g")
    assert "Name must be a non-empty string" in str(e.value)

def test_pantry_item_invalid_quantity():
    with pytest.raises(ValueError) as e:
        PantryItem("Eggs", 0, "units")
    assert "Quantity must be a positive number" in str(e.value)

def test_pantry_item_invalid_unit():
    with pytest.raises(ValueError) as e:
        PantryItem("Sugar", 1, "")
    assert "Unit must be a non-empty string" in str(e.value)

def test_pantry_item_type_validation():
    with pytest.raises(ValueError) as e:
        PantryItem(123, "two", [])
    assert "Name must be a non-empty string" in str(e.value)