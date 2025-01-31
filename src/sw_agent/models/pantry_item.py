from dataclasses import dataclass
from typing import Optional

@dataclass
class PantryItem:
    name: str
    quantity: float
    unit: str

    def __init__(self, name: str, quantity: float, unit: str):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number")
        if not isinstance(unit, str) or len(unit.strip()) == 0:
            raise ValueError("Unit must be a non-empty string")

        self.name = name.strip()
        self.quantity = quantity
        self.unit = unit.strip()

    def __str__(self):
        return f"{self.name}: {self.quantity}{self.unit}"