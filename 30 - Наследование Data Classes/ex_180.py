import random
from dataclasses import dataclass, field
from typing import Any


class GlobalGraphData:
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'gray']

    @staticmethod
    def get_color():
        return GlobalGraphData.colors[random.randint(0, len(GlobalGraphData.colors)-1)]

@dataclass
class Graph:

    width: float = field(init=False, compare=False, default=0.5)
    color: Any = field(default_factory=GlobalGraphData.get_color, init=False, compare=False)

@dataclass
class Rect(Graph):
    sp: tuple # координата верхнего левого угла
    ep: tuple # координата нижнего правого угла

    def draw(self):
        return f"Rect: {self.sp}; {self.ep}"

rect = Rect((1, 2), (10, 20))
print(rect)
print(rect.draw())