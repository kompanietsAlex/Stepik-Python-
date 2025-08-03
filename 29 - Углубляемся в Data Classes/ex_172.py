from dataclasses import dataclass, field

@dataclass
class PolyLine:
    width: float = field(compare=False) # с исключением из операций сравнения
    color: int = field(compare=False, default=0) # с исключением из операций сравнения и начальным значением 0
    points: list = field(default_factory=list) # список с первый элемент списка - это  кортеж(0, 0)

    def __post_init__(self):
        self.points.append((0, 0))  # добавляем (0, 0) в начало списка точек

pl1 = PolyLine(width=0.5, color=0)
pl2 = PolyLine(width=1.5, color=2)
pl1.points.extend([(10, -5),( 12, 1)]) # добавляем точки в полилинию
pl2.points.extend([(10, -5), (12, 1)]) # добавляем точки в другую полилинию
res = pl1 == pl2  # сравнение полилиний
print(res)  # вывод результата сравнения
