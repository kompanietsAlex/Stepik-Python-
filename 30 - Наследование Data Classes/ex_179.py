from dataclasses import dataclass, field, InitVar
from typing import Any


class StaticItemData:
    current_id = 0

    @staticmethod
    def get_item_id():
        StaticItemData.current_id += 1
        return StaticItemData.current_id


@dataclass
class Table:
    id: int = field(default_factory=StaticItemData.get_item_id, init=False, compare=False)
    model: str
    color: Any


@dataclass
class SquareTable(Table):
    width: InitVar[int]
    length: InitVar[int]
    height: int = field(default=0)
    square: int = field(init=False, compare=False)

    def __post_init__(self, width, length):
        self.square = width * length


rt = SquareTable("Mozaic Table", 'black', 50, 1024, 85)
print(rt)