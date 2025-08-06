from dataclasses import dataclass
from typing import Any


@dataclass
class Thing:
    name: Any
    color: Any
    weight: float

@dataclass
class Table(Thing):
    width: float # ширина стола
    height: float # высота стола


tb = Table('Suprise', 'red', 102.5, 0.45, 10.1)