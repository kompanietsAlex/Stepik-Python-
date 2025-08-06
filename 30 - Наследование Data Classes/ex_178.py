from dataclasses import dataclass, field, InitVar
from typing import Any


@dataclass
class Table:
    current_id = 0
    id: int = field(init=False, compare=False, default=-1)
    model: str
    color: Any

    def __post_init__(self):
        Table.current_id += 1
        self.id = Table.current_id

@dataclass
class RoundTable(Table):

    radius: InitVar[int] # с типом int: радиус столешницы
    height: int # высота стола
    square: float = field(init=False, compare=False) # площадь с исключением из инициализатора и операций сравнения

    def __post_init__(self, radius):
        super().__post_init__()
        self.square = 3.1415 * radius ** 2

rt = RoundTable("RT", "green", 120, 90)
print(rt.__dict__)