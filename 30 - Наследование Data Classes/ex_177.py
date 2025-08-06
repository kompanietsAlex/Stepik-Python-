from dataclasses import dataclass, field
from typing import Any

@dataclass
class Animal:
    """базовый класс для животных"""

    name: str   # имя животного
    old: int    # возраст животного
    weight: Any # вес животного

@dataclass
class Turtle(Animal):
    """черепаха"""

    weight: float # вес черепахи
    length: float # длина черепахи
    speed: float = field(init=False, default=0) # скорость с исключением из инициализатора и значением 0

t = Turtle('Черя', 94, 3.5, 108)
print(t)